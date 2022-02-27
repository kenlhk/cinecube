from django.urls import path
from movies import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('<slug:movie_id_slug>/', views.show_movie, name='movie_page'),
]