from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://images.freeimages.com/images/large-previews/277/doggy-1382866.jpg"


def connect_db(app):

    db.app = app
    db.init_app(app)


"""Models for Blogly."""


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String,
                           nullable=False)
    last_name = db.Column(db.String,
                          nullable=False)
    image_url = db.Column(db.String,
                          nullable=True,
                          default=DEFAULT_IMAGE_URL)


class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String,
                      nullable=False)
    content = db.Column(db.String,
                        nullable=False)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))


class Tag(db.Model):
    """Tag."""

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String,
                     nullable=False,
                     unique=True)
    posts = db.relationship('Post',
                            secondary='posttags',
                            backref='tags')


class PostTag(db.Model):
    """PostTag."""

    __tablename__ = "posttags"

    post_id = db.Column(db.Integer,
                        db.ForeignKey("posts.id"),
                        primary_key=True)
    tag_id = db.Column(db.Integer,
                       db.ForeignKey("tags.id"),
                       primary_key=True)
