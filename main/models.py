from django.db import models
from users.models import CustomUser
# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=70, decimal_places=2,)
    image=models.ImageField(upload_to='images')
    number=models.IntegerField()
    description=models.TextField(null=True)                                               






    def __str__(self):
        return self.name