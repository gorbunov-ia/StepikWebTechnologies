from django import forms

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    #question = forms.IntegerField()

    def clean(self):
        return self.cleaned_data

    def save(self):
        #answer = Answer(**self.cleaned_data)
        answer = Answer()
        answer.text = self.cleaned_data['text']
        #answer.question_id = self.cleaned_data['question']
        answer.question_id = self.question
        answer.author_id = 1
        #answer.question_id = self.changed_data.__getattribute__('question')
        answer.save()
        return answer



