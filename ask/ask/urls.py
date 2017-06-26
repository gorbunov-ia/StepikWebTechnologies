"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa.views import test, question_info, questions_new, questions_popular, question_add,signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', questions_new, name='questions_new'),
    #url(r'^login/$', auth_views.LoginView.as_view()), #django 1.11
    url(r'^login/$', auth_views.login), #django 1.10
    #url(r'^logout/$', auth_views.LogoutView.as_view()),
    url(r'^signup/$', signup),
    url(r'^question/(?P<q_id>\d+)/$', question_info, name='question-info'),
    url(r'^ask/$', question_add, name='question_add'),
    url(r'^popular/$', questions_popular),
    url(r'^new/$', test),
]