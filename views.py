from flask import Blueprint, render_template, request, redirect, url_for

# Create blueprint to add all routes in here rather than initialztion file "app.py"

views = Blueprint(__name__, 'views') # Initializing blueprint

@views.route("/")
def home():
    return render_template("index.html", name="Matt") # When you go to this root, it will render "index.html"
        # Can also pass variables and values to be rendered by the template
        # Can access the name variable inside the html file

#@views.route("/profile/<username>") # <> used to make a dynamic url (value can change)
#def profile(username):
#    return render_template("index.html", name=username)

@views.route("/profile")
def profile():
    args = request.args
    username = args.get('username') # Can also use a query (/?variable_name="") to get the value, alternative to above function
    return render_template("index.html", name=username)

@views.route("/go-to-home") # Allosing user to redirect to a different directory
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/additional")
def additional():
    return render_template("additional.html")