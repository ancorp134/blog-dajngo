from django.shortcuts import render , redirect
from django.urls import reverse
from .models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from blog.models import Post
# Create your views here.


def loginview(request):

    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email,password=password)
        
        if user is not None:
           
            context = {
                
                'user' : user
            }
            login(request,user)
            
            return redirect(reverse('dashboard'),context)
        
        return messages.error(request,"Invalid credentials")

    return render(request,"login.html")



def signupview(request):
    if request.method=='POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.create_user(
            email = email,
            first_name = first_name,
            last_name  = last_name,
            password = password
        )

        if user:
            messages.success(request, "Registration Complete Successfully...")

        return redirect('signup')

    return render(request,"signup.html")



def dashboard(request):
    posts = Post.objects.get(author=request.user)
    context = {'posts' : posts}
    return render(request , 'dashboard.html' , context)








