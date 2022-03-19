from dataclasses import field
from rest_framework import serializers
from storage.models import Video, Author, Comments, User, QuotationsCommentsArray, PrivateRoom, PrivateMessage





#--------------AUTHOR
class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'



# костылим 

class AuthorViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'




#--------------VIDEO
class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'



# костылим 

class VideoViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

#--------------Comments

class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'



# костылим 

class CommentsViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'


#--------------USER

class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



# костылим 

class UsersViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


#--------------QuotationsCommentsArray

class QuotationsCommentsArrayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationsCommentsArray
        fields = '__all__'



# костылим 

class QuotationsCommentsArrayViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuotationsCommentsArray
        fields = '__all__'


#----------------PrivateRooms

class PrivateRoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateRoom
        fields = '__all__'



# костылим 

class PrivateRoomViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivateRoom
        fields = '__all__'


#----------------PrivateMessages

class PrivateMessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = '__all__'



# костылим 

class PrivateMessageViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivateMessage
        fields = '__all__'
