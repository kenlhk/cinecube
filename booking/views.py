from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect


from booking import forms
from movies.models import Movie, Category

from .models import Booking

from time import gmtime, strftime
import datetime

# Create your views here.
def show_booking(request, movie_id):
    context_dict = {}
    try:
        movie = Movie.objects.get(slug=movie_id)
        context_dict['movie_id'] = movie_id
        context_dict['movie'] = movie
        context_dict['current_date'] = datetime.datetime.now().strftime ("%Y-%m-%d")

        now = datetime.datetime.now()
        oneWeek = datetime.timedelta(weeks = 1)
        newDate = now + oneWeek

        context_dict['week_date'] = newDate.strftime("%Y-%m-%d")
    except Movie.DoesNotExist:
        context_dict['movie'] = None

    return render(request, 'booking/book.html', context=context_dict)


# Create your views here.
def confirm_booking(request, movie_id):
    context_dict = {}
    movie = Movie.objects.get(slug=movie_id)

    if request.method == 'POST':
        try:
            date = request.POST.get('date')
            time = request.POST.get('time')

            context_dict['movie_id'] = movie_id
        
            context_dict['movie'] = movie
            context_dict['date'] = date
            context_dict['time'] = time

            book = Booking.createbooking(movie_id=movie_id, date=date, time=time)
            book.save()
        except:
         context_dict['error'] = "Error with booking. Please try again."
        return render(request, 'booking/confirm.html', context=context_dict)
    context_dict['error'] = "Error with booking. Please try again."
    return HttpResponseRedirect("", context=context_dict)

# Create your views here.
def my_bookings(request):
    context_dict = {}
    movies = []

    try:
        bookings = Booking.objects.all()

        for b in bookings:
            movies.append(Movie.objects.get(slug=b.movie_id))

        context_dict['bookings'] = bookings
        context_dict['movies'] = movies
        context_dict['movie_booking'] = zip(bookings, movies)
    except Booking.DoesNotExist:
        context_dict['bookings'] = None
        context_dict['movies'] = None
        context_dict['error'] = "No current bookings."
    return render(request, 'booking/mybookings.html', context=context_dict)


