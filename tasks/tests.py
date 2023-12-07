from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Task, TaskStatus, Comments
from .forms import (TaskForm, TaskEditForm,
                    TaskDeleteForm, CommentsForm,
                    CommentsEditForm, CommentsDeleteForm)

User = get_user_model()


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@email.com',
                                             password='testpassword')
        self.task = Task.objects.create(text='Test task',
                                        author=self.user)

    def test_task_text(self):
        self.assertEqual(self.task.text, 'Test task')

    def test_task_author(self):
        self.assertEqual(self.task.author, self.user)


class TaskStatusModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@email.com',
                                             password='testpassword')
        self.task = Task.objects.create(text='Test task',
                                        author=self.user)
        self.status = TaskStatus.objects.create(task_status_index_name_idx=self.task,
                                                status='В ожидани')

    def test_task_status_task(self):
        self.assertEqual(self.status.task_status_index_name_idx, self.task)

    def test_task_status_status(self):
        self.assertEqual(self.status.status, 'В ожидани')


class CommentsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@email.com',
                                             password='testpassword')
        self.task = Task.objects.create(text='Test task',
                                        author=self.user)
        self.comment = Comments.objects.create(task_comments_index_name_idx=self.task,
                                               text='Test comment')

    def test_comment_task(self):
        self.assertEqual(self.comment.task_comments_index_name_idx, self.task)

    def test_comment_text(self):
        self.assertEqual(self.comment.text, 'Test comment')


class TaskFormTest(TestCase):
    def test_task_form_fields(self):
        form = TaskForm()
        self.assertEqual(form.Meta.model, Task)
        self.assertEqual(form.Meta.fields, ['text'])
        self.assertEqual(form.Meta.labels, {'text': 'Название задачи'})


class TaskEditFormTest(TestCase):
    def test_task_edit_form_fields(self):
        form = TaskEditForm()
        self.assertEqual(form.Meta.model, Task)
        self.assertEqual(form.Meta.fields, ['text', 'status'])
        self.assertEqual(form.Meta.labels, {'text': 'Название задачи', 'status': 'Статус'})
        self.assertTrue('status' in form.fields)


class TaskDeleteFormTest(TestCase):
    def test_task_delete_form_fields(self):
        form = TaskDeleteForm()
        self.assertEqual(form.Meta.model, Task)
        self.assertEqual(form.Meta.fields, [])


class CommentsFormTest(TestCase):
    def test_comments_form_fields(self):
        form = CommentsForm()
        self.assertEqual(form.Meta.model, Comments)
        self.assertEqual(form.Meta.fields, ['task_comments_index_name_idx', 'text'])
        self.assertEqual(form.Meta.labels, {'task_comments_index_name_idx': 'Задача', 'text': 'Текст комментария'})
        self.assertTrue('task_comments_index_name_idx' in form.fields)
        self.assertTrue(form.fields['task_comments_index_name_idx'].widget.attrs['readonly'])


class CommentsEditFormTest(TestCase):
    def test_comments_edit_form_fields(self):
        form = CommentsEditForm()
        self.assertEqual(form.Meta.model, Comments)
        self.assertEqual(form.Meta.fields, ['task_comments_index_name_idx', 'text'])
        self.assertEqual(form.Meta.labels, {'task_comments_index_name_idx': 'Задача', 'text': 'Текст комментария'})


class CommentsDeleteFormTest(TestCase):
    def test_comments_delete_form_fields(self):
        form = CommentsDeleteForm()
        self.assertEqual(form.Meta.model, Comments)
        self.assertEqual(form.Meta.fields, [])
