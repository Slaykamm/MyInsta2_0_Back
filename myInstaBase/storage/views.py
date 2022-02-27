from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from storage.serializer import VideoDetailSerializer, VideoViewSerializer, AuthorDetailSerializer, AuthorViewSerializer, CommentsDetailSerializer, CommentsViewSerializer, UsersDetailSerializer, UsersViewSerializer
from storage.models import Video, Author, Comments, User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#Author

##ниже 2 класса аокнментил. тестю.
class AuthorCreateView(generics.CreateAPIView):
    serializer_class =  AuthorDetailSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Video.objects.all()    


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()

    serializer_class = AuthorViewSerializer

    def get_queryset(self, **kwargs):
            id =  self.request.query_params.get('id', None)
            name = self.request.query_params.get('name', None)  
            email =  self.request.query_params.get('email', None)

            if id:
                return Author.objects.filter(id=id)
            elif name:
                return Author.objects.filter(name=name)
            elif email:
                return Author.objects.filter(email=email)
            else:
                return Author.objects.all()

#Video
class VideoCreateView(generics.CreateAPIView):
    serializer_class =  VideoDetailSerializer


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoDetailSerializer
    queryset = Video.objects.all()    

class VideoViewSet(viewsets.ModelViewSet):

    queryset = Video.objects.all()
    serializer_class = VideoViewSerializer

    def get_queryset(self, **kwargs):
            id =  self.request.query_params.get('id', None)
            title = self.request.query_params.get('title', None)  
            author =  self.request.query_params.get('author', None)
            rating = self.request.query_params.get('rating', None)  
            create_at = self.request.query_params.get('create_at', None)  


            if id:
                return Video.objects.filter(id=id)
            elif title:
                return Video.objects.filter(title=title)
            elif author:
                return Video.objects.filter(author=author)
            elif rating:
                return Video.objects.filter(rating=rating)
            elif create_at:
                return Video.objects.filter(create_at=create_at)

            else:
                return Video.objects.all()



#Comments

class CommentsCreateView(generics.CreateAPIView):
    serializer_class =  CommentsDetailSerializer


class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsDetailSerializer
    queryset = Comments.objects.all()    


class CommentsViewSet(viewsets.ModelViewSet):
   permission_classes=[IsAuthenticated]
   queryset = Comments.objects.all()

   serializer_class = CommentsViewSerializer

   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        author =  self.request.query_params.get('author', None)
        video = self.request.query_params.get('video', None)  
        rating = self.request.query_params.get('rating', None)  
        create_at = self.request.query_params.get('create_at', None)  


        if id:
            return Comments.objects.filter(id=id)

        elif author:
            return Comments.objects.filter(author=author)

        elif video:
            return Comments.objects.filter(video=video)

        elif rating:
            return Comments.objects.filter(rating=rating)

        elif create_at:
            return Comments.objects.filter(create_at=create_at)
            
        else:
            return Comments.objects.all()

# ------------------------------USERS----------------

class UsersCreateView(generics.CreateAPIView):
    serializer_class =  UsersDetailSerializer


class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsersDetailSerializer
    queryset = User.objects.all()    

class UsersViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UsersViewSerializer


   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        password =  self.request.query_params.get('password', None)
        username = self.request.query_params.get('username', None)  
        first_name = self.request.query_params.get('first_name', None)  
        last_name = self.request.query_params.get('last_name', None)  
        email = self.request.query_params.get('email', None)  
        date_joined = self.request.query_params.get('date_joined', None)  
        groups = self.request.query_params.get('groups', None)  

        if id:
            return User.objects.filter(id=id)

        elif password:
            return User.objects.filter(password=password)

        elif username:
            return User.objects.filter(username=username)

        elif first_name:
            return User.objects.filter(first_name=first_name)

        elif last_name:
            return User.objects.filter(last_name=last_name)

        elif email:
            return User.objects.filter(email=email)

        elif date_joined:
            return User.objects.filter(date_joined=date_joined)

        elif groups:
            return User.objects.filter(groups=groups)

        else:
            return User.objects.all()