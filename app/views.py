import random

from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/")
def index():
  return render_template("index.html")

@views.route("/cat", methods=["GET"])
def get_cat():
    q = request.args.get("q")
    if not q:
       q = 1
    cat_image_url = "https://cataas.com/cat?" + str(random.randint(1, 10000))
    return render_template("cat.html", cat_image_url=cat_image_url)
