# Author: Zhi Kai
# Time:  14:59
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinecube.settings')

import django
django.setup()
from userprofile.models import UserProfile
from django.contrib.auth.models import User

def populate():

    u1 = User(username="Aabbye",email="Aabbye12345@gmail.com")
    u2 = User(username="Abby",email="Abby12345@gmail.com")
    u3 = User(username="Abbie",email="Abbie12345@gmail.com")

    u1.save()
    u2.save()
    u3.save()

    example_user = [

        {'user': u1,
         'userID': "6e57ed57-1c61-44d9-8ed2-d85d41296c6c",
         'address': 'qweqqweqweqw',
         },
        {'user': u2,
         'userID': "ead72316-bbc4-4faa-9c8b-ea8190de9bc8",
         'address': 'qweqqweqweqw',
         },
        {'user': u3,
         'userID': "efc936b7-6ba0-4ca3-85a8-cea8f53dd76a",
         'address': 'qweqqweqweqw',
         },
        ]

    for u in example_user:
        add_user(u['user'],u['userID'],u['address'])

def add_user(user,userID,address):
    user = UserProfile.objects.get_or_create(user=user,userID=userID,address=address)
    print(user)

if __name__ == '__main__':
    print('Starting userfile population script...')
    populate()