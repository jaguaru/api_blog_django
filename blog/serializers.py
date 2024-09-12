from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment


# Serializer for UserRegister model
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user with validated data
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        # Set the password correctly using set_password
        user.set_password(validated_data['password'])
        user.save()
        return user

# Serializer for Comment model
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']
        read_only_field = ['created_at', 'updated_at']

# Serializer for Post model
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'comments']
        read_only_field = ['created_at', 'updated_at']
