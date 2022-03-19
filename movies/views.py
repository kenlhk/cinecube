
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

def genre_list(request):
    context_dict = {}
    
    try:
        genre_list = Category.objects.all()
        context_dict['list'] = genre_list
    except Movie.DoesNotExist:
        context_dict['list'] = None
        
    return render(request, 'movies/movies_genres.html', context=context_dict) 
    

def show_movie(request, movie_id_slug):
    context_dict = {}
    
    try:
        movie = Movie.objects.get(slug=movie_id_slug)
        context_dict['movie'] = movie
        context_dict['movie_id'] = movie_id_slug
    except Movie.DoesNotExitst:
        context_dict['movie'] = None
        context_dict['movie_id'] = None
    
    return render(request, 'movies/movies_movie.html', context=context_dict)

def show_genre(request, genre_name_slug):
    context_dict = {}
    
    try:
        genre = Category.objects.get(slug=genre_name_slug)
        movies = Movie.objects.filter(category=genre)
        
        context_dict['category'] = genre
        context_dict['contents'] = movies
        
    except Movie.DoesNotExitst:
        context_dict['category'] = None
        context_dict['contents'] = None
    
    return render(request, 'movies/movies_genre_page.html', context=context_dict)

