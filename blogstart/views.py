from django.shortcuts import render, get_object_or_404
from .models import Post, Author, PostAuthor

def post_list(request):
    posts = Post.objects.all().order_by("published_date")
    return render(request, "blog/post_list.html", {"posts": posts})

def author_list(request):
    authors = Author.objects.all().order_by("name")
    return render(request, "blog/author_list.html", {"authors": authors})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_detail.html", {"post": post})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "blog/author_detail.html", {"author": author})

def posts_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(authors__author=author).order_by('published_date')
    return render(request, "blog/posts_by_author.html", {"author": author, "posts": posts})

def authors_by_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    authors = Author.objects.filter(posts__post=post).order_by('name')
    return render(request, "blog/authors_by_post.html", {"post": post, "authors": authors})
