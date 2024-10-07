from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def Get_Message(request):
    return Response( {'message': "Hello from Django! via API hurray!" } )
