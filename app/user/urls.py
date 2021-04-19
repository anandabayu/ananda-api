'''
File: urls.py
Project: user
File Created: Monday, 19th April 2021 12:38:32 pm
Author: Ananda Yudhistira (anandabayu12@gmail.com)
-----
Last Modified: Monday, 19th April 2021 1:27:42 pm
Modified By: Ananda Yudhistira (anandabayu12@gmail.com>)
-----
Copyright 2021 Ananda Yudhistira, FAN Integrasi Teknologi, PT
'''
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
