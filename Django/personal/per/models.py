from django.db import models

# Create your models here.

class Student(models.Model):

    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Age = models.IntegerField()
    Email = models.EmailField()




    def __str__(self):
        return self.Name





class Teacher(models.Model):
    Name = models.CharField(max_length=15)
    Phone = models.IntegerField()
    Age = models.IntegerField()
    Email = models.EmailField()
    Subject = models.CharField(max_length=20)



    def __str__(self):
        return self.name



class Staff(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Age = models.IntegerField()
    Email = models.EmailField()
    Experience = models.CharField(max_length=20)

    def __str__(self):
        return self.name



