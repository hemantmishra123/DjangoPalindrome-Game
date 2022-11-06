from django.db import models

# Create your models here.

class Student(models.Model):
    Name    =       models.CharField(max_length=50)
    #Roll No of the Student is Primary key unique. #Roll_No gives the unique data of the cell for the student.
    Roll_No =       models.IntegerField(max_length=10)
    Father  =       models.CharField(max_length=50)
    Mother  =       models.CharField(max_length=50)
    Math    =       models.IntegerField(max_length=50)
    English =       models.IntegerField(max_length=50)
    Physics =       models.IntegerField(max_length=50)

    def __str__(self):
        return self.Name 

#class ListView and Return Average da
class Record(models.Model):
    Roll_No = models.IntegerField(max_length=10)
    Ds    =     models.IntegerField(max_length=10)
    Coa       = models.IntegerField(max_length=10)
    Cn  =    models.IntegerField(max_length=10)
    Prog =   models.IntegerField(max_length=10)
    



     
