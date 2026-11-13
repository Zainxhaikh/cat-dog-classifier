# Cat vs Dog Image Classifier

A Deep Learning web app that classifies an uploaded image as Cat or Dog using TensorFlow + Flask.

## Tech Stack
- Python
- TensorFlow / Keras
- Flask
- HTML, CSS
- NumPy, Pillow

## How it Works
- CNN model trained on Cat vs Dog dataset
- Trained model saved as `cat_dog_model.tflite` for fast inference
- User uploads an image on web app
- Flask backend loads TFLite model and predicts Cat or Dog

## Project Files
- `app.py` - Flask backend
- `cats_vs_dog_classification.ipynb` - Model training notebook
- `cat_dog_model.tflite` - Trained model
- `templates/` - HTML frontend
- `cat.jpg`, `dog.jpg` - Sample test images

## How to Run Locally
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Open browser: `http://127.0.0.1:5000`
5. Upload any Cat / Dog image to test

## Result
Model accurately predicts whether the uploaded image is a Cat or a Dog.

## Author
Zain Ul Abidin - Aspiring AI/ML Developer
