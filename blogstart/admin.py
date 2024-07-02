from django.contrib import admin
from .models import Post, Author
#proxymodelapp
admin.site.register(Post)
admin.site.register(Author)


# Register your models here.
