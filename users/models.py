from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Данные пользователя обязательно должны содержать email')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        db_index=True
    )
    user_name = models.CharField(
        verbose_name='username',
        max_length=25,
        unique=True,
        db_index=True
    )
    first_name = models.CharField(
        verbose_name='name',
        max_length=30,
        blank=True,
        db_index=True
    )
    last_name = models.CharField(
        verbose_name='surname',
        max_length=30,
        blank=True,
        db_index=True
    )
    date_joined = models.DateTimeField(
        verbose_name='registered',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        verbose_name='is_active',
        default=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Возвращает first_name и last_name с пробелом между ними.
        """
        return f'{self.first_name} {self.last_name}'
