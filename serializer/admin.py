from django.contrib import admin
from .models import Snippet, Member, Book
# Register your models here.
admin.site.register((Snippet))
admin.site.register((Member))
admin.site.register((Book))