from django.contrib import admin
from .models import Author, Video, Comments

# Register your models here.

admin.site.register(Author)
admin.site.register(Video)
admin.site.register(Comments)
