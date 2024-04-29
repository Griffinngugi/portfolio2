from django.db import models

# Create your models here.



class students(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=False, null=False)
    subject = models.CharField(max_length=15, blank=False, null=False)
    image = models.ImageField(upload_to='uploads/images', default="logo jpeg")

    def __str__(self):
        return self.name

    class teachers(models.Model):
        name = models.CharField(max_length=20,blank=False,null=False)
        email = models.EmailField()
        age = models.IntegerField()
        gender = models.CharField(max_length=10, blank=False, null=False)
        subject = models.CharField(max_length=15, blank=False, null=False)
        image = models.ImageField(upload_to='uploads/images', default="animation jpeg")

    def __str__(self):
        return self.name


class Staff(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Age = models.IntegerField()
    Email = models.EmailField()
    work = models.CharField(max_length=20,blank=False,null=False)
    Experience = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/images',default="animation jpeg")

    def __str__(self):
        return self.name




