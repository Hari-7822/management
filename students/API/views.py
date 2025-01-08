from django.contrib.auth.models import Group

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin

from .modelSerializer import UserSerializer, StudentSerializer, GroupSerializers
from students.models import user, Student

@api_view(["GET"])
def api_root(req, format=None):
    return Response({
        'users': reverse('Api_users', request=req, format=format),
        'Student': reverse('Api_students', request=req, format=format),
        'Groups': reverse("Api_groups", request=req, format=format)
    })

class UserViewset(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    @action(detail=True, methods=['POST', 'PUT'])
    def CreateOrUpdate(self, request, pk=None, *args):
        if request.methods=="POST":
            user.objects.create()
        return Response({f'User Created'})
    
    @action(detail=True, methods=["DELETE"])
    def delete(self, request, pk):
        user.objects.delete(pk=pk)
        return Response({f'User, deleted'})

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes=[permissions.IsAuthenticated]




