from django.contrib.auth.models import Group

from rest_framework import serializers

from students.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields='__all__' 
    
    def list(self, instance):
        pass
    
    def create(self, instance, *args, **kwargs):
        data=user()

        for field, val in instance.items():
            if field == 'password':
                data.set_password(val)
            else:
                setattr(data, field, val)
        data.save()
        return data

    def update(self, instance, field):
        instance=user()
        for i,j in field.items():
            if i == "password":
                instance.set_password(j)
            else:
                setattr(instance, i, j)
        instance.save()
        return instance
        
class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields=['url', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
