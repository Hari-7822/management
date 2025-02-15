from django.contrib.auth.models import Group

from rest_framework import serializers

from students.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields='__all__' 
    
    def list(self, instance):
        pass
    
    def create(self, validated_data):
        print("Validated Data:", validated_data)  # Debug statement

        password = validated_data.pop('password', None)
        print("Password:", password)  # Debug statement
        
        instance = self.Meta.model(**validated_data)
        print("Instance:", instance)  # Debug statement
        
        if password is not None:
            instance.set_password(password)  # Use set_password() for the user password
        
        instance.save()
        
        # Set groups after saving the instance
        groups_data = self.initial_data.get('groups')
        print("Groups Data:", groups_data)  # Debug statement
        
        if groups_data:
            instance.groups.set(groups_data)
        
        return instance


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
