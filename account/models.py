from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False)
    email = models.EmailField(_("email address"), unique=True)
    bio = models.TextField(max_length=50,null=True)
    dob = models.DateField(auto_now_add=False,null=True)
    address = models.CharField(max_length=50,null=True)
    avatar = models.ImageField(upload_to="avatars",blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
