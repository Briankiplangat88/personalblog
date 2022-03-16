import unittest
from app.models import Comment,Blog,User
from app import db
class CommentTest(unittest.TestCase):
    def setUp(self):
        self.newComment = Comment(id = 1, comment = 'Test comment', user = self.userBryan, blog_id = self.newBlog)
    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
    def checkvariablesTest(self):
        self.assertEquals(self.newComment.comment,'Test comment')
        self.assertEquals(self.newComment.user,self.bryan)
        self.assertEquals(self.newComment.blogs_id,self.newblog)
class CommentTest(unittest.TestCase):
    def setUp(self):
        self.bryan = User(username='bryan', password='12345', email='bryanbryson85@gmail.com')
        self.newblog = Blog(id=1, title='Encapsulation', content='Testing', user_id=self.userBryan.id)
        self.newComment = Comment(id=1, comment =' test comment', user_id=self.bryan.id, blog_id = self.newblog.id )
    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
        Comment.query.deleteComment()
    def checkInstanceVariables(self):
        self.assertEquals(self.newComment.comment, 'test comment')
        self.assertEquals(self.newComment.user_id, self.bryan.id)
        self.assertEquals(self.newComment.blog_id, self.new_blog.id)