"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db import models
from .models import Blog
from .forms import BlogForm
from .forms import Support
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.all()
    

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts, 
            
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_l = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr) 
            comment_f.save()

            return redirect('blogpost', parametr=post_l.id)
    else:
        form = CommentForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_l': post_l, 
            'comments': comments,
            'form': form,
            'year':datetime.now().year,
        }
    )

def newpost(request):
    
    assert isinstance(request, HttpRequest)

    if request.method == "POST": 
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid(): 
            blog_f = blogform.save(commit=False) 
            blog_f.posted = datetime.now() 
            blog_f.autor = request.user 
            blog_f.save() 

            return redirect('blog') 
    else:
        blogform = BlogForm()
    return render(
        request,
        'app/newpost.html',
        {

        'blogform': blogform, 
        'title':'Добавить статью блога',

        'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О Нас',
            'message':'Сведения о нас',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Сведения о средах разработки',
            'year':datetime.now().year,
        }
    )

def pool(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина','2':'Женщина'}
    abilities = {'1': 'не знаком с английским языком',
                '2': 'знает основы',
                '3': 'может читать на английском',
                '4': 'может говорить на английском'}
    if request.method == 'POST':
        form = Support(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            data['gender'] = gender[ form.cleaned_data['gender'] ]
            data['abilities'] = abilities[ form.cleaned_data['abilities'] ]
            form = None
    else:
        form = Support()
    return render(
        request,
        'app/pool.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request):
    
    assert isinstance(request, HttpRequest)
    if request.method == "POST": 
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): 
            reg_f = regform.save(commit=False) 
            reg_f.is_staff = False 
            reg_f.is_active = True 
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now() 
            reg_f.last_login = datetime.now() 
            regform.save() 
            return redirect('home') 
    else:
        regform = UserCreationForm() 
    return render(
        request,
        'app/registration.html',
        {

        'regform': regform, 
        'year':datetime.now().year,
        }
    )

def videopost(request):
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'message':'Видео о сайте',
            'year':datetime.now().year,
        }
    )
