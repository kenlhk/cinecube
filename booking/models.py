# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True, unique=True)
    movie_id = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # email = models.CharField('email', max_length=64, unique=True)  # email

    class Meta:
        db_table = 'booking'

    # create user
    @classmethod
    def createbooking(cls, movie_id, date, time, user):
        b = cls(movie_id=movie_id, date=date, time=time, user=user)
        return b

    def __str__(self):
        return self.booking_id
