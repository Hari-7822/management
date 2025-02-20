from django.contrib.auth.models import Group

from rest_framework import serializers

from students.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields='__all__' 
    
    def list(self, instance):
        pass
    
    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data, *args, **kwargs):
        instance = self.Meta.model.objects.create(**validated_data)
        instance.set_password(validated_data['password']) if CheckPassword(validated_data['password']) else instance.save()
        instance.save()

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
    
    def get(self, req, *args, **kwargs):
        return self.retrieve(req, *args, **kwargs)
    
    def put(self, req, *args, **kwargs):
        return self.update(req, *args, **kwargs)
    
    def delete(self, req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)
    