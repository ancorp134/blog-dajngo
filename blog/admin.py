from django.contrib import admin
from .models import Category,Post,Tag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)

class Post(admin.ModelAdmin):
    list_display = ('id','title','pub_date')


