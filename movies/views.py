
from django.shortcuts import render
from movies.load_info import get_movies
from movies.models import Movie, Category

# Create your views here.

def index(request):
    
    get_movies(request)
    
    context_dict = {}
    context_dict['title'] = "CineCube"
    context_dict['now_playing'] = Movie.objects.order_by('showing_time')[:5]
    
    return render(request, 'movies/movies_index.html', context=context_dict)

def movie_list(request):
    context_dict = {}
    
    try:
        now_playing_list = Movie.objects.all()
        context_dict['list'] = now_playing_list
    except Movie.DoesNotExist:
        context_dict['list'] = None
        
    return render(request, 'movies/movies_list.html', context=context_dict)    
    

def show_movie(request, movie_id_slug):
    context_dict = {}
    
    try:
        movie = Movie.objects.get(slug=movie_id_slug)
        context_dict['movie'] = movie
    except Movie.DoesNotExitst:
        context_dict['movie'] = None
    
    return render(request, 'movies/movies_movie.html', context=context_dict)

