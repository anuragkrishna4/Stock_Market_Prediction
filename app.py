from flask import Flask, render_template, request, jsonify
from model import predict_stock  # Import prediction function

app = Flask(__name__)
#CORS(app)  # Enable CORS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        days = int(request.form["days"])
        prediction = predict_stock(days)
        return jsonify({"prediction": float(prediction)})  # Convert to standard float
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
