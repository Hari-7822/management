from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response

from .modelSerializer import UserSerializer, StudentSerializer

from ..models import user, Student


class UserProfileView(generics.RetrieveAPIView):
    queryset= user.objects.all()
    serializer_class= UserSerializer
    permission_classes=[permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes=[authentication.SessionAuthentication, authentication.TokenAuthentication]

    def get(self, req, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return Response(serializer.data)

    def post(self, serializer, *args, **kwargs):
        instance=serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def delete(self, req, *args, **kwargs):
        instance=self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StudentProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes=[authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser, permissions.IsAuthenticated]


    
    