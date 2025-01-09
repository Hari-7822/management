from django.db import models
from django.conf import settings

class Chat(models.Model):
    # sender= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    # receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    sent_time = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"Message: {self.message} by {self.sender} to {self.receiver}"