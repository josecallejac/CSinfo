from django.urls import path
from . import views

app_name="csinfo"

urlpatterns = [
    path('major', views.major, name='major'),
    
]
