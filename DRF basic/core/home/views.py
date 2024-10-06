#https://www.django-rest-framework.org
#pip install djangorestframework
#we need to activate venv even to run the server
from django.shortcuts import render


# def home(request):
#     return render(request, "home.html")

#using apiview
from rest_framework.decorators import api_view
from rest_framework.response import Response

# #@api_view()#this is accepting all GET, POST method etc
# @api_view(["POST"])# this accept only POST method, if we send GET method it will give error in api testing
# def home(request):
#     return Response({"status":200, 'message' : "hello from django rest framework"})

# #we need to migrate to run this for session table

from . models import *
from . serializers import *

@api_view(["GET"])
def home(request):

    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True) #serializing data(student_objs) get from "just above line" and many=True because we process large bulk of data

#sending JSON data through API
    return Response({"status":200, 'Payload' : serializer.data}) # "serializer.data" to access above serialized data

#for getting data from frontend
@api_view(["POST"])
def post_student(request):
    data = request.data #we take data from frontend by "request.data"
    #print(data)
    #return Response({"status" : 200, "payload": data, "message" : "you sent"})


    serializer1 = StudentSerializer(data = request.data)#data = request.data = we get from user

    if not serializer1.is_valid():
        print(serializer1.errors)
        return Response({"status":403, "errors":serializer1.errors, "message":"Somthing went wrong"})#"errors":serializer1.errors, if added here will show error on testing
    
    serializer1.save()
    return Response({"status":200, "payload": serializer1.data, "message": "Your data is saved"})

#PUT method, we needed to give all the filed exept "id" to update
@api_view(["PUT"])# for PUT we need to provide full package no partial data
def update_student(request, id): #we used "id" to say DRF which object to update and we must set "fileds = __all__" in serializers.py to used id too
        
    try:

        student_obj2 = Student.objects.get(id = id) # "id" is like a slug

        serializer1 = StudentSerializer(student_obj2, data = request.data)#we passed fetched object(student_obj2) to this line and #data = request.data = we get from user

        if not serializer1.is_valid():
            print(serializer1.errors)
            return Response({"status":403, "errors":serializer1.errors, "message":"Somthing went wrong hhhhhhhhhhhhhhhh!"})
        
        serializer1.save()
        return Response({"status":200, "payload": serializer1.data, "message": "Your data is saved"})
    
    except Exception as e:
        return Response({"status": 403, "message": "Invalid id ZZZZzzzzzZZZZZZZZzzzzzz!"})
    
#PATCH update can update fields partially i.e. we do not need to type all info to update eg "age"   unlike in PUT 
@api_view(["PATCH"])
def patchupdate_student(request, id):
        
    try:
         # Fetch the student object by ID
        student_obj2 = Student.objects.get(id = id) # id is a slug

       # Apply partial update
        serializer1 = StudentSerializer(student_obj2, data = request.data, partial=True )#added partial = True

        # If the serializer is not valid, return errors
        if not serializer1.is_valid():
            print(serializer1.errors)
            return Response({"status":403, "errors":serializer1.errors, "message":"Somthing went wrong"})

        # If the serializer is valid
        serializer1.save()# Save the updated student data
        return Response({"status":200, "payload": serializer1.data, "message": "Your data is saved"})
    
    except Exception as e:
        return Response({"status": 403, "message": "invalid id"})
    
#delete
@api_view(["DELETE"])
def delete_student(request, id):
    try:
        # id = request.GET.get('id') #for /?id=15
        student_object = Student.objects.get(id=id)
        student_object.delete()

        return Response({"status": 200, "message": "deleted"})

    except Exception as e:
        return Response({"status": 403, "message": "invalid id"})
    

#for Nested serializer
@api_view(['GET'])
def get_book(request):
    book_object = Book.objects.all()
    serializer = BookSerializer(book_object, many =True)
    return Response({"status":200, 'Payload' : serializer.data}) 
    


#for API view method   333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
from rest_framework.views import APIView

class StudentAPI(APIView):

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

    def patch(self, request):
        try:
            student_obj2 = Student.objects.get(id = request.data["id"])

            serializer1 = StudentSerializer(student_obj2, data = request.data, partial=True )


            if not serializer1.is_valid():
                print(serializer1.errors)
                return Response({"status":403, "errors":serializer1.errors, "message":"Somthing went wrong"})

            
            serializer1.save()
            return Response({"status":200, "payload": serializer1.data, "message": "Your data is patch updated"})

        except Exception as e:
            print(e)
            return Response({"status": 403, "message": "invalid id"})
        
    def delete(self, request):
        try:
            id = request.GET.get('id')#use "stu/?id=10"

            student_object = Student.objects.get(id=id)
            student_object.delete()

            return Response({"status": 200, "message": "deleted"})

        except Exception as e:
            return Response({"status": 403, "message": "invalid id"})


