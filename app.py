__aurthor__ = 'reubin'

from models.post import Post
from database import Database


Database.initialize()

post = Post(blog_id="123",
            title="The Greatest Post",
            content="some content",
            author="Reubin")
post.save_to_mongo()

