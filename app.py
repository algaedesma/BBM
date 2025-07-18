# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M9KEPyLQ2zDThiBgNpd-siZfiLp1jYUj
"""

import streamlit as st
import pandas as pd
import joblib

# Load model pipeline
model_pipeline = joblib.load("model_fuel.pkl")

st.title("🚘 Prediksi Biaya Bahan Bakar Tahunan di Indonesia 🇮🇩")
st.write("Masukkan data kendaraan untuk prediksi biaya bahan bakar tahunan (Rp).")

# Input dari user
year = st.number_input("Tahun Kendaraan", min_value=1980, max_value=2025, value=2015)
engine_cylinders = st.selectbox("Jumlah Silinder Mesin", options=[2, 3, 4, 5, 6, 8])
engine_displacement = st.number_input("Kapasitas Mesin (Liter)", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
fuel_type = st.selectbox("Jenis Bahan Bakar", options=["Regular", "Premium", "Diesel", "Electricity"])
vehicle_class = st.selectbox("Kelas Kendaraan", options=["Compact", "SUV", "Sedan", "Pickup", "Minivan"])

# Buat dataframe input
user_input = pd.DataFrame({
    "year": [year],
    "engine_cylinders": [engine_cylinders],
    "engine_displacement": [engine_displacement],
    "fuel_type": [fuel_type],
    "vehicle_class": [vehicle_class]
})

# Prediksi
if st.button("Prediksi"):
    try:
        prediction = model_pipeline.predict(user_input)[0]
        st.success(f"💸 Estimasi Biaya BBM per Tahun: **Rp {prediction:,.0f}**")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")