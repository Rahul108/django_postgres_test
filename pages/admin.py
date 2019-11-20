from django.contrib import admin
from .models import Person, Musician, Album, PersonOther, Student
# Register your models here.
admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(PersonOther)
admin.site.register(Student)