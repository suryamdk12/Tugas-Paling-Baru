from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Fungsi untuk memuat dan memproses data
def load_and_process_data():
    # Membaca data dari CSV
    df = pd.read_csv('investasi_saham.csv')

    # Pembersihan data: menghapus baris dengan nilai NaN
    df.dropna(inplace=True)

    # Normalisasi data
    scaler = StandardScaler()
    features = df[['open_price', 'close', 'volume', 'market_cap']]  # Ganti dengan kolom yang relevan
    scaled_features = scaler.fit_transform(features)

    # Memisahkan data latih dan data uji
    X_train, X_test = train_test_split(scaled_features, test_size=0.2, random_state=42)

    return X_train, X_test, df['stock_symbol']

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    initial_price = data['initialPrice']
    final_price = data['finalPrice']
    market_volume = data['marketVolume']

    # Memuat dan memproses data
    X_train, X_test, stock_symbols = load_and_process_data()

    # K-Means Clustering
    kmeans = KMeans(n_clusters=3)  # Misalnya kita ingin 3 cluster
    kmeans.fit(X_train)

    # Prediksi untuk data uji
    prediction = kmeans.predict(X_test)

    # Mencari cluster untuk data uji yang sesuai dengan investasi
    normalized_investment = scaler.transform([[initial_price, market_volume, 0]])  # Normalisasi sesuai fitur
    cluster_prediction = kmeans.predict(normalized_investment)

    # Membuat grafik
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=prediction, cmap='viridis', marker='o', label='Data Uji')
    plt.scatter(normalized_investment[0][0], normalized_investment[0][1], c='red', marker='x', s=200, label='Investasi')
    plt.title('Hasil Clustering K-Means')
    plt.xlabel('Fitur 1 (misalnya Price)')
    plt.ylabel('Fitur 2 (misalnya Volume)')
    plt.legend()
    
    # Simpan grafik sebagai file gambar
    image_path = 'static/cluster_plot.png'
    plt.savefig(image_path)
    plt.close()

    # Kembalikan path gambar
    return jsonify({
        'cluster': int(cluster_prediction[0]),
        'stock_symbol': stock_symbol,
        'image_path': image_path
    })

if __name__ == '__main__':
    # Pastikan folder static ada
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(port=5000)