from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken  
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.decorators import action 
from .models import CustomUser
from .serializer import UserSerializer


get_user_model().objects.create_user
serializers.CharField()
generics.GenericsAPIView

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **extra_kwargs):
        response = super(LoginView, self).post(request, *args, **extra_kwargs)
        token = Token.objects.get(user=response.data['user'])
        return Response({'token': token.key, 'user_id': token.user_id})

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='follow')
    def follow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following.add(user_to_follow)
        return Response({'status': 'followed'})
    
     @action(detail=True, methods=['post'], url_path='unfollow')
    def unfollowfollow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following.add(user_to_unfollow)
        return Response({'status': 'unfollowed'})