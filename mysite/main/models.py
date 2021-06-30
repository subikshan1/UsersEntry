"""modules"""
from django.db import models


# Create your models here.

class Response(models.Model):
    """Response"""
    Response = models.CharField(max_length=100)
    Reason = models.CharField(max_length=100)


class Users(models.Model):
    """Users"""
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    Gender = models.CharField(max_length=20)
    National = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Pin = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=100)
    Salary = models.CharField(max_length=20)
    PanNum = models.CharField(max_length=30)
    Date = models.DateTimeField(auto_now_add=True)
    Responses = models.ForeignKey(Response, on_delete=models.CASCADE, blank=True, null=True)
