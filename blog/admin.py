from django.contrib import admin
from .models import Post, Tag, Category, About
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('title', 'category', 'published', 'autor', 'created', 'post_tags')
	ordering = ('autor', '-created')
	search_fields = ('title', 'content', 'autor__username', 'category__name')
	list_filter = ('autor', 'category', 'tags')

	def post_tags(self, obj):
		return ' - '.join([t.name for t in obj.tags.all().order_by('name')])

	post_tags.short_description = 'Etiquetas'

admin.site.register(Post, PostAdmin) 

class TagAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('name', 'active', 'created')

admin.site.register(Tag, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Category, CategoryAdmin)

# ABOUT
class AboutAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('description', 'created')

admin.site.register(About, AboutAdmin)
