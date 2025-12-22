from django.db import models
from core.models import TimeStampsMixin

# Create your models here.


class Product(TimeStampsMixin, models.Model):
    avatar = models.ImageField(upload_to='products/images', blank=True,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    def __str__(self):
        return self.name