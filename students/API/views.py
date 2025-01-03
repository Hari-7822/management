
from rest_framework import viewsets

from .modelSerializer import UserSerializer, StudentSerializer
from students.models import user, Student


class UserViewset(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class = UserSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

