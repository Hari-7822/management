from django.db import models
from django.contrib.auth.models import AbstractUser
from management.settings import MEDIA_ROOT, STATIC_ROOT, STATIC_URL, MEDIA_URL

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

    image=models.ImageField(upload_to=directory)
    

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

class UserBin(user):
    pass



class UserDeleteLog(user):
    pass