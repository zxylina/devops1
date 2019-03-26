#!/bin/python

import sys
import os

# pwd = os.path.realpath(__file__)
# print(os.path.dirname(pwd))

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops1.settings")

import django
django.setup()

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

def get_users():
    for user in User.objects.all():
        print(user.username)

def create_user(name):
    for i in range(2, 4):
        username = "{}-{}".format(name, i)
        User.objects.create_user(username, "{}@kq300061.com".format(username), "1234567")

if __name__ == "__main__":
    create_user('zhangxiying')
    get_users()