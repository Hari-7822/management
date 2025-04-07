from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.generics import CreateAPIView

from .modelSerializer import UserSerializer, UserRegistrationSerializer, StudentSerializer, GroupSerializers
from students.models import user, Student, StudentBin
from Users.models import UserBin

from datetime import datetime

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

    def get_obj(slef, pk):
        try:
            return user.objects.get(pk=pk)
        except:
            return False

    @action(detail=True, methods=['POST', 'PATCH'])
    def CreateOrUpdate(self, request, pk=None, *args):
        if request.method=="POST":
            user.objects.update_or_create()
            return Response({f'User Created'})
        elif request.method=="PATCH":
            try:
                # target=user.objects.get(id=id)
                obj=self.serializer_class
                obj.update(pk=pk, data=request.DATA)
                if obj.is_valid():
                    obj.save()
                    return JsonResponse(code=201, data=obj.data)
                return JsonResponse(code=400, data="wrong parameters")
            except:
                return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['POST', 'PUT'])
    def create(self, request, pk=None, *args):
        if request.method=="POST":
            user.objects.create()
            
    @action(detail=True, methods=["DELETE"])
    def delete(self, request, pk):
        if request.method=="DELETE":
            user.objects.delete(pk=pk)
        return Response({f'User deleted'})
    

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(Created_By=self.request.user, Created_At= datetime.now())
        return super().perform_create(serializer)


class GroupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes=[permissions.IsAuthenticated]

class UserRegistrationViewset(CreateAPIView):
    queryset=user.objects.all()
    serializer_class=UserRegistrationSerializer
    permission_classes=[permissions.IsAuthenticated, permissions.IsAdminUser]


class StudentRegistrationViewSet(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(Created_By=self.request.user, Created_At= datetime.now())
        return super().perform_create(serializer)

class UserDestroy(generics.DestroyAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]
    lookup_field = 'pk'
    
    def perform_destroy(self, instance) :
        UserBin.objects.create(**{field.name: getattr(instance, field.name) for field in instance._meta.fields})
        super().perform_destroy(instance)
        return Response(f"{instance.user.username} has been deleted")



class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]
    lookup_field='roll_number'

class UserCreateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
