from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=300,
                            verbose_name='task_name',
                            db_index=True)
    author = models.ForeignKey(get_user_model(),
                               default=None,
                               on_delete=models.CASCADE,
                               related_name='tasks',
                               verbose_name='author',
                               db_index=True)
    date_created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    def __str__(self):
        return self.text

    class Meta:
        indexes = [
            models.Index(fields=['text']),
            models.Index(fields=['author']),
        ]


class TaskStatus(models.Model):
    tasks_status = (
        ('Не приступали', 'Не приступали'),
        ('В ожидани', 'В ожидани'),
        ('В работе', 'В работе'),
        ('Завершена', 'Завершена'),
    )
    task = models.OneToOneField(Task,
                                on_delete=models.CASCADE,
                                db_index=True,
                                name='task_status_index_name_idx')
    status = models.CharField(max_length=15,
                              choices=tasks_status,
                              default='Не приступали',
                              verbose_name='task_status',
                              db_index=True)

    def __str__(self):
        return self.status

    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['task_status_index_name_idx']),
        ]


class Comments(models.Model):
    task = models.ForeignKey(Task,
                             default=None,
                             on_delete=models.CASCADE,
                             related_name='task_comments',
                             db_index=True,
                             name='task_comments_index_name_idx',
                             db_constraint=False)
    text = models.TextField(db_index=True)
    date_created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    def __str__(self):
        return self.text

    class Meta:
        indexes = [
            models.Index(fields=['text']),
            models.Index(fields=['task_comments_index_name_idx']),
        ]
