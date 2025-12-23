from django.db import models

# models here.
class UserData(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Mobiles(models.Model):
    mobile_name=models.CharField(max_length=50)
    specs=models.TextField()
    images=models.ImageField(upload_to="products/")

    def __str__(self):
        return self.mobile_name
    
