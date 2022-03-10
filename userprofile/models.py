from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField('nickname', max_length=32, unique=True)  # nickname
    password = models.CharField(max_length=200)  # password
    email = models.CharField('email', max_length=64, unique=True)  # email
    token = models.CharField(max_length=250, default='')

    # create user
    @classmethod
    def createuser(cls, username, password, email, token):
        u = cls(username=username, password=password, email=email, token=token)
        return u

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
