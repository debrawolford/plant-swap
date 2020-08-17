import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "plant_swap"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Variables
mongo = PyMongo(app)
posts = mongo.db.posts
countries = mongo.db.countries
users = mongo.db.users


@app.route("/")
def index():
    if "username" in session:
        return render_template("account.html")
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        current_user = users.find_one({"username": request.form["username"].lower()})
        if current_user:
            if (
                bcrypt.hashpw(
                    request.form["password"].encode("utf-8"), current_user["password"]
                )
                == current_user["password"]
            ):
                session["username"] = request.form.get("username").lower()
                return redirect(url_for("index"))
            else:
                return render_template("error-login.html")
        else:
            return render_template("error-login.html")
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        existing_user = users.find_one({"username": request.form.get("username")})
        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form.get("password").encode("utf-8"), bcrypt.gensalt()
            )
            users.insert_one(
                {
                    "username": request.form.get("username").lower(),
                    "email": request.form.get("email"),
                    "password": hashpass,
                },
            )
            session["username"] = request.form.get("username").lower()
            return redirect(url_for("index"))
        else:
            return render_template("error-register.html")
    else:
        return render_template("register.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/get_posts")
def get_posts():
    return render_template("posts.html", posts=posts.find(), countries=countries.find())


@app.route("/add_post")
def add_post():
    return render_template("addpost.html", countries=countries.find())


@app.route("/submit_post", methods=["POST"])
def submit_post():
    posts.insert_one(request.form.to_dict())
    return redirect(url_for("get_posts"))


@app.route("/edit_post/<post_id>")
def edit_post(post_id):
    the_post = posts.find_one({"_id": ObjectId(post_id)})
    return render_template("editpost.html", post=the_post)


@app.route("/update_post/<post_id>", methods=["POST"])
def update_post(post_id):
    posts.update(
        {"_id": ObjectId(post_id)},
        {
            "plant_name": request.form.get("plant_name"),
            "location": request.form.get("location"),
            "looking_for": request.form.get("looking_for"),
            "plant_image": request.form.get("plant_image"),
            "date_posted": request.form.get("date_posted"),
            "email": request.form.get("email"),
        },
    )
    return redirect(url_for("get_posts"))


@app.route("/remove_post/<post_id>", methods=["POST", "GET"])
def remove_post(post_id):
    posts.remove({"_id": ObjectId(post_id)})
    return redirect(url_for("get_posts"))


@app.route("/filter_posts", methods=["POST"])
def filter_posts():
    filter_results = posts.find({"location": request.form.get("location")})
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
