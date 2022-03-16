import json
from movies.models import Movie, Category
import requests
import datetime
import os

from cinecube.settings import MEDIA_DIR, MEDIA_ROOT

def get_movies(request):
    
    genre_dict = {12:"Adventure", 14:"Fantasy", 16:"Animation", 18:"Drama",
                      27:"Horror", 28:"Action", 35:"Comedy", 36:"History", 
                      37:"Western", 53:"Thriller", 80:"Crime", 99:"Documentary", 
                      10402:"Music", 9648:"Mystery",878:"Science Fiction",
                      10749:"Romance", 10770:"TV Movie",10752:"War"}
    
    TMDB_KEY = read_tmdb_key()
    
    url = "https://api.themoviedb.org/3/movie/now_playing?api_key=" + TMDB_KEY + "&language=en-US&page=1"
    
    clear_database()
    
    response = requests.get(url)
    data = response.json()
    movies = data['results']
    
    for movie in movies:
        movie_data = Movie(
                id = movie['id'],
                category = set_genre(movie['genre_ids'], genre_dict),
                name = movie['title'],
                description = movie['overview'],
                showing_time = get_date(movie['release_date']),
                poster_path = set_poster_path(movie['poster_path']),
        )
        movie_data.save()
    
        
def set_genre(genre_ids, dict):
    for key in genre_ids:
        if key in dict.keys():   
            genre = get_or_add_genre(dict[key])
            return genre
    return "unknown_type"

def set_poster_path(url):
    base_path = 'https://image.tmdb.org/t/p/w500'
    return base_path + url

def get_date(str):
    info = str.split("-", 3)
    date = datetime.date(int(info[0]), int(info[1]), int(info[2]))
    return date

def get_or_add_genre(value):
    genre = Category.objects.get_or_create(genre = value)[0]
    genre.save()
    return genre

def read_tmdb_key():
    TMDB_KEY = None
    try:
        with open('tmdb.key', 'r') as f:
            TMDB_KEY = f.readline().strip()
    except:
        try:
            with open('../tmdb.key') as f:
                TMDB_KEY = f.readline().strip()
        except:
            raise IOError('tmdb.key not found')
        
    if not TMDB_KEY:
        raise KeyError('tmdb key not found')
    
    return TMDB_KEY

def clear_database():
    if Category.objects.all():
        for cat in Category.objects.all():
            print(cat.genre + " deleted")
            Category.objects.filter(genre = cat.genre).delete()
