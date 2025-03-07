from django.db.models.signals import post_save, post_delete, pre_save, pre_delete, post_migrate
from django.dispatch import receiver
from django.apps import apps

from .models import user, Student, StudentBin

#user db signals
@receiver(pre_delete, sender=user)
def UserPreDelete(sender, instance, **kwargs):
    print(f"{instance.user.username} yet to be deleted")

@receiver(post_save, sender=user)
def user_created(sender, instance, created, **kwargs):
        if created:
            print(f"New user - {instance.username} is created")
        else:
            print(f"{instance.username} has been updated")

@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        print(f"New Student - {instance.name} of {instance.grade} is created.")
    else:
        print(f"{instance.name} of {instance.grade} has been updated.")

@receiver(post_delete, sender=user)
def user_delete_signal(sender, instance, deleted, **kwargs):
    if deleted:
        print(f"{instance.username} has been deleted")
    else:
         pass

@receiver(post_delete, sender=Student)
def student_delete_signal(sender, instance, deleted, **kwargs):
    if deleted:
        print(f"{instance.name} of class {instance.grade} has been deleted")
    else:
        pass