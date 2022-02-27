from django.core.validators import FileExtensionValidator
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    avatar = models.ImageField(upload_to='avatar/', max_length = 100, blank=True)
    phone = models.CharField(unique=True, max_length=12)
    

    def __str__(self):
        return self.phone



class Video(models.Model):
    title = models.CharField(verbose_name='Name', unique=True, max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    video = models.FileField(
        upload_to='video/',
        blank=True,
        #validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])]
    )

    image = models.ImageField(upload_to='preview/', blank=True)
    rating = models.IntegerField(default = 0)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='+')
    text = models.TextField()
    rating = models.IntegerField(default = 0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
