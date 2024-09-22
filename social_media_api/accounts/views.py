from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken  
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model


get_user_model().objects.create_user
serializers.CharField()

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