from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    speed = models.IntegerField()
    year = models.IntegerField()


    def __str__(self):
        return f"{self.car_name} {self.model} ({self.year})"