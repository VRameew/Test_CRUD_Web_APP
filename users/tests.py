from django.test import TestCase
from .models import UserModel


# Create your tests here.
class UserModelTest(TestCase):
    def test_create_users(self):
        user1 = UserModel.objects.create_user(
            user_name='One',
            email='1@email.com',
            password='One1One')
        user2 = UserModel.objects.create_user(
            email='2@email.com',
            password='Two2Two',
            user_name="SecondUser")
        user3 = UserModel.objects.create_user(
            user_name='Three',
            email='3@email.com',
            password='Tree3Three')
