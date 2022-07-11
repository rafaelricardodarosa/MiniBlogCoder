from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.

from PostApp.models import Post, Category

def index(request):
    post_random = Post.objects.order_by('?')[:4]
    post_latest = Post.objects.order_by('id')[:3]
    category = Category.objects.all()

    context = {
        'post_random': post_random,
        'post_latest': post_latest,
        'category': category
    }
    return render(request, 'index.html', context)

def blog(request):
    # Aca listamos todos los posts, incluyendo categorias y últimos posts realizados en la columna derecha. 
    
    post = Post.objects.all()
    category = Category.objects.all()
    post_latest = Post.objects.order_by('id')[:3]
    
    # a continuacion incorporamos funcionalidad de pagination para django, para pasar entre numeros de paginas de blog arriba del footer.
    
    paginator = Paginator(post, 4) # Muestra 2 posts por pagina. 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'category' : category,
        'post_latest': post_latest
    }
    return render(request, 'pages/blog.html', context)

def post_detail(request, id, slug):
    post = Post.objects.get(pk=id)
    return render(request, 'pages/post_detail.html',{'post': post })