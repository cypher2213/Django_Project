from django.db import models
from users.models import UserProfile
# Create your models here.



class Contact(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20,unique=True,blank=False,null=False)
    
    
    
    def __str__(self):
        return self.name