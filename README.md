#Stock Market Prediction

This project predicts stock prices using LSTM (Long Short-Term Memory) and Linear Regression models. The application fetches historical stock market data, processes it, trains models, and visualizes predictions through a Flask-based web interface.


📌 Features:


📊 Fetches historical stock data from Yahoo Finance using yfinance

🔍 Preprocesses stock data for training

🧠 Implements Linear Regression and LSTM for stock price prediction

📈 Visualizes predicted stock prices with graphs

🌐 Deploys the model using Flask for real-time predictions


📥 Dataset (Fetching Stock Data)


We fetch historical stock data using yfinance. For this project, we are using NVIDIA (NVDA) stock data from:


Start Date: 2014-01-01

End Date: 2024-05-31

Stock Symbol: NVDA


🚀 Technologies Used:


Python

Flask (for web deployment)

TensorFlow/Keras (for LSTM)

Scikit-learn (for Linear Regression)

Matplotlib & Seaborn (for data visualization)

yfinance (for stock data retrieval)

Pandas & NumPy (for data processing)
