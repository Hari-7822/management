from datetime import datetime
from django import template     

from Users.models import user

register = template.Library() 
  
@register.simple_tag
def Count(): 
      return user.objects.count()

@register.simple_tag
def InTime(request):
      return datetime.now() - request.user.last_login

@register.filter
def get_fields(model):
      try:
            return [field.name for field in model._meta.fields]
      except:
            []
