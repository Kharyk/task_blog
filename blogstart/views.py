from django.shortcuts import render, get_object_or_404
from .models import Post, Author

def post_list(request):
    posts = Post.objects.all().order_by("published_date")
    
    return render(request, "blog.post_list.html", {"posts": posts})

def author_list(request):
    authors = Author.objects.all().order_by("name")
    return render(request, "blog.author_list.html", {"author": authors})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, "blog/post_detail.html", {"post":post})

def user_detail(request, post_id):
    user = get_object_or_404(Author, pk = author_id)
    return render(request, "blog/author_detail.html", {"author":author})

def post_by_author(request):
    authors = Author.objects.all()
    return render(request, "blog/post_by_author.html", {"author": posts})

def author_by_post(request):
    post = Post.objects.all()
    return render(request, "blog/author_by_post.html", {"posts": authors})

    
    
# Create your views here.
