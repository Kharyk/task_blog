from blogstart.models import Post, Author
from blogstart.views import post_list, author_list, user_detail, post_detail, post_by_author, author_by_post

while inquiry != 0:
    
    inquiry = input(str('Hallo\nIf you want to add a user, Press 1\nIf you want to add a post, Press 2\nIf you want to display all users, Press 3\nIf you want to display all posts, Press 4\nIf you want to display all user posts, Press 5\nIf you want to display all users posts, Press 6\nIf you want to see more info about author, Press 7\nIf you want to see more info about post, Press 8\nIf you want to exit Press 0'))
   
    if inquiry == 1:
        
        name = input(str('Enter the name of the user: '))
        email = input(str('Enter the email of the user: '))
       
        author_add = Author(
            name=name,
            email=email
        )
        author_add.save()
        
        print("User added.")
        
    if inquiry == 2:
        
        title = input(str('Enter the title of the post: '))
        content = input(str('Enter the content of the post: '))
        published_date = input(str('Enter the published date(if not the date will be today, automatically):'))
        
        post_add = Post(
            title= title,
            content= content,
            published_date= published_date
        )
        post_add.save()
        
        print('Post added.')
        
    if inquiry == 3:
        
        post_list()
        
    if inquiry == 4:
        
        author_list()
        
    if inquiry == 5:
        
        post_by_author()
        
    if inquiry == 6:
        
        author_by_post()
        
""" if inquiry == 7:
        
        user_detail()
        
    if inquiry == 8:
        
        post_detail()"""
       
    
