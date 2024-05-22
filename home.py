import streamlit as st
import pandas as pd
from function import load_data

def app():
    # Judul dan Informasi mengenai Dasboard
    st.title("Dashboard Pemantauan dan Prediksi Banjir Berbasis Curah Hujan di Kabupaten Cilacap :thunder_cloud_and_rain:")
    st.write("Selamat datang di Dashboard Pemantauan dan Prediksi Banjir Berbasis Curah Hujan di **Kabupaten Cilacap**! "
            "Kabupaten Cilacap, Jawa Tengah, sering mengalami masalah banjir, khususnya dalam rentang waktu tahun 2020-2023. " 
            "Dengan menggabungkan data kejadian banjir dari **BNPB** dan informasi curah hujan harian dari **WorldWeatherOnline**, " 
            "kami menciptakan solusi prediktif berupa dashboard ini. Kami menganalisis curah hujan, membuat model forecast,"
            "dan memvisualisasikannya agar dapat memberikan pemahaman yang lebih baik mengenai potensi risiko banjir. " 
            "Dengan fitur-fitur seperti data historis, forecast, dan prediksi kejadian banjir, kami berharap " 
            "dashboard ini dapat menjadi alat yang berguna dalam menghadapi tantangan banjir di **Kabupaten Cilacap**."
            )
    st.info("Semua data curah hujan diukur dalam satuan mm/jam.")

     # Load Dataset
    df = load_data("data/train.csv")
    st.write(df)
