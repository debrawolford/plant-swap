import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Imports env.py (file containing confidential information)
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
# Landing Page
@app.route("/")
def index():
    # If user is currently logged in it redirects to account.html
    if "username" in session:
        return redirect(url_for("account"))
    # If no user is logged in, redirects to the landing page, index.html
    return render_template("index.html")


# Login Form: For user who have already registered but are not signed in
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # Searches MongoDB users database to see if filled in username exists
        current_user = users.find_one(
            {"username": request.form.get("username").lower()}
        )
        # If the username is in the DB, the filled in hashed password gets compared to the
        # password in the DB
        if current_user:
            if (
                bcrypt.hashpw(
                    request.form.get("password").encode("utf-8"),
                    current_user["password"],
                )
                == current_user["password"]
            ):
                # If the two passwords are the same, it starts a session and redirects to the index function
                session["username"] = request.form.get("username").lower()
                session["email"] = current_user["email"]
                return redirect(url_for("index"))
            # If the passwords don't match, it redirects to error-login.html
            else:
                return render_template("error-login.html")
        # If the username is not in the DB, it redirects to error-login.html
        else:
            return render_template("error-login.html")
    return render_template("login.html")


# Log Out: When users press the Sign Out button
@app.route("/logout")
def logout():
    # Ends session
    session.clear()
    # Redirects to index.html
    return redirect(url_for("index"))


# Register Form: Allows users to create an account
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # Checks MongoDB to ensure username and email haven't been used before
        existing_user = users.find_one({"username": request.form.get("username")})
        existing_email = users.find_one({"email": request.form.get("email")})
        if existing_user is None and existing_email is None:
            # Hashes password that user has entered and stores in variable
            hashpass = bcrypt.hashpw(
                request.form.get("password").encode("utf-8"), bcrypt.gensalt()
            )
            # Inserts user data into MongoDB users collection
            users.insert_one(
                {
                    "username": request.form.get("username").lower(),
                    "email": request.form.get("email").lower(),
                    "password": hashpass,
                },
            )
            # Starts session with entered username and email and redirects to account
            session["username"] = request.form.get("username").lower()
            session["email"] = request.form.get("email").lower()
            return redirect(url_for("index"))
        # If username or email already exists, redirects to error-register.html
        else:
            return render_template("error-register.html")
    else:
        return render_template("register.html")


# Delete Account: When user pushed the delete account button and confirms
@app.route("/remove_account/<email>", methods=["POST", "GET"])
def remove_account(email):
    # Searches for posts with user email and deletes from DB
    posts.delete_one({"email": session["email"]})
    # Searches for users with user email and deletes from DB
    users.delete_one({"email": session["email"]})
    return redirect(url_for("logout"))


# User Account Page: Allows user to see/edit/delete their posts, and delete their account
@app.route("/account")
def account():
    # Checks if user is logged in
    if "username" in session:
        # Counts the number of posts on page
        number_posts = posts.count_documents({"email": session["email"]})
        # Redirects to account.html
        return render_template(
            "account.html", posts=posts.find(), number_posts=number_posts
        )
    # If user is not logged in, redirects to index
    else:
        return redirect(url_for("index"))


# About Page
@app.route("/about")
def about():
    return render_template("about.html",)


# Posts Page: Shows posts made by all users
@app.route("/get_posts")
def get_posts():
    return render_template("posts.html", posts=posts.find(), countries=countries.find())


# Add Post Page: Allows users to create a new post
@app.route("/add_post")
def add_post():
    return render_template("addpost.html", countries=countries.find())


# Submit Post: When user presses submit after filling in the form on addpost.html
@app.route("/submit_post", methods=["POST"])
def submit_post():
    # Gets all of the filled in data from the form and created a new post in mongoDB
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


# Edit Post Page: Allows user to edit their own posts
@app.route("/edit_post/<post_id>")
def edit_post(post_id):
    # Searches for post in DB with the same id
    the_post = posts.find_one({"_id": ObjectId(post_id)})
    return render_template("editpost.html", post=the_post, countries=countries.find())


# Update Post: When user presses submit after updating the form on editpost.html
@app.route("/update_post/<post_id>", methods=["POST"])
def update_post(post_id):
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


# Remove Post: Allows for a post to be deleted when user presses delete button
@app.route("/remove_post/<post_id>", methods=["POST", "GET"])
def remove_post(post_id):
    # removes post with the same _id in the DB
    posts.delete_one({"_id": ObjectId(post_id)})
    return redirect(url_for("account"))


# Filter Posts: Filters posts depending on the country selected
@app.route("/filter_posts", methods=["POST"])
def filter_posts():
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
        host=os.environ.get("IP"), port=os.environ.get("PORT"), debug=True,
    )
