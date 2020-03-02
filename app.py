__aurthor__ = 'reubin'

from models.post import Post
from models.blog import Blog
from database import Database


Database.initialize()

blog = Blog(author="James",
            title="title",
            description="content")
blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())

