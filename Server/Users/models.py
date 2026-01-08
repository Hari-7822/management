from django.db import models
from django.contrib.auth.models import AbstractUser
from management.settings import MEDIA_ROOT, STATIC_ROOT, STATIC_URL, MEDIA_URL
from Server.utils.contrib.backends import PasswordGenerator
from datetime import datetime
import os

# def directory(instance,dir, file):
#     if not file:
#         file = 'default.jpg'
#     return os.path.join(f'{instance.user.id}/{dir}', file)


class user(AbstractUser):
    def directory(instance,dir, file):
        if not file:
            file = 'default.jpg'
        return os.path.join(f'{instance.user.id}/{dir}', file)
    
    def __str__(self):
        return f'{self.username}'
    def __repr__(self):    
        return f'User - {self.username}'

    Key= models.CharField(defualt=PasswordGenerator.generate_key(), max_length=4, blank=False)
    image=models.ImageField(upload_to=directory)
    

class UserSession(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)

    def time_spent(self):
        if self.logout_time:
            return self.logout_time - self.login_time
        return None
class preferences(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    theme=models.CharField(max_length=122)
    timezone=models.CharField(max_length=255)    

class Requests(models.Model):
    raised_by=models.ForeignKey(user, on_delete=models.CASCADE)
    content=models.TextField()
    approval=models.BooleanField(default=False, db_default=False)
    raised_date=models.DateTimeField(default=datetime.now(), db_default=datetime.now())
    # approved_by=models.ForeignKey(user, related_name= "name", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

# class UserBin(models.Model):
#     pass

class UserDeleteLog(user):
    pass 