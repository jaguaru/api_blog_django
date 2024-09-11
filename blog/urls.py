from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()

router.register(r'posts', PostViewSet)  # Register PostViewSet
router.register(r'comments', CommentViewSet)  # Register CommentViewSet
#router.register('api/posts', PostViewSet, 'posts')  # Register PostViewSet
#router.register('api/comments', CommentViewSet, 'comments')  # Register CommentViewSet

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('api/blog', include(router.urls)),  # Include the generated URLs from the router
]

