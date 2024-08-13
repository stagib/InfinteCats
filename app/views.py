from flask import Blueprint, render_template
import requests

views = Blueprint("views", __name__)

@views.route("/")
def index():
  return render_template("index.html")

@views.route("/cat", methods=["GET"])
def get_cat():
    response = requests.get("https://cataas.com/cat")
    if response.status_code == 200:
        cat_image_url = "https://cataas.com/cat"
    else:
        cat_image_url = None
    return