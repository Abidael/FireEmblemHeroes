from django.test import TestCase
from .models import Post

# Create your tests here.

class PostTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Post.objects.create(autor="autor", titulo="titulo")

    def test_post(self):
        post1 = post.objects.get(id=1)
        field_label = post1._meta.get_field('nombre').verbose_name 
        self.assertEqual(field_label,"nombre")