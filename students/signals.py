from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import user

@receiver(post_save, sender=user)
def user_saved(sender, instance, created, **kwargs):
        if created:
            print(f"New user - {instance.username} is created")
        else:
            print(f"{instance.username} has been updated")