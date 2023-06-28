from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save

from core import settings



class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    ROLES_CS = (
         ('R', 'Rifler'),
         ('A', 'Awper'),
         ('S', 'Support'),
         ('EF', 'Entry-Fragger'),
         ('F', 'Fragger'),
    )
    rol_cs = models.CharField(max_length=10, choices=ROLES_CS)
    bio = models.TextField(blank=True)

    


     

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Imagen de perfil')
    ROLES_CS = (
         ('R', 'Rifler'),
         ('A', 'Awper'),
         ('S', 'Support'),
         ('EF', 'Entry-Fragger'),
         ('F', 'Fragger'),
    )
    rol_cs = models.CharField(max_length=10, choices=ROLES_CS)
    


    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
    
   
    





""" @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
 """



