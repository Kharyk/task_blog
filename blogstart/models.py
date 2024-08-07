from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def published_recently(self):
        return (timezone.now() - self.published_date).days < 7

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class PostAuthor(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='authors')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"