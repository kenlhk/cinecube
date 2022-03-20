# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True, unique=True)
    movie_id = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=20)
    person = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # email = models.CharField('email', max_length=64, unique=True)  # email

    class Meta:
        db_table = 'booking'

    # create user
    @classmethod
    def createbooking(cls, movie_id, date, time, person, user):
        b = cls(movie_id=movie_id, date=date, time=time, person=person, user=user)
        return b

    def __str__(self):
        return '{}'.format(self.booking_id)
