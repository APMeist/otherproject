from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import Teacher, Student

@receiver(post_save, sender=Teacher)
def teacher_permissions(sender, instance, created, **kwargs):
    if created:
        try:
            Permission.objects.get(codename='change_mark')
            instance.user.user_permissions.add(Permission.objects.get(codename='change_mark'))
        except Permission.DoesNotExist:
            print('Permission "change_mark" not found"')

@receiver(post_save, sender=Student)
def student_permissions(sender, instance, created, **kwargs):
    if created:
        try:
            permissions = Permission.objects.get(codename='change_fileanswer')
            instance.user.user_permissions.add(permissions)
        except Permission.DoesNotExist:
            print('Permission "change_fileanswer" not found')



