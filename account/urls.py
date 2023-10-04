from django.urls import path,include
from .views import loginview,signupview,dashboard


urlpatterns = [
   path('login/',loginview,name="login"),
   path('signup/',signupview,name="signup"),
   path('dashboard/',dashboard,name='dashboard')
]
