"""Seed file to make sample data for Users db."""

from models import User, Post, Tag, Color, PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()
Color.query.delete()
Tag.query.delete()
PostTag.query.delete()

# Add users
one = User(first='Jarred', last="Baird", image_url="https://static2.cbrimages.com/wordpress/wp-content/uploads/2020/06/Screenshot-2020-07-04-at-11.57.49-PM.jpg?q=50&fit=crop&w=740&h=370")
two = User(first='Sonic', last="the Hedgehog", image_url="/static/images/sonic.png")
three = User(first='Butt', last="Farts")
four = User(first='Booty', last="Farts")

# Add posts
meh = Post(title="I'm so lonely", content="Can anybody hear me?", user_id=1)
meh_meh = Post(title="Now I'm happy", content="It just makes me wanna play the banjo!", user_id=1)

# Add colors
blue = Color(name="Blue",
                bg='bg-primary',
                badge='badge-primary',
                text='text-white'
)
secondary = Color(name="Grey",
                bg="bg-secondary",
                badge='badge-secondary',
                text="text-white"
                )
green = Color(name="Green",
                bg="bg-success",
                badge='badge-success',
                text="text-white",
               )
red = Color(name="Red",
            bg="bg-danger",
                badge='badge-danger',
            text="text-white",
           )
yellow = Color(name="Yellow",
                bg="bg-warning",
                badge='badge-warning',
                text="text-white",
                )
teal = Color(name="Teal",
                bg="bg-info",
                badge='badge-info',
                text="text-white",
               )
light_grey = Color(name="Light Grey",
                    bg="bg-light",
                badge='badge-light',
                    text="text-dark",
                    )
dark = Color(name="Dark",
                bg="bg-dark",
                badge='badge-dark',
                text="text-white",
               )
white = Color(name="White",
                bg="bg-white",
                badge='badge-white',
                text="text-dark"
                )

db.session.add(blue)
db.session.add(secondary)
db.session.add(green)
db.session.add(red)
db.session.add(yellow)
db.session.add(teal)
db.session.add(light_grey)
db.session.add(dark)
db.session.add(white)
db.session.commit()

# Add tags
heh = Tag(tag_name="skin tag", tag_color=4, tag_descr="pretty self explanatory")
hehe = Tag(tag_name="dog tag", tag_color=3, tag_descr="a tag a soldier wears during conflict")

# Add new users and tags to session, so they'll persist
db.session.add(one)
db.session.add(two)
db.session.add(three)
db.session.add(four)
db.session.add(heh)
db.session.add(hehe)
db.session.commit()

# Add new posts to the session
db.session.add(meh)
db.session.add(meh_meh)

# Add post tags
pt = PostTag(post_id=1,tag_id=1)
pt2 = PostTag(post_id=2, tag_id=1)
pt3 = PostTag(post_id=1, tag_id=2)
db.session.add(pt)
db.session.add(pt2)
db.session.add(pt3)
db.session.commit()

# Commit--otherwise, this never gets saved!
db.session.commit()
