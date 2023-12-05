from django.shortcuts import (render, get_object_or_404,
                              redirect)
from .models import Task, Comments
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
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskEditForm(instance=task)

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
def create_comment(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('comments_list')
    else:
        form = CommentsForm()

    return render(
        request,
        'create_comment.html',
        {'form': form})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)

    if request.user != comment.author:
        return redirect('comments_list')

    if request.method == 'POST':
        form = CommentsEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comments_list')
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

    if request.user != comment.author:
        return redirect('comments_list')

    if request.method == 'POST':
        form = CommentsDeleteForm(request.POST, instance=comment)
        if form.is_valid():
            comment.delete()
            return redirect('comments_list')
    else:
        form = CommentsDeleteForm(instance=comment)

    return render(
        request,
        'delete_comment.html',
        {'form': form,
         'comment': comment})
