from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
model = tf.keras.models.load_model("cat_dog_model.h5")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            img = Image.open(file).resize((256, 256))
            arr = np.array(img) / 255.0
            arr = np.expand_dims(arr, axis=0)
            pred = model.predict(arr)[0][0]
            if pred > 0.5:
                result = f"Ye DOG hai  - {pred*100:.2f}%"
            else:
                result = f"Ye CAT hai - {(1-pred)*100:.2f}%"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()