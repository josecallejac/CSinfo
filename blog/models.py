from django.db import models

from ckeditor.fields import RichTextField


from django.conf import settings



# Create your models here.

class Category (models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['name']

	def __str__(self):
		return self.name
	
# MODELO DE ETIQUETAS
	
class Tag (models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Etiqueta'
		verbose_name_plural = 'Etiquetas'
		ordering = ['name']

	def __str__(self):
		return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    excerpt = models.TextField(verbose_name='Bajada')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name='Imagen')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    #CAMPOS CON RELACIONES
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoría')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')
    autor =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name='get_posts', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')


class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

        def __str__(self):
            return self.title
	
class About(models.Model):
	description = models.CharField(max_length=350, verbose_name='Descripción')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Acerca de'
		verbose_name_plural = 'Acerca de Nosotros'
		ordering = ['-created']

	def __str__(self):
		return self.description