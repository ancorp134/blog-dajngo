from django.urls import path,include
from .views import home,blog_post

urlpatterns = [
    path('',home , name="home"),
    path('blog_post/<str:pk>/',blog_post,name="blogpost"),
    path('',include('account.urls'))
]
