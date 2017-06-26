from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    # def __init__(self, user, **kwargs):
    #     self._user = user
    #     super(AskForm, self).__init__(**kwargs)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    #question = forms.IntegerField()

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        #self.cleaned_data['question'] = self._question
        answer = Answer(**self.cleaned_data)
        #answer = Answer()
        #answer.text = self.cleaned_data['text']
        #answer.question_id = self._question
        answer.question_id = self.question
        #answer.author_id = self._user
        #answer.author_id = self.cleaned_data['author']
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        return self.cleaned_data

    def save(self):
        #user = User.objects.create_user(self.cleaned_data['username'],None,self.cleaned_data['password'])
        user = User()
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        user.save()
        return user

    class Meta:
        model = User

