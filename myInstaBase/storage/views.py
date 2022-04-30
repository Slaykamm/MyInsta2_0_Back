from venv import create
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from storage.serializer import VideoDetailSerializer, VideoViewSerializer, AuthorDetailSerializer, AuthorViewSerializer, CommentsDetailSerializer, CommentsViewSerializer, UsersDetailSerializer, UsersViewSerializer 
from storage.serializer import CommentsQuotationsDetailSerializer, CommentsQuotationsViewSerializer, PrivateMessageDetailSerializer, PrivateMessageViewSerializer, PrivateRoomDetailSerializer, PrivateRoomViewSerializer
from storage.models import Video, Author, Comments, User, CommentsQuotations, PrivateMessage, PrivateRoom
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse


# =============BLOCK FOR PASSWORD CHANGING
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import ChangePasswordSerializer

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##==================END==============

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


    def save(self, *args, **kwargs):
        # Сначала модель нужно сохранить, иначе изменять/обновлять будет нечего
        super(Author, self).save(*args, **kwargs)


    def post(self, request, *args, **Kwargs):
        
        if len(request.FILES) !=0:
            file = request.FILES['imagefile']
            print('request.FILES', request.FILES)
            print('file', file)

            idd = self.kwargs['pk']
            newImageToBase = Author.objects.get(id = idd)
            print("000", idd, newImageToBase.name)

            newImageToBase.avatar = request.FILES['imagefile']
            newImageToBase.save()

        return HttpResponse({'message':'Avatar added'}, status = 200)



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

    def post(self, request, *args, **Kwargs):
        
        if len(request.FILES) !=0:
            idd = self.kwargs['pk']
            newImageToBase = Video.objects.get(id = idd)


            if 'imagefile' in request.FILES:
                file = request.FILES['imagefile']
                newImageToBase.image = request.FILES['imagefile']
                newImageToBase.save()
            else:
                file = request.FILES['videofile']
                if file:
                    newImageToBase.video = request.FILES['videofile']
                    newImageToBase.save()

        return HttpResponse({'message':'Video Preview added'}, status = 200)

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


