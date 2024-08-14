import random
import requests
from flask import Blueprint, render_template, render_template_string, request

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
    return render_template("cat.html", cat_image_url=cat_image_url, cats=int(q))

@views.route("/cat/image", methods=["GET"])
def get_cat_image():
   cat_image_url = "https://cataas.com/cat?" + str(random.randint(1, 10000))
   image_tag = f"<img src='{cat_image_url}' alt='cat ran away'>"
   return render_template_string(image_tag)

@views.route("/qoute", methods={"GET"})
def get_qoute():
    response = requests.get("https://api.quotable.io/random?" + str(random.randint(1, 10000)))
    quote = response.json()

    return render_template("quote.html", quote=quote)