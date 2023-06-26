from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from core import settings



class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    ROLE_CHOICES = (
         ('admin', 'Administrador'),
         ('is_user', 'Usuarios'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    nacionalidad = models.CharField(max_length=100)
    is_user = models.BooleanField('¿Desea crear cuenta cliente?', default=False)
    ROLE_CHOICES = (
         ('admin', 'Administrador'),
         ('is_user', 'Usuarios'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
            return self.user.username
    
   
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()





"""  class User(AbstractUser):
    is_user = models.BooleanField('¿Desea crear cuenta cliente?', default=False)
    nacionalidad = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField()

    def __str__(self):
            return self.username """
