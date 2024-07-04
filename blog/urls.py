"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogstart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('authors/', views.author_list, name='author_list'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    path('author/<pk>/', views.author_detail, name='author_detail'),
    path('author/<pk>/posts/', views.posts_by_author, name='posts_by_author'),
    path('post/<pk>/authors/', views.authors_by_post, name='authors_by_post'),
]
