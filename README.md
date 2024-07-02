# task_blog

Pos:
    title CharField
    content TextField
    published_date DateTimeField(blank=True, null=True)

Author:
    name CharField
    email EmailField

post_author:
    posts ManyToManyField(Post, related_name='authors')
