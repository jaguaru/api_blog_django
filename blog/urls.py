from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import PostViewSet, CommentViewSet, UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Create a router and register our viewsets with it
router = DefaultRouter()

router.register('blog/posts', PostViewSet, 'posts')  # Register PostViewSet
router.register('blog/comments', CommentViewSet, 'comments')  # Register CommentViewSet

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/register/', UserRegisterView.as_view(), name='register'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

