#see "https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication"

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


from . models import *
from . serializers import *


from rest_framework.views import APIView






#for making only accessesible with token; see "https://www.django-rest-framework.org/api-guide/authentication/"
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#add some c/p in setting.py too

class StudentAPI(APIView):

    #for making only accessesible with token; see "https://www.django-rest-framework.org/api-guide/authentication/"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #now we cannot access http://127.0.0.1:8000/stu/ like before it asked ""detail": "Authentication credentials were not provided.""
    #now we have to make a header Authorization and pass the token from admin panel


    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True) 

        #to see who is the current user
        print(request.user)

        return Response({"status":200, 'Payload' : serializer.data}) 

    def post(self, request):
        data = request.data
        serializer1 = StudentSerializer(data = request.data)

        if not serializer1.is_valid():
            print(serializer1.errors)
            return Response({"status":403, "errors":serializer1.errors, "message":"Somthing went wrong"})#"errors":serializer1.errors, if added here will show error on testing0

        serializer1.save()
        return Response({"status":200, "payload": serializer1.data, "message": "Your data is saved"})
    


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
        #this return 2 things
        token_obj , _ = Token.objects.get_or_create(user=user)

                                                                    #passing token_obj here as string
        return Response({"status":200, "payload": serializers.data, "token" : str(token_obj), "message": "Your data is saved"})


