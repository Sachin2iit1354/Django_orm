from rest_framework import serializers
from .models import user_schema,Log
from rest_framework.response import Response
from orm_test import models
from datetime import datetime
from datetime import time
# from .views import session,Customers
class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        # self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

class User(serializers.ModelSerializer):
    class Meta:
        model=user_schema
        fields='__all__'
    def create(self,validated_data):
        question=user_schema.objects.create(
            id=validated_data['id'],
            name=validated_data['name'],
            add=validated_data['add'],
            email=validated_data['email'],
            log_time=validated_data['log_time'],
            new_1=validated_data['new_1']
        )
        return question


    # def update(self, instance, validated_data):
    #     # return super().update(instance, validated_data)
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.add = validated_data.get('add', instance.add)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
    def delete(request,pk=None):
        user=user_schema.objects.get(pk=pk)
        user.delete()
        return Response("Given id has deleted!")
    
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()
    def create(self, validated_data):
        # return super().create(validated_data)
        question=[]
        question.append(validated_data['email'])
        question.append(validated_data['content'])
        return question
    
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'