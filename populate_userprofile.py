# Author: Zhi Kai
# Time:  14:59
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinecube.settings')

import django
django.setup()
from userprofile.models import User

def populate():
    example_user = [
        {'nickname': 'Tony',
         'password': '123456qwe',
         'email': 'Tony123456@gmail.com',
         'token':'pbkdf2_sha256$120000$stCazQuy8XVG$a1I32j4KagSAL/8r6v7a8i898lynTdC0FmtdSqPajco='},
        {'nickname': 'Alex',
         'password': '123456qwe',
         'email': 'Alex123456@gmail.com',
         'token': 'pbkdf2_sha256$120000$qbOJ4SSo8bbe$TJJAUUkgTi0vcp5yHb0uXXeYbtSd2K2eSeWr5ry6a6A='},
        {'nickname': 'Andy',
         'password': '123456qwe',
         'email': 'Andy123456@gmail.com',
         'token': 'pbkdf2_sha256$120000$aadgeofStsjd$SxCRYL0HKKRgztgiv0aHoi5eTUFD9HtpV2bSIgFvxJE='},
        ]

    for u in example_user:
        add_user(u['nickname'],u['email'],u['password'],u['token'])

def add_user(nickname,email,password,token):
    user = User.objects.get_or_create(username=nickname,email=email,password=password,token=token)
    print(user)

if __name__ == '__main__':
    print('Starting userfile population script...')
    populate()