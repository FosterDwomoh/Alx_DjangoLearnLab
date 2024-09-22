from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
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