# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer

@require_GET
def question_info(request, q_id):
    question = get_object_or_404(Question, id = q_id)
    try:
        answers = question.answer_set.all()[:]
    except Answer.DoesNotExist:
        answers = None
    return render(request, 'qa/question_info.html', {
        'question': question,
        'answers': answers,
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