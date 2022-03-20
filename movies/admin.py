from django.contrib import admin
from movies.models import Movie, Category, Review


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


# Register your models here.
admin.site.register(Category)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
