from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path,include
router = routers.DefaultRouter()

urlpatterns=[
     path('',include(router.urls)),
]