# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def test(request, *args, **kwargs):
    return HttpResponse('OK')

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from qa.forms import AnswerForm

#@require_GET
@login_required
def question_info(request, q_id):
    question = get_object_or_404(Question, id = q_id)
    try:
        answers = question.answer_set.all()[:]
    except Answer.DoesNotExist:
        answers = None

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.question = q_id
            form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        #GET
        form = AnswerForm()

    return render(request, 'qa/question_info.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

from django.core.paginator import Paginator, EmptyPage


@require_GET
def questions_new(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit',10)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions,limit)
    paginator.baseurl = '?page='
    try:
        page = paginator.page(page) #Page
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/questions_new.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page':page,
    })

@require_GET
def questions_popular(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit',10)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions,limit)
    paginator.baseurl = '?page='
    try:
        page = paginator.page(page) #Page
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/questions_popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page':page,
    })

from qa.forms import AskForm


@login_required
def question_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        #'GET'
        form = AskForm()
    return render(request, 'qa/question_add.html', {
            'form' : form
        })

from qa.forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if form.is_valid():
            user_new = form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect(reverse('questions_new'))
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {
        "form": form
    })

#def login(request):

