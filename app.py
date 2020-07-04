import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256


if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "plant_swap"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_posts")
def get_posts():
    return render_template("posts.html", posts=mongo.db.posts.find())


@app.route("/add_post")
def add_post():
    return render_template("addpost.html")


@app.route("/submit_post", methods=["POST"])
def submit_post():
    posts = mongo.db.posts
    posts.insert_one(request.form.to_dict())
    return redirect(url_for("get_posts"))


@app.route("/edit_post/<post_id>")
def edit_post(post_id):
    the_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("editpost.html", post=the_post)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"), port=os.environ.get("PORT"), debug=True,
    )

