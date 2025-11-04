from django.db.models.signals import post_save, post_delete, pre_save, pre_delete, post_migrate
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.apps import apps

from .models import user

#user db signals

@receiver(user_logged_in)
def login():
    pass

@receiver(pre_delete, sender=user)
def UserPreDelete(sender, instance, **kwargs):
    print(f"{instance.user.username} yet to be deleted")

@receiver(post_save, sender=user)
def user_created(sender, instance, created, **kwargs):
        if created:
            print(f"New user - {instance.username} is created")
            try:
                instance.key= password(key, key.max_length)
                instance.save()
                print(f"Key for {instance.username} is generated")
            except Exception as E:
                 print(f"User {instance.username} has been created wihtout key is")
                 instance.save()
                 
        
        else:
            print(f"{instance.username} has been updated")

@receiver(post_delete, sender=user)
def user_delete_signal(sender, instance, deleted, **kwargs):
    if deleted:
        #use file writer to write logs
        print(f"{instance.username} has been deleted")
    else:
         pass

@receiver(post_save, sender=<sender>, dispatch_uid=<string>)
def method(sender, instance, **kwargs):
    last_field_change = FieldHistory.objects.filter(field_name=<your_field_which_you_want_to_check_for_change>,
                                          object_id=instance.id).last()
    if last_field_change:
         #do your thing