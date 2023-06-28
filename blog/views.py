from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import PostForm

@login_required
def crear_post(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        autor = request.user
        post = Post(titulo=titulo, descripcion=descripcion, autor=autor)
        post.save()
    return render(request, 'pages/crear_post.html')
#Home del blog
class HomeListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'pages/blog.html'

    def get_queryset(self):
        return Post.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Detalle del Post
class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/detalle_post.html'

# Filtrado por Categoría
def category(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        return render(request, 'pages/category.html', {'category':category})    
    except:
        return render(request, 'pages/404.html')
    

    

def autor(request, autor_id):
 
        autor = get_object_or_404(get_user_model(), id=autor_id)
        
        return render(request, 'pages/autor.html', {'autor':autor})    
   

#crear post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('blog:blog') 


#Editar post
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('blog:update', args=[self.object.id]) + '?ok'

#Delete post
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog') 