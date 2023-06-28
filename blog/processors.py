""" from .models import About,Category, Post

# ABOUT
def ctx_dic_about(request):
	ctx_about = {}
	ctx_about['ABOUT'] = About.objects.latest('created')
	return ctx_about

# CATEGORIAS
def ctx_dic_category(request):
	ctx_category = {}
	ctx_category['categories'] = Category.objects.filter(active=True)
	return ctx_category

 """
 