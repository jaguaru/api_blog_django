from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# ViewSet for Post model
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Only authenticated users can create, update, and delete. Read-only access for others.
    permission_classes = [IsAuthenticatedOrReadOnly]

# ViewSet for Comment model
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # Only authenticated users can create, update, and delete. Read-only access for others.
    permission_classes = [IsAuthenticatedOrReadOnly]
