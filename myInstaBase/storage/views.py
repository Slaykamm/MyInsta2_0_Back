from venv import create
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from storage.serializer import VideoDetailSerializer, VideoViewSerializer, AuthorDetailSerializer, AuthorViewSerializer, CommentsDetailSerializer, CommentsViewSerializer, UsersDetailSerializer, UsersViewSerializer 
from storage.serializer import CommentsQuotationsDetailSerializer, CommentsQuotationsViewSerializer, PrivateMessageDetailSerializer, PrivateMessageViewSerializer, PrivateRoomDetailSerializer, PrivateRoomViewSerializer
from storage.models import Video, Author, Comments, User, CommentsQuotations, PrivateMessage, PrivateRoom
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
   #permission_classes=[IsAuthenticated]
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


##--------------------QUAOTATIONSSSSSSSSSSSS
class CommentsQuotationsViewSet(viewsets.ModelViewSet):
   #permission_classes=[IsAuthenticated]
   queryset = CommentsQuotations.objects.all()

   serializer_class = CommentsQuotationsViewSerializer

   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        baseComment =  self.request.query_params.get('baseComment', None)
        author = self.request.query_params.get('author', None)  
        text = self.request.query_params.get('text', None)  
        create_at = self.request.query_params.get('create_at', None)  


        if id:
            return CommentsQuotations.objects.filter(id=id)

        elif baseComment:
            return CommentsQuotations.objects.filter(baseComment=baseComment)

        elif author:
            return CommentsQuotations.objects.filter(author=author)

        elif text:
            return CommentsQuotations.objects.filter(text=text)

        elif create_at:
            return CommentsQuotations.objects.filter(create_at=create_at)

        else:
            return CommentsQuotations.objects.all()




# ------------------------------USERS----------------

class UsersCreateView(generics.CreateAPIView):
    serializer_class =  UsersDetailSerializer


class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsersDetailSerializer
    queryset = User.objects.all()    

class UsersViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UsersViewSerializer
   #permission_classes=[IsAuthenticated]

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




# ------------------------------Message Rooms--------- PrivateRoom-------

class PrivateRoomCreateView(generics.CreateAPIView):
    serializer_class =  PrivateRoomDetailSerializer


class PrivateRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateRoomDetailSerializer
    queryset = PrivateRoom.objects.all()    

class PrivateRoomViewSet(viewsets.ModelViewSet):
   queryset = PrivateRoom.objects.all()
   serializer_class = PrivateRoomViewSerializer
   #permission_classes=[IsAuthenticated]

   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        privateRoomMembers =  self.request.query_params.get('privateRoomMembers', None)
        privateChatName = self.request.query_params.get('privateChatName', None)  

        if id:
            return PrivateRoom.objects.filter(id=id)

        elif privateRoomMembers:
            return PrivateRoom.objects.filter(privateRoomMembers=privateRoomMembers)

        elif privateChatName:
            return PrivateRoom.objects.filter(privateChatName=privateChatName)

        else:
            return PrivateRoom.objects.all()

   def post(self, request, *args, **Kwargs):
        print('ya tutta request', request)
        id = self.kwargs['pk']
        print('ya tutta', id)
        if PrivateRoom.objects.filter(id=id).exists():
            return PrivateRoom.objects.filter(id=id)
        # else:
        #     PrivateRoom.objects.create(privateChatName=) 





# ------------------------------Message Rooms--------- PrivateMessage-------

class PrivateMessageCreateView(generics.CreateAPIView):
    serializer_class =  PrivateMessageDetailSerializer


class PrivateMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateMessageDetailSerializer
    queryset = PrivateMessage.objects.all()    

class PrivateMessageViewSet(viewsets.ModelViewSet):
   queryset = PrivateMessage.objects.all()
   serializer_class = PrivateMessageViewSerializer
   #permission_classes=[IsAuthenticated]

   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        author =  self.request.query_params.get('author', None)
        text = self.request.query_params.get('text', None)  
        privateRoom = self.request.query_params.get('privateRoom', None)  

        if id:
            return PrivateMessage.objects.filter(id=id)

        elif author:
            return PrivateMessage.objects.filter(author=author)

        elif text:
            return PrivateMessage.objects.filter(text=text)
        
        elif privateRoom:
            return PrivateMessage.objects.filter(privateRoom=privateRoom)

        else:
            return PrivateMessage.objects.all()