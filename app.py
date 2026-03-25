from flask import Flask, render_template, request, jsonify

# Import your modules
from models.crop_model import predict_crop
from models.fertilizer import recommend_fertilizer
from utils.weather import get_weather
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app = Flask(__name__)

# 🔹 Home route (VERY IMPORTANT)
@app.route('/')
def home():
    return render_template("index.html")

# 🔹 Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    N = int(data['N'])
    P = int(data['P'])
    K = int(data['K'])
    ph = float(data['ph'])
    rainfall = float(data['rainfall'])
    city = data['city']

    weather = get_weather(city)
    temp = weather["temperature"]
    humidity = weather["humidity"]

    crop = predict_crop([N, P, K, temp, humidity, ph, rainfall])
    fertilizer = recommend_fertilizer(N, P, K)

    return jsonify({
        "crop": crop,
        "fertilizer": fertilizer,
        "disease": "Healthy",
        "temperature": temp,
        "humidity": humidity
    })

# 🔹 Run app
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)