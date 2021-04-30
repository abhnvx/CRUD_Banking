from django.db import models

class newUser(models.Model):  
    userID = models.CharField(max_length=20)  
    userFirstName = models.CharField(max_length=100)  
    userLastName = models.CharField(max_length=100)
    userAge = models.CharField(max_length=20) 
    userGender = models.CharField(max_length=20)
    userDistrict = models.CharField(max_length=100)
    userState = models.CharField(max_length=100)
    userNationality = models.CharField(max_length=100)
    userAadhaar = models.CharField(max_length=100)
    userEmail = models.EmailField()  
    userContact = models.CharField(max_length=15)  
    userImage = models.ImageField(upload_to="images/")


    class Meta:  
        db_table = "userDetails"  


