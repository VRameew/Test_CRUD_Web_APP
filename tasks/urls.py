"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (create_task, tasks_list, edit_task,
                    task_data, create_comment, delete_task,
                    edit_comment, delete_comment)

urlpatterns = [
    path('tasks_list', tasks_list, name='tasks_list'),
    path('create_task', create_task, name='create_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('task_data/<int:task_id>', task_data, name='task_data'),
    path('delete_task/<int:task_id>}/', delete_task, name='delete_task'),
    path('create_comment/<int:task_id>/', create_comment, name='create_comment'),
    path('edit_comment/<int:comment_id>', edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
]
