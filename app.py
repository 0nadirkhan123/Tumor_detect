
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = load_model("brain_tumor_model.keras")

# Define class labels (based on your model training)
class_labels = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    img_path = None

    if request.method == "POST":
        file = request.files.get("img")  # 👈 must match the 'name' in HTML: <input name="img">
        if file:
            # Save the uploaded image to static folder
            img_path = os.path.join("static", "uploaded_image.jpg")
            file.save(img_path)

            # Preprocess image
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Predict
            preds = model.predict(img_array)
            class_index = np.argmax(preds[0])
            prediction = class_labels[class_index]

    return render_template("index.html", prediction=prediction, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)
