from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# AbstractUser ile default olarak gelen field'lara, ek field'lar(portfolio,profile_pic gibi) ekleyebiliriz.
class User(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile.pics', blank = True)
    
