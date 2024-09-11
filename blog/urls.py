from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import PostViewSet, CommentViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()

router.register('api/blog/posts', PostViewSet, 'posts')  # Register PostViewSet
router.register('api/blog/comments', CommentViewSet, 'comments')  # Register CommentViewSet

# The API URLs are now determined automatically by the router
urlpatterns = router.urls

