from rest_framework import serializers
from .models import Post, Comment


# Serializador para el modelo Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_field = ['created_at', 'updated_at']

# Serializador para el modelo Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at', 'updated_at']
        read_only_field = ['created_at', 'updated_at']
