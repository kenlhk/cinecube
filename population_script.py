# Author: Zhi Kai
# Time:  14:59
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinecube.settings')

import django
django.setup()
from userprofile.models import UserProfile
from django.contrib.auth.models import User

def populate():
    
    if UserProfile.objects.all():
        for user in UserProfile.objects.all():
            user.delete()

    if User.objects.all():
        for user in User.objects.all():
            user.delete()                    

    u1 = User(username="Alice",email="alice@gmail.com")
    u2 = User(username="Bernie",email="bernie@gmail.com")
    u3 = User(username="Cindy",email="cindy@gmail.com")
    u4 = User(username="Dandy",email="dandy@gmail.com")
    u5 = User(username="Edward",email="edward@gmail.com")
    u6 = User(username="Henry",email="henry@gmail.com")

    u1.save()
    u2.save()
    u3.save()
    u4.save()
    u5.save()
    u6.save()

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
        {'user': u4,
         'userID': "dc8b0030-c3ee-4d0a-9e4f-787b65604dc1",
         'address': 'qweqqweqweqw',
        },
        {'user': u5,
         'userID': "637af820-632f-4738-a478-7cc0d34d980c",
         'address': 'qweqqweqweqw',
        },
        {'user': u6,
         'userID': "999ae667-39c7-4038-b0ba-e916e320e7d0",
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