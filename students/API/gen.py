from rest_framework import generics
from ..models import user

class UserProfileView(generics.RetrieveAPIView):
    queryset= user.objects.all()