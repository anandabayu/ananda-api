'''
File: test_models.py
Project: test
File Created: Saturday, 17th April 2021 11:17:10 am
Author: Ananda Yudhistira (anandabayu12@gmail.com)
-----
Last Modified: Saturday, 17th April 2021 11:42:45 am
Modified By: Ananda Yudhistira (anandabayu12@gmail.com>)
-----
Copyright 2021 Ananda Yudhistira, FAN Integrasi Teknologi, PT
'''
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_positive(self):
        email = 'test@gmail.com'
        password = 'P@ssw0rd'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'P@ssw0rd')

    def test_create_superuser_positive(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com', 'P@ssw0rd'
        )

        self.assertTrue(user.is_superuser)
