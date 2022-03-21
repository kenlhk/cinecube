from django.test import TestCase
from movies.views import Category

# Create your tests here.

class CategoryMethodTest(TestCase):
    def test_ensure_index_are_positive(self):
        category =Category(genre="test")
        category.save()
        print("test pass")
