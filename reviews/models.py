from django.db import models
from core.models import TimeStampsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Review(TimeStampsMixin,models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    
    
    def __str__(self):
        return self.name