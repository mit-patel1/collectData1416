from django.contrib.auth.models import User
from rest_framework import serializers
from home.models import UserData


class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserData
        # frelds = '__all__'
        exclude = ['created_at', 'updated_at']

    # def validate(self, data):

    #     if User.objects.filter(username=data['username'].lower()).exists():
    #         raise serializers.ValidationError('Username is exist.')
        
    #     return data
    
# class UserDataSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     number = serializers.IntegerField(required=True)
#     email = serializers.EmailField(required=False)
#     address = serializers.CharField()
#     description = serializers.CharField(max_length=1000)
#     dob = serializers.DateField()