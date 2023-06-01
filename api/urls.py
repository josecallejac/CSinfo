from django.urls import path, include
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)

urlpatterns = [
   # path('', views.getData),
    #path('add/', views.addPlayer),
    path('', include(router.urls)),
]
