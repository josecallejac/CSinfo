from django.urls import path
from .views import category,crear_post, autor, HomeListView, PostDetailView

app_name="blog"

urlpatterns = [
    path('', HomeListView.as_view(), name='blog'),
    #Detalle post
    path('post/<pk>/', PostDetailView.as_view(), name='detalle_post'),
    path('crear_post', crear_post, name='crear_post'),
    
    path('category/<int:category_id>/', category, name='category'),
    path('autor/<int:autor_id>/', autor, name='autor'),
    
]