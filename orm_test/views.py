from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from django.http import HttpResponse
# from .models import Question
from django.template import loader
from rest_framework import status
from . import serializers,models
from .models import user_schema
from .serializers import User,CommentSerializer,comment
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import action
# Create your views here.


class Userviewset(viewsets.ModelViewSet):
    serializer_class=User
    queryset=user_schema.objects.all()
    # @action(detail=False, methods=['put'])
    def put(request, pk):
        user = user_schema.objects.get(pk=pk)
        serializer = User(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # @action(detail=False, methods=['delete'])
    def delete(self,request):
        user=user_schema.objects.all()
        # serializer=User(instance=user,data=request.data)
        user.delete()
        return Response("Deleted")
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    
class ListViewSet(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset=user_schema.objects.all()
    def detail(request):
        serializer=CommentSerializer(comment)
        return Response(serializer.data)