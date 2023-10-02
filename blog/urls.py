from django.urls import path
from .views import home,blog_post

urlpatterns = [
    path('',home , name="home"),
    path('blog_post/<str:pk>/',blog_post,name="blogpost")
]
