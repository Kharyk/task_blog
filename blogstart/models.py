from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
class Post_Author(models.Model):
    posts = models.ManyToManyField(Post, related_name='authors')
    
# Create your models here.
