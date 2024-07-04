import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
import django
django.setup()

from blogstart.models import Post, Author, PostAuthor
from blogstart.views import post_list, author_list, author_detail, post_detail, posts_by_author, authors_by_post

def main():
    while True:
        inquiry = input(
            'Hallo\n'
            'If you want to add a user, Press 1\n'
            'If you want to add a post, Press 2\n'
            'If you want to display all users, Press 3\n'
            'If you want to display all posts, Press 4\n'
            'If you want to display all users who did these posts, Press 5\n'
            'If you want to display all user posts, Press 6\n'
            'If you want to see more info about the author, Press 7\n'
            'If you want to see more info about post, Press 8\n'
            'If you want to exit Press 0\n'
        )

        if inquiry == '0':
            break
        
        elif inquiry == '1':
            name = input('Enter the name of the user: ')
            email = input('Enter the email of the user: ')
            author_list(request=None, add_author=True, name=name, email=email)
            print("User added.")
        
        elif inquiry == '2':
            title = input('Enter the title of the post: ')
            content = input('Enter the content of the post: ')
            published_date = input('Enter the published date (if not, the date will be today automatically): ')
            post_list(request=None, add_post=True, title=title, content=content, published_date=published_date)
            print('Post added.')
        
        elif inquiry == '3':
            for author in Author.objects.all():
                print(f"Name: {author.name}, Email: {author.email}")
        
        elif inquiry == '4':
            for post in Post.objects.all():
                print(f"Title: {post.title}, Published Date: {post.published_date}")
        
        elif inquiry == '5':
            post_id = input('Enter the post ID: ')
            authors_by_post(post_id)
        
        elif inquiry == '6':
            post_id = input('Enter the post ID: ')
            authors_by_post(post_id)
        
        elif inquiry == '7':
            author_id = input('Enter the author ID: ')
            author_detail(author_id)
        
        elif inquiry == '8':
            post_id = input('Enter the post ID: ')
            post_detail(post_id)

if __name__ == "__main__":
    main()
