from django.urls import path 
from .views import RegisterView, LoginView, UserProfileView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import UserViewSet
from .views import follow_user, unfollow_user 

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
    path('follow/<int:user_id/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id/', unfollowfollow_user, name='unfollow'),
]