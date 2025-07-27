
# 🧠 Brain Tumor Detection App

A web-based tool to detect the type of brain tumor from MRI images using deep learning.

---

## 🌟 Features

- 🧪 Upload an MRI scan and instantly predict tumor type
- 📸 Supports all common image formats (JPG, PNG)
- 🎯 Detects 4 categories: 
  - Glioma
  - Meningioma
  - Pituitary
  - No Tumor
- 🌐 Simple and aesthetic web interface built with Flask
- ⚙️ Lightweight and easy to run locally

---

## 📁 Folder Structure

```
project/
├── app.py                   # Flask backend
├── brain_tumor_model.keras  # Trained model (not mentioned in UI)
├── templates/
│   └── index.html           # Frontend interface
├── static/
│   └── uploaded_image.jpg   # Uploaded file display
└── README.md
```


## 🚀 How to Run

### 1. Setup Virtual Environment

# (Windows)
>python -m venv venv
>venv\Scripts\activate

# Install required packages
>pip install flask tensorflow pillow


### 2. Start the App

>python app.py


>Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 🖼 How It Works

1. Upload a brain MRI scan.
2. The backend processes the image.
3. The prediction is displayed on the webpage.
4. The image preview and tumor type appear below the form.

---

## 📦 Requirements

- Python 3.9 recommended
- TensorFlow
- Flask
- Pillow

---

## 💡 Future Ideas

- Add heatmap visualization (Grad-CAM)
- Deploy to Render or HuggingFace Spaces
- Add mobile-friendly layout

---

## 👤 Author

Created by [Mohammed Nadir Khan]  

