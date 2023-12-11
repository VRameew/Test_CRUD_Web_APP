from django.shortcuts import (render, get_object_or_404,
                              redirect)
from .models import Task, Comments, TaskStatus
from .forms import (TaskForm, TaskEditForm,
                    TaskDeleteForm, CommentsForm,
                    CommentsEditForm, CommentsDeleteForm)
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            status, created = TaskStatus.objects.get_or_create(task_status_index_name_idx=task)
            return redirect('tasks_list')
    else:
        form = TaskForm()

    return render(
        request,
        'create_task.html',
        {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user != task.author:
        return redirect('tasks_list')

    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)  # Получаем объект Task из формы без сохранения в базу данных
            task.save()  # Сохраняем изменения

            # Обновляем статус задачи
            status, created = TaskStatus.objects.get_or_create(task_status_index_name_idx=task)
            status.status = form.cleaned_data['status']  # Получаем новый статус из формы
            status.save()

            # Обновляем форму с обновленным объектом task и объектом status
            form = TaskEditForm(instance=task)
            form.fields['status'].initial = status.status  # Устанавливаем значение статуса в форме

            return redirect(f'/tasks/task_data/{task_id}')
    else:
        form = TaskEditForm(instance=task)
        status, created = TaskStatus.objects.get_or_create(task_status_index_name_idx=task)
        form.fields['status'].initial = status.status  # Устанавливаем значение статуса в форме

    return render(
        request,
        'edit_task.html',
        {'form': form,
         'task': task})



@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user != task.author:
        return redirect('tasks_list')

    if request.method == 'POST':
        form = TaskDeleteForm(request.POST, instance=task)
        if form.is_valid():
            task.delete()
            return redirect('tasks_list')
    else:
        form = TaskDeleteForm(instance=task)

    return render(
        request,
        'delete_task.html',
        {'form': form,
         'task': task})


@login_required
def create_comment(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = task
            comment.save()
            return redirect(f'/tasks/task_data/{task_id}')
    else:
        form = CommentsForm(initial={'task': task})

    return render(
        request,
        'create_comment.html',
        {'form': form}
    )


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)

    if request.method == 'POST':
        form = CommentsEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(f'/tasks/task_data/{comment.task_comments_index_name_idx_id}')
    else:
        form = CommentsEditForm(instance=comment)

    return render(
        request,
        'edit_comment.html',
        {'form': form,
         'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)

    if request.method == 'POST':
        form = CommentsDeleteForm(request.POST, instance=comment)
        if form.is_valid():
            comment.delete()
            return redirect('tasks_list')
    else:
        form = CommentsDeleteForm(instance=comment)

    return render(
        request,
        'delete_comment.html',
        {'form': form,
         'comment': comment})


@login_required
def tasks_list(request):
    tasks = Task.objects.filter(author=request.user)
    return render(
        request,
        'tasks_list.html',
        {'tasks': tasks})


@login_required
def task_data(request, task_id):
    task = Task.objects.filter(id=task_id).first()
    print(task)
    status = TaskStatus.objects.filter(task_status_index_name_idx=task).first()
    print(status)
    comments = Comments.objects.filter(task_comments_index_name_idx=task)
    print(comments)
    return render(request,
                  'task_data.html',
                  {
                      'task': task,
                      'status': status,
                      'comments': comments,
                  })
