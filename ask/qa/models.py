# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at','-id')
    def popular(self):
        return self.order_by('-rating','-id')

#Question - вопрос
class Question(models.Model):
    objects = QuestionManager()
    # title - заголовок вопроса
    title = models.CharField(max_length=255)
    #text - полный текст вопроса
    text = models.TextField()
    #added_at - дата добавления вопроса
    added_at = models.DateTimeField(auto_now_add=True)
    #rating - рейтинг вопроса(число)
    rating = models.IntegerField(default=0)
    #author - автор вопроса
    author = models.ForeignKey(User)
    #likes - список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(User, related_name='likes_set')

    def get_url(self):
        return reverse('question-info',
            kwargs={'q_id':self.id})
    def __unicode__(self):
        return self.title

    class Meta:
            ordering = ['-added_at']

#Answer - ответ
class Answer(models.Model):
    #text - текст ответа
    text = models.TextField()
    #added_at - дата добавления ответа
    added_at = models.DateTimeField(auto_now_add=True)
    #question - вопрос, к которому относится ответ
    question = models.ForeignKey(Question)
    #author - автор ответа
    author = models.ForeignKey(User)
    class Meta:
            ordering = ['-added_at']