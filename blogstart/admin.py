from django.contrib import admin
from .models import Post, Author, PostAuthor, Comment
#proxymodelapp
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostAuthor)
admin.site.register(Comment)




# Register your models here.
