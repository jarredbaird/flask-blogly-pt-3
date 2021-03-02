"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first = db.Column(db.String(50),
                           nullable=False)
    
    last = db.Column(db.String(50),
                          nullable=True)
    
    image_url = db.Column(db.Text,
                          nullable=True,
                          default='/static/images/avatar.png')

    @classmethod
    def get_users_by_last_name(cls, last):
        return cls.query.filter_by(last=last).all()
    
class Post(db.Model):
    __tablename__ = 'posts'
    
    post_id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.Text,
                           nullable=False)
    
    content = db.Column(db.Text,
                          nullable=True)
    
    created_at = db.Column(db.DateTime,
                          nullable=False,
                          default=datetime.datetime.now)
    
    user_id = db.Column(db.Integer, 
                        db.ForeignKey("users.id"), 
                        nullable=False)
    
    user = db.relationship('User', backref="posts")
    tags = db.relationship('Tag', secondary='post_tags')

class Tag(db.Model):
    __tablename__ = 'tags'

    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_color = db.Column(db.Integer, db.ForeignKey('colors.color_id'))
    tag_name = db.Column(db.Text, nullable=False)
    tag_descr = db.Column(db.Text, default="no description")

    color = db.relationship('Color')
    posts = db.relationship('Post', secondary='post_tags')

    def __repr__(self):
        return f"<Tag {self.tag_id} {self.tag_color} {self.tag_name} {self.tag_descr} >"

class PostTag(db.Model):

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'), primary_key=True)

class Color(db.Model):

    __tablename__ = "colors"

    color_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    bg = db.Column(db.Text, nullable=False)
    badge = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Color {self.color_id} {self.name} {self.bg} {self.text} >"

# colors_list = {
#         "blue": {"name": "Blue",
#                      "bg": 'bg-primary',
#                      "text": 'text-white',
#                      "html": '<div class="p-3 mb-2 bg-primary text-white">Blue</div>'},
#         "white": {"name": "White",
#                       "bg": "bg_secondary",
#                       "text": "text-whtie",
#                       "html": '<div class="p-3 mb-2 bg-secondary text-white">Grey</div>'},
#         "green": {"name": "Green",
#                       "bg": "bg-success",
#                       "text": "text-white",
#                       "html": '<div class="p-3 mb-2 bg-success text-white">Green</div>'},
#         "red": {"name": "Red",
#                     "bg": "bg-danger",
#                     "text": "text-white",
#                     "html": '<div class="p-3 mb-2 bg-danger text-white">Red</div>'},
#         "yellow": {"name": "Yellow",
#                        "bg": "bg-warning",
#                        "text": "text-white",
#                        "html": '<div class="p-3 mb-2 bg-warning text-dark">Yellow</div>'},
#         "teal": {"name": "Teal",
#                      "bg": "bg-info",
#                      "text": "text-white",
#                      "html": '<div class="p-3 mb-2 bg-info text-white">Teal</div>'},
#         "light_grey": {"name": "Light Grey",
#                            "bg": "bg-light",
#                            "text": "text-dark",
#                            "html": '<div class="p-3 mb-2 bg-light text-dark">Light Grey</div>'},
#         "dark": {"name": "Dark",
#                      "bg": "bg-dark",
#                      "text": "text-white",
#                      "html": '<div class="p-3 mb-2 bg-dark text-white">Dark</div>'},
#         "white": {"name": "White",
#                       "bg": "bg-white",
#                       "text": "text-dark",
#                       "html": '<div class="p-3 mb-2 bg-white text-dark">White</div>'}}