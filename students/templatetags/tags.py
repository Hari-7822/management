from datetime import datetime

from django import template     

from ..models import user

register = template.Library() 
  
@register.simple_tag
def Count(): 
      return user.objects.count()

@register.simple_tag
def InTime(request):
      return datetime.now() - request.user.last_login