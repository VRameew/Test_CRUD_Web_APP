from django.test import TestCase, Client
from .models import UserModel
from .forms import UserRegistrationForm, LoginForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from .views import register, user_login, user_update, change_password


class UserModelTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email='test@test.com', password='test123')

    def test_create_user(self):
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertTrue(self.user.check_password('test123'))

    def test_create_superuser(self):
        UserModel.objects.all().delete()  # Удаляем все записи из модели UserModel
        superuser = UserModel.objects.create_superuser(
            email='admin@test.com',
            password='admin123',
            user_name='admin'
        )
        self.assertEqual(superuser.email, 'admin@test.com')
        self.assertEqual(superuser.user_name, 'admin')
        self.assertTrue(superuser.check_password('admin123'))
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_get_full_name(self):
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'
        self.user.save()
        full_name = self.user.get_full_name()
        self.assertEqual(full_name, 'John Doe')

    def test_user_model_fields(self):
        self.assertEqual(self.user._meta.get_field('email').verbose_name, 'email')
        self.assertTrue(self.user._meta.get_field('email').unique)
        self.assertTrue(self.user._meta.get_field('email').db_index)
        self.assertEqual(self.user._meta.get_field('user_name').verbose_name, 'username')
        self.assertTrue(self.user._meta.get_field('user_name').unique)
        self.assertTrue(self.user._meta.get_field('user_name').db_index)
        self.assertEqual(self.user._meta.get_field('first_name').verbose_name, 'name')
        self.assertEqual(self.user._meta.get_field('last_name').verbose_name, 'surname')
        self.assertTrue(self.user._meta.get_field('date_joined').auto_now_add)
        self.assertTrue(self.user._meta.get_field('is_active').default)


class UserRegistrationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'email': 'test@example.com',
            'user_name': 'testuser',
            'password': 'testpass',
            'first_name': 'Test',
            'last_name': 'User'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_existing_email(self):
        form_data = {
            'email': 'test@example.com',
            'user_name': 'testuser',
            'password': 'testpass',
            'first_name': 'Test',
            'last_name': 'User'
        }
        # Создаем пользователя с таким же email вручную
        UserModel.objects.create_user(email='test@example.com', password='password')
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_invalid_form_existing_user_name(self):
        # Создаем пользователя с таким же user_name вручную
        UserModel.objects.create(email='another@example.com', password='password', user_name='testuser')

        form_data = {
            'email': 'test@example.com',
            'user_name': 'testuser',
            'password': 'testpass',
            'first_name': 'Test',
            'last_name': 'User'
        }
        form = UserRegistrationForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('user_name', form.errors)

    def test_invalid_form_missing_fields(self):
        form_data = {
            'email': 'test@example.com',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('user_name', form.errors)
        self.assertIn('password', form.errors)


class LoginFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'email': 'test@example.com',
            'password': 'testpass'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        form_data = {
            'email': 'test@example.com',
        }
        form = UserRegistrationForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('user_name', form.errors)
        self.assertIn('password', form.errors)


class RegisterViewTest(TestCase):
    def test_register_view_get(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertIn('form', response.context)

    def test_register_view_post_valid_form(self):
        form_data = {
            'email': 'test@example.com',
            'user_name': 'testuser',
            'password': 'testpass',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(reverse('registration'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Перенаправление после успешной регистрации
        self.assertRedirects(response, reverse('success'))

    def test_register_view_post_invalid_form(self):
        # Создаем пользователя с таким же email вручную
        get_user_model().objects.create_user(email='test@example.com', password='password')

        form_data = {
            'email': 'test@example.com',
            'user_name': 'testuser',
            'password': 'testpass',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(reverse('registration'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertIn('form', response.context)
        self.assertIn('email', response.context['form'].errors)


class UserLoginViewTest(TestCase):
    def test_user_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn('form', response.context)

    def test_user_login_view_post_valid_form(self):
        user = get_user_model().objects.create_user(email='test@example.com', password='testpass')
        form_data = {
            'email': 'test@example.com',
            'password': 'testpass'
        }
        response = self.client.post(reverse('login'), data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_user_login_view_post_invalid_form(self):
        user = get_user_model().objects.create_user(email='test@example.com', password='testpass')
        form_data = {
            'email': 'test@example.com',
            'password': 'wrongpass'
        }
        response = self.client.post(reverse('login'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn('form', response.context)


class UserUpdateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword',
        )

    def test_user_update(self):
        self.client.login(
            username='testuser@example.com',
            password='testpassword',
        )
        response = self.client.post(
            reverse('user_data_update'),
            {
                'email': 'newemail@example.com',
                'user_name': 'newusername',
                'first_name': 'New',
                'last_name': 'User',
            },
        )
        self.assertEqual(response.status_code, 302)  # Проверка статус кода
