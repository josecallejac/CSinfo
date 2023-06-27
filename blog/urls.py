from django.urls import path
from .views import category, autor, HomeListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name="blog"

urlpatterns = [
    path('', HomeListView.as_view(), name='blog'),
    #Detalle post
    path('post/<pk>/', PostDetailView.as_view(), name='detalle_post'),
    #crear post
    path('create/', PostCreateView.as_view() , name='create'),
    #editar post
    path('update/<int:pk>', PostUpdateView.as_view() , name='update'),
    #eliminar post
    path('delete/<int:pk>', PostDeleteView.as_view() , name='delete'),
    
    
    path('category/<int:category_id>/', category, name='category'),
    path('autor/<int:autor_id>/', autor, name='autor'),
    
]