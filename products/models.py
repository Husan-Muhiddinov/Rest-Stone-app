from django.db import models
from main.models import Product
from users.models import CustomUser

# Create your models here.




class CheckOut(models.Model):
    
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    ref = models.CharField(max_length=50, blank=True, null=True)
    name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    payment=models.CharField(max_length=50)
    number=models.CharField(max_length=17)
    email=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    country=models.CharField(max_length=25)
    status = models.CharField(max_length=100, null=True, blank=True)
    cost = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    count=models.IntegerField(default=0)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    sav=models.ForeignKey(CheckOut,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.product)
 

    