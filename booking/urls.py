from django.urls import path
from booking import views

app_name = 'booking'

urlpatterns = [
    path('mybookings/', views.my_bookings, name='mybookings'),
    path('<movie_id>/', views.show_booking, name='book'),
    path('<movie_id>/confirm/', views.confirm_booking, name='confirm'),
]