import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----- KONFIGURASI HALAMAN -----
st.set_page_config(
    page_title="Dashboard Analisis E-Commerce",
    page_icon="📊",
    layout="wide"
)

# ----- FUNGSI-FUNGSI BANTU -----

# Menggunakan cache agar data hanya dimuat sekali
@st.cache_data
def load_data():
    # Menggunakan 'all_data.csv' sesuai instruksi
    df = pd.read_csv("all_data.csv")
    # Mengubah kolom tanggal jika belum dalam format datetime
    date_cols = ["order_purchase_timestamp", "order_delivered_customer_date", "order_estimated_delivery_date"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])
    return df

# Fungsi untuk plot perbandingan pelanggan vs. penjual
def create_customer_seller_plot(df):
    top_10_customer_cities = df.groupby('customer_city')['customer_unique_id'].nunique().nlargest(10).reset_index()
    top_10_seller_cities = df.groupby('seller_city')['seller_id'].nunique().nlargest(10).reset_index()
    
    fig, axes = plt.subplots(1, 2, figsize=(22, 8))
    sns.set_style("whitegrid")
    
    # Plot Pelanggan
    sns.barplot(x='customer_unique_id', y='customer_city', data=top_10_customer_cities, palette='viridis', ax=axes[0])
    axes[0].set_title('Top 10 Kota dengan Pelanggan Terbanyak', fontsize=16)
    axes[0].set_xlabel('Jumlah Pelanggan Unik', fontsize=12)
    axes[0].set_ylabel('Kota', fontsize=12)
    for index, value in enumerate(top_10_customer_cities['customer_unique_id']):
        axes[0].text(value, index, f' {value}', va='center')

    # Plot Penjual
    sns.barplot(x='seller_id', y='seller_city', data=top_10_seller_cities, palette='plasma', ax=axes[1])
    axes[1].set_title('Top 10 Kota dengan Penjual Terbanyak', fontsize=16)
    axes[1].set_xlabel('Jumlah Penjual Unik', fontsize=12)
    axes[1].set_ylabel('')
    for index, value in enumerate(top_10_seller_cities['seller_id']):
        axes[1].text(value, index, f' {value}', va='center')
        
    plt.suptitle('Perbandingan Konsentrasi Pelanggan vs. Penjual', fontsize=20, fontweight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig

# Fungsi untuk plot pendapatan vs. ulasan
def create_revenue_review_plot(df):
    category_performance = df.groupby('product_category_name_english').agg({
        'price': 'sum',
        'review_score': 'mean',
        'order_id': 'nunique'
    }).reset_index()
    category_performance = category_performance[category_performance['order_id'] > 50]
    top_10_revenue_categories = category_performance.nlargest(10, 'price').sort_values(by='price', ascending=False)

    fig, ax1 = plt.subplots(figsize=(14, 10))
    sns.set_style("whitegrid")

    sns.barplot(x='price', y='product_category_name_english', data=top_10_revenue_categories, palette='coolwarm', ax=ax1)
    ax1.set_title('Top 10 Kategori: Pendapatan vs. Rata-rata Skor Ulasan', fontsize=18)
    ax1.set_xlabel('Total Pendapatan (Revenue)', fontsize=14)
    ax1.set_ylabel('Kategori Produk', fontsize=14)
    
    ax2 = ax1.twiny()
    sns.lineplot(x='review_score', y='product_category_name_english', data=top_10_revenue_categories, color='gold', marker='o', markersize=8, ax=ax2)
    ax2.set_xlabel('Rata-rata Skor Ulasan (1-5)', fontsize=14, color='gold')
    ax2.tick_params(axis='x', labelcolor='gold')
    ax2.set_xlim(3.8, 4.5)
    ax2.grid(False)
    return fig

# ----- MEMUAT DATA -----
all_data = load_data()


# ----- SIDEBAR -----
with st.sidebar:
    st.image("https://storage.googleapis.com/dicoding-cdn-prod/uploads/companies/logos/dicoding-logo.png", width=200) # Ganti dengan logo Anda jika ada
    st.header("Filter Data")
    
    # Filter berdasarkan rentang tanggal
    min_date = all_data["order_purchase_timestamp"].min().date()
    max_date = all_data["order_purchase_timestamp"].max().date()
    
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data berdasarkan tanggal yang dipilih
main_df = all_data[
    (all_data["order_purchase_timestamp"].dt.date >= start_date) &
    (all_data["order_purchase_timestamp"].dt.date <= end_date)
]


# ----- HALAMAN UTAMA -----
st.title('📊 Dashboard Analisis E-Commerce')
st.write("Dashboard ini menampilkan analisis data dari E-Commerce Public Dataset.")

# --- METRIK UTAMA ---
st.header("Ringkasan Kinerja")
col1, col2, col3 = st.columns(3)

with col1:
    total_revenue = main_df['price'].sum()
    st.metric("Total Pendapatan", value=f"R$ {total_revenue:,.2f}")

with col2:
    total_orders = main_df['order_id'].nunique()
    st.metric("Total Pesanan", value=f"{total_orders:,}")

with col3:
    avg_review_score = main_df['review_score'].mean()
    st.metric("Rata-rata Skor Ulasan", value=f"{avg_review_score:.2f} ⭐")


# --- VISUALISASI DATA ---
st.header("Analisis Mendalam")

# Visualisasi 1: Perbandingan Geografis
st.subheader("Perbandingan Konsentrasi Pelanggan vs. Penjual")
st.write("Analisis ini membandingkan 10 kota teratas berdasarkan jumlah pelanggan dan penjual unik. Ini membantu mengidentifikasi di mana basis pelanggan terbesar berada versus di mana persaingan penjual paling ketat.")
fig1 = create_customer_seller_plot(main_df)
st.pyplot(fig1)

# Visualisasi 2: Kinerja Kategori Produk
st.subheader("Analisis Kinerja Kategori Produk (Pendapatan vs. Kepuasan)")
st.write("Visualisasi di bawah ini menampilkan 10 kategori produk dengan pendapatan tertinggi, sekaligus menunjukkan rata-rata skor kepuasan pelanggan untuk setiap kategori tersebut.")
fig2 = create_revenue_review_plot(main_df)
st.pyplot(fig2)


st.caption('Copyright (c) 2024 - Bivandira Aurel Maha Dewa')