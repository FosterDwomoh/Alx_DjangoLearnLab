from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'bio', 'profile_picture',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_date)
    user = CustomUser(**validated_date)
    user.set_password(validated_date['password'])
    user.save()
    Token.objects.create(user=user)
    return user