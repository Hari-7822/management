from django.db.models.signals import post_save, post_delete, pre_save, pre_delete, post_migrate
from django.dispatch import receiver
from django.apps import apps

from .models import user, Student

#user db signals
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





# @receiver(post_save, sender=user)
# def created_signal(sender, instance, created, **kwargs):
#         if sender in apps.get_models():
#             if created:
#                 if apps.get_models() == "user": 
#                     print(f"New user - {instance.username} is created")
#                 elif apps.get_models() == "Student":
#                     print(f"New Student - {instance.name} of {instance.grade} is created.")
                     
#             else:
#                 if apps.get_models() == "user":
#                     print(f"{instance.username} has been updated")
#                 elif apps.get_models() == "Student":
#                     print(f"Student - {instance.name} of {instance.grade} has been updated.")