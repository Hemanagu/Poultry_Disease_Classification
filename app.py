from flask import Flask, render_template, request, redirect, url_for
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import os
import uuid
import json

import requests

MODEL_URL = "https://huggingface.co/Bharathchilaka/poultry-disease-model/resolve/main/best.pt"
MODEL_PATH = "models/best.pt"

os.makedirs("models", exist_ok=True)

if not os.path.exists(MODEL_PATH):
    print("Downloading model from Hugging Face...")
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, 'wb') as f:
        f.write(response.content)
    print("Download complete.")


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Storage path for prediction history and uploaded images
HISTORY_FILE = 'history.json'
UPLOAD_FOLDER = 'static/temp_uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Label mapping
labels = ['Coccidiosis', 'Healthy', 'Newcastle Disease', 'Salmonella']

# Load model
model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, len(labels))
checkpoint = torch.load('models/best.pt', map_location='cpu')
model.load_state_dict(checkpoint['model_state_dict'])
model.eval()

# Image transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    confidence = None
    image_path = None
    history = load_history()

    if request.method == 'POST':
        file = request.files.get('image')
        if not file or file.filename == '':
            return redirect(request.url)

        image = Image.open(file.stream).convert('RGB')
        img_t = transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = model(img_t)
            probs = torch.nn.functional.softmax(outputs[0], dim=0)
            confidence_score, predicted = torch.max(probs, 0)
            prediction = labels[predicted.item()]
            confidence = round(confidence_score.item() * 100, 2)

        # Save image to disk
        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        image.save(filepath)
        image_path = '/' + filepath.replace('\\', '/')

        # Save history
        history.insert(0, {
            'result': prediction,
            'confidence': confidence,
            'filename': filename
        })
        history = history[:5]  # Keep last 5 entries
        save_history(history)

    return render_template('predict.html', prediction=prediction, confidence=confidence, image_path=image_path, history=history)

@app.route('/clear-history')
def clear_history():
    save_history([])
    # Clear images
    for f in os.listdir(UPLOAD_FOLDER):
        os.remove(os.path.join(UPLOAD_FOLDER, f))
    return redirect(url_for('predict'))

@app.route('/delete/<int:index>')
def delete(index):
    history = load_history()
    if 0 <= index < len(history):
        # Delete the image file
        img_path = os.path.join(UPLOAD_FOLDER, history[index]['filename'])
        if os.path.exists(img_path):
            os.remove(img_path)
        history.pop(index)
        save_history(history)
    return redirect(url_for('predict'))

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
