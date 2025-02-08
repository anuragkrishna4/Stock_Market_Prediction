from tensorflow.keras.models import load_model
import numpy as np

# Load LSTM model
lstm_model = load_model("C:\\Users\\KIIT\\OneDrive\\Desktop\\AD Lab\\stock_prediction_project\\lstm_model.h5")

def predict_stock(data):
    data = np.array(data).reshape(1, -1)
    prediction = lstm_model.predict(data)[0][0]
    return round(prediction, 2)
