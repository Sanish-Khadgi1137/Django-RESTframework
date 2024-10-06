
from rest_framework import serializers
from .models import * # "*" = all

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        
        fields = '__all__' 

    def validate(self, data):

        if data["name"]:
         for n in data['name']:
             if n.isdigit():
                 raise serializers.ValidationError({'error': "name must not contain numeric"})


        if data['age']<18:
            raise serializers.ValidationError({"error":"age can not be less than 18"})
        
        return data
    
#for manual token generator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ["username", "password" ]

    #for hasing password, to resolve this in admin panel (Invalid password format or unknown hashing algorithm.); now see password instead of 123 there is hast code
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data["password"])
        user.save()

        return user

        