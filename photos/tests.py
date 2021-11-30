from django.test import TestCase
from .models import Photo,Category

# Create your tests here.
class CategoryTest(TestCase):

    def setUp(self):
        self.travel = Category(name='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))

    def test_save(self):
        self.travel.save_category()
        categoriess = Category.objects.all()
        self.assertTrue(len(categoriess) > 0)

    def test_delete(self):
        self.travel.save_category()
        self.travel.delete_category()
        categoriess = Category.objects.all()
        self.assertTrue(len(categoriess) == 0)



class PhotoTest(TestCase):

    def setUp(self):
        # Creating a new editor and saving it

        self.Travelling = Photo(description = 'Travelling')
        self.Travelling.save_photo()

        # Creating a new tag and saving it
        self.new_photo = Category(name = 'testing')
        self.new_photo.save()

        self.new_photo = Photo(description = 'This is a random test Photo', location = 'Test photo', image='', category = self.Travelling)
        self.new_photo.save()
        self.new_photo.category.add(self.new_photo)

    def tearDown(self):

        Category.objects.all().delete()
        Photo.objects.all().delete()