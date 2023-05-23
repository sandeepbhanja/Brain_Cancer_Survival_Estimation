from flask import Flask, request, render_template
import numpy as np
import scipy.ndimage
import cv2
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017")
db = client["my_database"]
collection = db["3d_images"]


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
  image = request.files["image"]
  collection.insert_one({"image": image.read()})
  return "Image uploaded successfully!"

if __name__ == "__main__":
  app.run(debug=True)
