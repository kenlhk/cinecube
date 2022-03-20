from django.http import HttpResponseRedirect
from django.shortcuts import render
from movies.load_info import get_movies
from movies.populate_reviews import populate_reviews
from movies.models import Movie, Category, Review
from movies import forms


# Create your views here.

def index(request):
    get_movies(request)
    # populate_reviews()

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
        if request.method == 'POST':
            form = forms.ReviewForm(request.POST)
            if form.is_valid():
                id = len(Review.objects.all()) + 1
                comment = request.POST.get('comment')
                score = request.POST.get('score')
                review = Review.objects.create(id=id, target=movie, reviewer=request.user, comment=comment, score=score)
                review.save()
                return HttpResponseRedirect(request.path_info)

        context_dict['movie'] = movie
        context_dict['movie_id'] = movie_id_slug

        # Review section
        if request.user.is_authenticated:
            context_dict['review_form'] = forms.ReviewForm()

        reviews = Review.objects.filter(target=movie)
        context_dict['reviews'] = reviews
    except Movie.DoesNotExist:
        context_dict['movie'] = None
        context_dict['movie_id'] = None
        context_dict['reviews'] = None

    return render(request, 'movies/movies_movie.html', context=context_dict)


def show_genre(request, genre_name_slug):
    context_dict = {}

    try:
        genre = Category.objects.get(slug=genre_name_slug)
        movies = Movie.objects.filter(category=genre)

        context_dict['category'] = genre
        context_dict['contents'] = movies

    except Movie.DoesNotExist:
        context_dict['category'] = None
        context_dict['contents'] = None

    return render(request, 'movies/movies_genre_page.html', context=context_dict)
