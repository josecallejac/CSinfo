
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from .models import UserProfile

@receiver(post_save, sender=UserProfile)
def assign_role(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            group, _ = Group.objects.get_or_create(name='Administrador')
            instance.groups.add(group)
        elif instance.role == 'normal':
            group, _ = Group.objects.get_or_create(name='Usuarios')
            instance.groups.add(group)

@receiver(user_signed_up)
def assign_permissions(sender, user, request, **kwargs):
    if user.role == 'admin':
        admin_content_type = ContentType.objects.get_for_model(UserProfile)
        admin_permissions = admin_permissions = (
    ('can_view_admin_dashboard', 'Puede ver el panel de administración'),
)  
        for codename, desc in admin_permissions:
            permission, created = Permission.objects.get_or_create(
                codename=codename,
                content_type=admin_content_type,
                defaults={'name': desc}
            )
            user.user_permissions.add(permission)
