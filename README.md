# task_blog

Pos:
    title CharField
    content TextField
    published_date DateTimeField(blank=True, null=True)

Autho:
    name CharField
    email EmailField
    posts ManyToManyField(Post, related_name='authors')