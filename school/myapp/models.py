from django.db import models

# Create your models here.
class SchoolData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    StudentClass = models.CharField(max_length=100)   
    age = models.IntegerField()             


    # def __str__(self):
    #     return f"{self.name} - Class: {self.StudentClass}, Age: {self.age}"