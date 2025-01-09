from django import template     
from ..models import user 

register = template.Library() 
  
@register.simple_tag
def Count(): 
      return user.objects.count()