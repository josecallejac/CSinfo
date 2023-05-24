from django.urls import path

from . import views

app_name="hltv"

urlpatterns = [
    path('', views.players, name='players'),
]


