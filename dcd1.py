import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
china_df = pd.read_csv('all_data.csv')

# Memfilter data untuk stasiun Tiantan
tiantan_df = china_df[china_df['station'] == 'Tiantan']
tiantan_2013 = tiantan_df[tiantan_df['year'] == 2013]
tiantan_2013_maret = tiantan_2013[tiantan_2013['month'] == 3]

# Mengelompokkan data perubahan konsentrasi PM2.5 dari hari ke hari
tiantan_2013_maret_grouped = tiantan_2013_maret.groupby('day').mean(numeric_only=True)

# Membuat plot dengan ukuran dan dpi yang diatur
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.plot(tiantan_2013_maret_grouped['PM2.5'], label='PM2.5', color='blue', linewidth=2)

# Mengatur label dan judul
ax.set_xlabel('Hari', fontsize=12)
ax.set_ylabel('Konsentrasi PM2.5', fontsize=12)
ax.set_title('Perubahan Konsentrasi PM2.5 di Tiantan (Maret 2013)', fontsize=14)
ax.legend(fontsize=10)

# Menampilkan plot dengan Streamlit
st.pyplot(fig)

# Memfilter data untuk stasiun Wanliu
wanliu_df = china_df[china_df['station'] == 'Wanliu']
wanliu_2015 = wanliu_df[wanliu_df['year'] == 2015]

# Mengelompokkan data Wanliu berdasarkan bulan dan menghitung rata-rata tiap polutan
wanliu_2015_grouped = wanliu_2015.groupby('month').mean(numeric_only=True)

# Membuat plot dengan ukuran dan dpi yang diatur
fig2, ax2 = plt.subplots(figsize=(10, 6), dpi=100)
ax2.plot(wanliu_2015_grouped['PM2.5'], label='PM2.5', color='blue', linewidth=2)
ax2.plot(wanliu_2015_grouped['PM10'], label='PM10', color='orange', linewidth=2)
ax2.plot(wanliu_2015_grouped['SO2'], label='SO2', color='green', linewidth=2)
ax2.plot(wanliu_2015_grouped['NO2'], label='NO2', color='red', linewidth=2)
ax2.plot(wanliu_2015_grouped['O3'], label='O3', color='purple', linewidth=2)

# Mengatur label dan judul
ax2.set_xlabel('Bulan', fontsize=12)
ax2.set_ylabel('Konsentrasi Polutan', fontsize=12)
ax2.set_title('Tren Kualitas Udara di Wanliu (2015)', fontsize=14)
ax2.legend(fontsize=10)

# Menampilkan plot dengan Streamlit
st.pyplot(fig2)
