from django.contrib import admin
from .models import Post,Like

# Register your models here.

admin.site.register(Post)       # This will add the Post in our admin site 
admin.site.register(Like)