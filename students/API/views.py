from django.contrib.auth.models import Group

from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.generics import CreateAPIView
from rest_framework import status

from .modelSerializer import UserSerializer, StudentSerializer, GroupSerializers
from students.models import user, Student, UserBin, StudentBin

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
            user.objects.update_or_create()
        return Response({f'User Created'})
    
    @action(detail=True, methods=["DELETE"])
    def delete(self, request, pk):
        if request.method=="DELETE":
            user.objects.delete(pk=pk)
        return Response({f'User deleted'})
    
    @action(detail=True, methods=["PATCH"])
    def patch(self, req, pk):
        if req.method == "PATCH":
            user.objects.update(pk=pk)

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes=[permissions.IsAuthenticated]

class UserRegistrationViewset(CreateAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]


class StudentRegistrationViewSet(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]

class UserCreateRetrieveUpdateDestroy(generics.DestroyAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]
    lookup_field = 'pk'
    
    def perform_destroy(self, instance) :
        super().perform_destroy(instance)
        return Response(f"{instance.user.username} has been deleted")


class StudentCreateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]

