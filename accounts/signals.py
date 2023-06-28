from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserProfile

@receiver(post_save, sender=UserProfile)
def add_user_to_users_group(sender, instance, created, **kwargs):
    if created:
        try:
            users = Group.objects.get(name='Usuarios')
        except Group.DoesNotExist:
            users = Group.objects.create(name='Usuarios')
            users = Group.objects.create(name='Administrador')
        instance.user.groups.add(users)