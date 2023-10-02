from django.urls import path,include
from .views import loginview,signupview

urlpatterns = [
   path('login/',loginview,name="login"),
   path('signup/',signupview,name="signup")
]
