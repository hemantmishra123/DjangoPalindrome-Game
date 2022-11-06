from rest_framework import serializers
from.models import Student,Record
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student 
        fields =['id','Name','Roll_No','Father','Mother','Math','English','Physics']


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record 
        fields =['Roll_No','Ds','Coa','Cn','Prog']
        





class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields= ['is_superuser','username','first_name','last_name','email']