from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from PostApp.models import Post, Category, Comment
from MiniBlogApp.models import Contact
from MiniBlogApp.forms import ContactForm
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    post_random = Post.objects.order_by('?')[:4]
    post_latest = Post.objects.order_by('id')[:3]
    category = Category.objects.all()

    context = {
        'post_random': post_random,
        'post_latest': post_latest,
        'category': category,
        'home_page': 'active'
    }
    return render(request, 'index.html', context)

def blog(request):
    # Aca listamos todos los posts, incluyendo categorias y últimos posts realizados en la columna derecha. 
    
    post = Post.objects.all()
    category = Category.objects.all()
    post_latest = Post.objects.order_by('id')[:3]
    
    # a continuacion incorporamos funcionalidad de pagination para django, para pasar entre numeros de paginas de blog arriba del footer.
    
    paginator = Paginator(post, 2) # Muestra 2 posts por pagina. 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'category' : category,
        'post_latest': post_latest,
        'blog_page': 'active'
    }
    return render(request, 'pages/blog.html', context)

def post_detail(request, id, slug):
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post_id=id, status='Leido')
    total = 0
    for i in comments:
        total = total + 1
    
    context = {
        'post': post,
        'comments': comments,
        'total': total}

    return render(request, 'pages/post_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']

            data.save()
            return HttpResponseRedirect('/contact/')
    form = ContactForm
    context = {
        'form': form,
        'contact_page':'active'
    }

    return render(request, 'pages/contact.html', context)

def about(request):
    
    context = {
        'about_page': 'active'
    }
    return render(request, 'pages/about.html', context)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("Login")
            
        else:
            return redirect("Login")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form":form, "login_page":"active"})
            
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            
            return redirect("Login")
        
        return redirect("Register")
    else:
        form = UserRegisterForm()
        return render(request, "register.html", {"form":form,"register_page":"active"})

def logout_request(request):
    logout(request)
    return redirect("inicio")

def editar_perfil(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.password1 = info["password1"]
            user.password2 = info["password1"]
            user.save()
            
            return redirect("inicio")
    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name,"last_name":user.last_name})
    
    return render(request, "editar_perfil.html", {"form":form, "user":user})