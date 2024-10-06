#https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#requirements
#was installed "pip install djangorestframework-simplejwt"

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


from . models import *
from . serializers import *

from rest_framework.views import APIView

#for permission based access of StudentAPI
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentAPI(APIView):

    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]#for permission based access of StudentAPI


    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True) 
        return Response({"status":200, 'Payload' : serializer.data}) 

    def post(self, request):
        data = request.data
        serializer1 = StudentSerializer(data = request.data)

        if not serializer1.is_valid():
            print(serializer1.errors)
            return Response({"status":403, "errors":serializer1.errors, "message":"Somthing went wrong"})#"errors":serializer1.errors, if added here will show error on testing0

        serializer1.save()
        return Response({"status":200, "payload": serializer1.data, "message": "Your data is saved"})


#use admin username and passowrd both="core"  POST method to generate token "http://127.0.0.1:8000/api/token/"
#we need to add generated access token to Auth>Bearer Token to get access to "http://127.0.0.1:8000/stu"

#for Creating token manually
from rest_framework_simplejwt.tokens import RefreshToken

#for manual token generator; See "https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication"
from rest_framework.authtoken.models import Token


class RegisterUser(APIView):
    def post(self, request):
        serializers = UserSerializer(data = request.data)

        if not serializers.is_valid():
            return Response({"status":403, "errors":serializers.errors, "message":"Somthing went wrong"})

        serializers.save()

        #generating token
        user = User.objects.get(username = serializers.data["username"])

        #for manual JWS token generation
        refresh = RefreshToken.for_user(user)
        

                                                                   
        return Response({"status":200,
                          "payload": serializers.data, 

                          'refresh': str(refresh),                                       #these 2 lines for JWT manual TG 
                            'access': str(refresh.access_token), 
        
                            "message": "Your data is saved"})

    