from django.shortcuts import render
from .models import Category, Tag, Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    
    context = {'posts': posts , 'categories': categories}
    
    return render(request, "index.html", context)

def blog_post(request,pk):
    post = Post.objects.get(id=pk)
    categories = Category.objects.all()
    
    context = {'post': post , 'categories': categories}
    return render(request,"blog_post.html",context)


