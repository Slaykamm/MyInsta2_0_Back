from django.core.validators import FileExtensionValidator
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    avatar = models.ImageField(upload_to='avatar/', max_length = 100, blank=True)
    phone = models.CharField(unique=True, max_length=12)
    

    def __str__(self):
        return self.phone



class Video(models.Model):
    title = models.CharField(verbose_name='Name', unique=True, max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
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

class QuotationsCommentsArray(models.Model):
    baseComment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    quotedCommentID = models.IntegerField()
    

class PrivateRoom(models.Model):
    privateRoomMembers = models.ManyToManyField(User, blank=True)
    privateChatName = models.CharField(max_length=64, unique=True)
    lastOpenDate = models.DateTimeField(blank=True)

    # или сюда дату последнего открывания. Если дата раньше ласт логин то сообщения светим 

    def __str__(self):
        return self.privateChatName

class PrivateMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    privateRoom = models.ForeignKey(PrivateRoom, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    # подумать добавить сюда? или проще сделать. Е

    def __str__(self):
        return self.text