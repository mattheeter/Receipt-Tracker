from flask import Blueprint, render_template

# Create blueprint to add all routes in here rather than initialztion file "app.py"

views = Blueprint(__name__, 'views') # Initializing bluepring

@views.route("/")
def home():
    return render_template("index.html", name="Matt") # When you go to this root, it will render "index.html"
        # Can also pass variables and values to be rendered by the template
        # Can access the name variable inside the html file

@views.route("/profile/<username>") # <> used to make a dynamic url (value can change)
def profile(username):
    return render_template("index.html", name=username)
