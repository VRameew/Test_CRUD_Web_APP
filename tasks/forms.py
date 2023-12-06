from django import forms
from .models import (Task, TaskStatus,
                     Comments)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        labels = {'text': 'Название задачи'}


class TaskEditForm(forms.ModelForm):
    status = forms.ChoiceField(choices=TaskStatus.tasks_status)

    class Meta:
        model = Task
        fields = ['text', 'status']
        labels = {
            'text': 'Название задачи',
            'status': 'Статус'
        }


class TaskDeleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = []


class CommentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['task'].widget.attrs['readonly'] = True  # Заблокировать поле task в форме

    class Meta:
        model = Comments
        fields = ['task', 'text']
        labels = {
            'task': 'Задача',
            'text': 'Текст комментария'
        }


class CommentsEditForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['task', 'text']
        labels = {
            'task': 'Задача',
            'text': 'Текст комментария'
        }


class CommentsDeleteForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = []