# Generated by Django 5.0 on 2023-12-06 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_taskstatus_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskstatus',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]