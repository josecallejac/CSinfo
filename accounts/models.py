from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nacionalidad = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField()

    def __str__(self):
            return self.bio