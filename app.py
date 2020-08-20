import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Imports confidential env.py
if os.path.exists("env.py"):
    import env

# Configurations for MongoDB, taken from env.py
app = Flask(__name__)
app.config["MONGO_DBNAME"] = "plant_swap"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Variables
mongo = PyMongo(app)
posts = mongo.db.posts
countries = mongo.db.countries
users = mongo.db.users


# Start of routes


@app.route("/")
def index():
    """
    Directs users to landing page
    Args:
        none
    Returns:
        (str) Redirects to account route or renders "index.html" template
    """
    if "username" in session:
        return redirect(url_for("account"))
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Directs users to login form
    Args:
        none
    Returns:
        (str) Redirects to index route or renders "errorlogin.html" template
    """
    if "username" in session:
        return redirect(url_for("account"))
    else:
        if request.method == "POST":
            # Searches MongoDB users database for user
            current_user = users.find_one(
                {"username": request.form.get("username").lower()}
            )
            # If the username exists, the filled in hashed
            # password gets compared to the password in the DB
            if current_user:
                if (
                    bcrypt.hashpw(
                        request.form.get("password").encode("utf-8"),
                        current_user["password"],
                    )
                    == current_user["password"]
                ):
                    # If passwords match
                    session["username"] = request.form.get("username").lower()
                    session["email"] = current_user["email"]
                    return redirect(url_for("index"))
                # If the passwords don't match
                else:
                    return render_template("errorlogin.html")
            # If the username does not exist
            else:
                return render_template("errorlogin.html")
        return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Logs current user out
    Args:
        none
    Returns:
        (str) Redirects to index route
    """
    session.clear()
    return redirect(url_for("index"))


@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Directs users to register form
    Args:
        none
    Returns:
        (str) Redirects to index route  or renders "errorregister.html" template
    """
    if "username" in session:
        return redirect(url_for("account"))
    else:
        if request.method == "POST":
            # Checks MongoDB to ensure username and email haven't been used before
            existing_user = users.find_one({"username": request.form.get("username")})
            existing_email = users.find_one({"email": request.form.get("email")})
            if existing_user is None and existing_email is None:
                # Hashes entered pw and stores in variable
                hashpass = bcrypt.hashpw(
                    request.form.get("password").encode("utf-8"), bcrypt.gensalt()
                )
                users.insert_one(
                    {
                        "username": request.form.get("username").lower(),
                        "email": request.form.get("email").lower(),
                        "password": hashpass,
                    },
                )
                session["username"] = request.form.get("username").lower()
                session["email"] = request.form.get("email").lower()
                return redirect(url_for("index"))
            else:
                return render_template("errorregister.html")
        else:
            return render_template("register.html")


@app.route("/remove_account/<email>", methods=["POST", "GET"])
def remove_account(email):
    """
    Deletes account when button is pressed
    Args:
        (str) email
    Returns:
        (str) Redirects to logout route
    """
    # Searches for posts with user email and deletes from DB
    posts.delete_one({"email": session["email"]})
    # Searches for users with user email and deletes from DB
    users.delete_one({"email": session["email"]})
    return redirect(url_for("logout"))


@app.route("/account")
def account():
    """
    Loads User Account Page
    Args:
        none
    Returns:
        (str) Renders "account.html" template or redirects to index route
    """
    if "username" in session:
        # Counts the number of posts on page
        number_posts = posts.count_documents({"email": session["email"]})
        return render_template(
            "account.html", posts=posts.find(), number_posts=number_posts
        )
    else:
        return redirect(url_for("index"))


@app.route("/about")
def about():
    """
    Loads About Page
    Args:
        none
    Returns:
        (str) Renders "about.html" template
    """
    return render_template("about.html",)


@app.route("/get_posts")
def get_posts():
    """
    Loads Posts Page
    Args:
        none
    Returns:
        (str) Renders "posts.html" template
    """
    return render_template("posts.html", posts=posts.find(), countries=countries.find())


@app.route("/add_post")
def add_post():
    """
    Loads Add Posts Page
    Args:
        none
    Returns:
        (str) Renders "addpost.html" template
    """
    return render_template("addpost.html", countries=countries.find())


@app.route("/submit_post", methods=["POST"])
def submit_post():
    """
    Submits new post
    Args:
        none
    Returns:
        (str) Redirects to "account" route
    """
    # Gets all of the data from the form and creates new post in mongoDB
    posts.insert_one(
        {
            "plant_name": request.form.get("plant_name"),
            "location": request.form.get("location"),
            "looking_for": request.form.get("looking_for"),
            "plant_image": request.form.get("plant_image"),
            "date_posted": request.form.get("date_posted"),
            "email": request.form.get("email").lower(),
        },
    )
    return redirect(url_for("account"))


@app.route("/edit_post/<post_id>")
def edit_post(post_id):
    """
    Loads Edit Post Page
    Args:
        (str) post_id
    Returns:
        (str) Renders "editpost.html" template
    """
    # Searches for post in DB with the same id
    the_post = posts.find_one({"_id": ObjectId(post_id)})
    return render_template("editpost.html", post=the_post, countries=countries.find())


@app.route("/update_post/<post_id>", methods=["POST"])
def update_post(post_id):
    """
    Updates post
    Args:
        (str) post_id
    Returns:
        (str) Redirects to "account" route
    """
    posts.replace_one(
        {"_id": ObjectId(post_id)},
        {
            "plant_name": request.form.get("plant_name"),
            "location": request.form.get("location"),
            "looking_for": request.form.get("looking_for"),
            "plant_image": request.form.get("plant_image"),
            "date_posted": request.form.get("date_posted"),
            "email": request.form.get("email").lower(),
        },
    )
    return redirect(url_for("account"))


@app.route("/remove_post/<post_id>", methods=["POST", "GET"])
def remove_post(post_id):
    """
    Deletes post when confirmed
    Args:
        (str) post_id
    Returns:
        (str) Redirects to "account" route
    """
    # removes post with the same _id in the DB
    posts.delete_one({"_id": ObjectId(post_id)})
    return redirect(url_for("account"))


@app.route("/filter_posts", methods=["POST"])
def filter_posts():
    """
    Filters post based on country selected
    Args:
        none
    Returns:
        (str) Renders "posts.html" template
    """
    # Gets the selected country from the form
    filter_results = posts.find({"location": request.form.get("location")})
    # Counts the number of posts with the selected country
    number_results = posts.count_documents({"location": request.form.get("location")})
    return render_template(
        "posts.html",
        posts=filter_results,
        countries=countries.find(),
        number_results=number_results,
    )


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"), port=os.environ.get("PORT"), debug=False,
    )
