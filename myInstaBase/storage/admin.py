from django.contrib import admin
from .models import Author, Video, Comments, QuotationsCommentsArray, PrivateMessage, PrivateRoom

# Register your models here.

admin.site.register(Author)
admin.site.register(Video)
admin.site.register(Comments)
admin.site.register(QuotationsCommentsArray)
admin.site.register(PrivateMessage)
admin.site.register(PrivateRoom)