from django.contrib import admin
from .models import Post, Author, PostAuthor
#proxymodelapp
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostAuthor)



# Register your models here.
