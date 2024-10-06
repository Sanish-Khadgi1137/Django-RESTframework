#seralizer convert queiry set to JSON format; hyper, normal, model serializer(here)

from rest_framework import serializers
from .models import * # "*" = all

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        
        #fields = ["name", "age"] #only serialize "name" and "age"
        #exclude = ['id',] #serialize all except "id"
        fields = '__all__' #serialize all

    #we do not write model/DB logic in view.py in DRF, like this
    def validate(self, data):

        if data["name"]: #this validation error is shown in API testing; if both validation caught error, because this is in first position
         for n in data['name']:
             if n.isdigit():
                 raise serializers.ValidationError({'error': "name must not contain numeric"})


        if data['age']<18:
            raise serializers.ValidationError({"error":"age can not be less than 18"})
        
     
                
        return data
    


 #nested serializer   
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        #fields = '__all__'
        fields = ["category_name"] #this way we will not get id of category in GET

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()#for foriegn key
    class Meta:
        model = Book
        fields = "__all__"
        #depth = 1 #depth doesnot work here; so work on fileds = in Meta of Category


