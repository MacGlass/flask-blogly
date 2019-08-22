"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'hey ma'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def load_page():

    return redirect('/users')


@app.route('/users')
def load_users():

    all_users = User.query.all()

    return render_template("user.html", users=all_users)


@app.route("/users/new", methods=["GET", "POST"])
def create_user():

    if request.method == 'GET': 
        return render_template("createUser.html")
 
    first_name = request.form['first']
    last_name = request.form['last']
    image = request.form['image']
    if image == '':
        image = None

    print(first_name, last_name, image)

    new_user = User(first_name=first_name,
                    last_name=last_name,
                    image_url=image)

    db.session.add(new_user)
    db.session.commit()

    user_id = User.id

    return redirect("/users")


@app.route("/users/<id>")
def view_user(id):

    a = User.query.get(id)
    first = a.first_name
    last = a.last_name
    image = a.image_url
    id = a.id

    return render_template("profile.html", first=first,
                           last=last, image=image, id=id)


@app.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    b = User.query.get(id)
    db.session.delete(b)
    flash("User Successfully Deleted!")
    db.session.commit()
    return redirect("/users")


@app.route("/users/<id>/edit", methods=["GET", "POST"])
def edit_user(id):
    user = User.query.get(id)

    if request.method == 'GET':
        return render_template("edit.html", user=user)

    c = User.query.get(id)
    edit_first = request.form['first']
    edit_last = request.form['last']
    edit_image = request.form['image']

    if c.first_name != edit_first:
        c.first_name = edit_first
    if c.last_name != edit_last:
        c.last_name = edit_last
    if c.image_url != edit_image:
        c.image_url = edit_image
    db.session.commit()

    return redirect(f"/users/{id}")
