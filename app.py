from flask import Flask, render_template, request
import os

from models.crop_model import predict_crop
from models.fertilizer import recommend_fertilizer
from models.disease_model import detect_disease
from utils.weather import get_weather
from utils.ndvi import calculate_ndvi

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['N'])
    P = int(request.form['P'])
    K = int(request.form['K'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    city = request.form['city']

    weather = get_weather(city)
    temp = weather["temperature"]
    humidity = weather["humidity"]

    # Crop prediction
    crop = predict_crop([N, P, K, temp, humidity, ph, rainfall])

    # Fertilizer
    fertilizer = recommend_fertilizer(N, P, K)

    # Image upload
    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    disease = detect_disease(filepath)

    ndvi = calculate_ndvi()

    return f"""
    🌾 Crop: {crop} <br>
    🧪 Fertilizer: {fertilizer} <br>
    📷 Disease: {disease} <br>
    🌦️ Weather: Temp {temp}°C, Humidity {humidity}% <br>
    📡 {ndvi}
    """

if __name__ == "__main__":
    app.run(debug=True)