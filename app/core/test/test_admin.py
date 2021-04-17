'''
File: test-admin.py
Project: test
File Created: Saturday, 17th April 2021 11:45:07 am
Author: Ananda Yudhistira (anandabayu12@gmail.com)
-----
Last Modified: Saturday, 17th April 2021 12:27:42 pm
Modified By: Ananda Yudhistira (anandabayu12@gmail.com>)
-----
Copyright 2021 Ananda Yudhistira, FAN Integrasi Teknologi, PT
'''
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='P@ssw0rd'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@gmail.com',
            password='P@ssw0rd',
            name='User Test'
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_change_user(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
