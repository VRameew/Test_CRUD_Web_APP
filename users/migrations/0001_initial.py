# Generated by Django 5.0 on 2023-12-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email')),
                ('user_name', models.CharField(db_index=True, max_length=25, unique=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=30, verbose_name='name')),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=30, verbose_name='surname')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='registered')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'indexes': [models.Index(fields=['email'], name='users_userm_email_40b93c_idx'), models.Index(fields=['user_name'], name='users_userm_user_na_8ae8b2_idx'), models.Index(fields=['first_name'], name='users_userm_first_n_636ea8_idx'), models.Index(fields=['last_name'], name='users_userm_last_na_ba5bbc_idx')],
            },
        ),
    ]
