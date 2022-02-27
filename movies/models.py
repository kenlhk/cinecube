from datetime import datetime
from distutils.command.upload import upload
from encodings import utf_8
from msilib.schema import Directory
from unicodedata import name
from django.db import models
from django.template.defaultfilters import slugify

from PIL import Image
from django.core.files import File
import os
import urllib.request as req

from cinecube.settings import MEDIA_DIR, MEDIA_ROOT, MEDIA_URL, BASE_DIR

# Create your models here.
class Category(models.Model):
    genre = models.CharField(max_length = 256, unique = True)
    
    def __str__(self):
        return self.genre
    
class Movie(models.Model):
    id = models.IntegerField(primary_key = True, unique = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    #total_score to be added
    name = models.CharField(max_length = 256)
    #director = models.CharField(max_length = 128)
    description = models.CharField(max_length = 4000)
    showing_time = models.DateField()
    #poster image
    poster_path = models.URLField(null = True)
    slug = models.SlugField()
    
    def get_image_from_url(self):
        # result = req.urlretrieve(self.poster_path)
        # self.poster_file.save(
        #     os.path.basename(self.poster_path),
        #     File(open(result[0]))
        #     )
        
        request = req.Request(self.poster_path)
        pic = req.urlopen(request)
        with open(os.path.basename(self.poster_path), 'wb') as localFile:
            localFile.write(pic.read())
    
    def save(self, *args, **kwargs):
        #self.get_image_from_url()
        self.slug = slugify(self.id)
        super(Movie, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    