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


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"), port=os.environ.get("PORT"), debug=True,
    )

