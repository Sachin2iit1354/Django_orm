from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
router = routers.DefaultRouter()
router.register('user', views.Userviewset,basename='user')
router.register('detail',views.ListViewSet,basename='detail')
# router.register('hello_world',views.hello_world)
urlpatterns = [
    # path('hello-world',views.hello_world),
    path('',include(router.urls)),
    # path('detail/<int:pk>',views.fun)
]