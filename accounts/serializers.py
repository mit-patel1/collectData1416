from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from home.models import UserData



class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(max_length=100)

    def validate(self, data):

        if User.objects.filter(username=data['username'].lower()).exists():
            raise serializers.ValidationError('Username is exist.')
        
        return data
    
    def create(self, validated_data):
        print('validated_data', validated_data)
        user = User(
            first_name = validated_data['first_name'],
            email=validated_data['email'].lower(),
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=100)

    def validate(self, data):

        if not User.objects.filter(username=data['username'].lower()).exists():
            raise serializers.ValidationError('Username is not exist.')
        
        return data
    
    def get_jwt_token(self, data):
        user = authenticate(username=data['username'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Credential is not match.')

        refresh = RefreshToken.for_user(user)

        return refresh
    
