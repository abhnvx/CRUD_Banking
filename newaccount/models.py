from django.db import models
from django import forms


GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ]

class newUser(models.Model):  
    userID = models.CharField(max_length=20)  
    userFirstName = models.CharField(max_length=100)  
    userLastName = models.CharField(max_length=100)
    userAge = models.CharField(max_length=20) 
    userGender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    userDistrict = models.CharField(max_length=100)
    userState = models.CharField(max_length=100)
    userNationality = models.CharField(max_length=100)
    userAadhaar = models.CharField(max_length=100)
    userEmail = models.EmailField()  
    userContact = models.IntegerField(max_length=15)
    userStartingBalance = models.FloatField()  
    userImage = models.ImageField(upload_to="images/")
    userAadhaarImage = models.ImageField(upload_to="aadhaar/")
    userRemarks = models.CharField(max_length=260)

    tc = models.BooleanField(default=False)


    class Meta:  
        db_table = "userDetails"  


