from django.test import TestCase
from django.conf import settings
from .models import Person, Musician, Album, PersonOther, Student
# Create your tests here.

class AnimalTestCase(TestCase):
    def test_language_using_override(self):
        with translation.override('fr'):
            response = self.client.get('/')
        self.assertEqual(response.content, b"Bienvenue sur mon site.")

    def setUp(self):
        Person.objects.create(first_name="Sarker", last_name="Aninda", name="Aninda Sarker Rahul", shirt_size="S")
        Person.objects.create(first_name="Mamun", last_name="abdullah", name="Mamun Abdullah", shirt_size="L")

    def test_musician(self):
        Musician.objects.create(first_name="Anick",last_name="Hasan",instrument="bass")

