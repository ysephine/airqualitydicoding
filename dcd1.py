import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Memuat dataset
def load_data():
    return pd.read_csv('all_data.csv')

china_df = load_data()

# Judul dashboard
st.title('Dashboard Kualitas Udara di Tiantan dan Wanliu')

# Pertanyaan 1: Perubahan Konsentrasi PM2.5 dari Hari ke Hari di Tiantan pada Maret 2013
st.header('Perubahan Konsentrasi PM2.5 di Tiantan (Maret 2013)')

# Memfilter data untuk stasiun Tiantan dan tahun 2013
tiantan_df = china_df[china_df['station'] == 'Tiantan']
tiantan_2013 = tiantan_df[tiantan_df['year'] == 2013]
tiantan_2013_march = tiantan_2013[tiantan_2013['month'] == 3]

# Mengelompokkan data perubahan konsentrasi PM2.5 dari hari ke hari di Tiantan pada Maret 2013
tiantan_2013_march_grouped = tiantan_2013_march.groupby('day').mean(numeric_only=True)

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(tiantan_2013_march_grouped['PM2.5'], label='PM2.5')
ax.set_xlabel('Hari')
ax.set_ylabel('Konsentrasi PM2.5')
ax.set_title('Perubahan Konsentrasi PM2.5 di Tiantan (Maret 2013)')
ax.legend()

st.pyplot(fig)

# Pertanyaan 2: Tren Kualitas Udara di Wanliu pada Tahun 2015
st.header('Tren Kualitas Udara di Wanliu (Tahun 2015)')

# Memfilter data untuk stasiun Wanliu dan tahun 2015
wanliu_df = china_df[china_df['station'] == 'Wanliu']
wanliu_2015 = wanliu_df[wanliu_df['year'] == 2015]

# Mengelompokkan data Wanliu berdasarkan bulan dan menghitung rata-rata tiap polutan
wanliu_2015_grouped = wanliu_2015.groupby('month').mean(numeric_only=True)

# Visualisasi tren polutan di Wanliu tahun 2015
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(wanliu_2015_grouped['PM2.5'], label='PM2.5')
ax2.plot(wanliu_2015_grouped['PM10'], label='PM10')
ax2.plot(wanliu_2015_grouped['SO2'], label='SO2')
ax2.plot(wanliu_2015_grouped['NO2'], label='NO2')
ax2.plot(wanliu_2015_grouped['O3'], label='O3')
ax2.set_xlabel('Bulan')
ax2.set_ylabel('Konsentrasi Polutan')
ax2.set_title('Tren Kualitas Udara di Wanliu (Tahun 2015)')
ax2.legend()

st.pyplot(fig2)
