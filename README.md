# Proyek Analisis Data: E-Commerce Brazil - Analisis Pasar & Kinerja Produk

## Latar Belakang

Proyek ini merupakan submission akhir untuk kelas Analisis Data dengan Python oleh Dicoding. Tujuan dari proyek ini adalah untuk melakukan analisis mendalam pada E-Commerce Public Dataset, sebuah kumpulan data transaksional dari salah satu e-commerce terbesar di Brazil. Analisis ini berfokus pada pemahaman dinamika pasar berdasarkan geografi dan evaluasi kinerja kategori produk berdasarkan pendapatan serta kepuasan pelanggan.

## Pertanyaan Bisnis yang Dianalisis

1.  **Di kota mana saja konsentrasi pelanggan dan penjual tertinggi, dan bagaimana perbandingan keduanya?**
2.  **Kategori produk apa yang menghasilkan pendapatan terbesar sekaligus memiliki skor ulasan (review score) rata-rata tertinggi?**
3.  **Bagaimana segmentasi pelanggan berdasarkan perilaku transaksi (Recency, Frequency, Monetary) untuk mengidentifikasi kelompok pelanggan paling bernilai?**

## Struktur Proyek

Proyek ini disusun dengan struktur direktori sebagai berikut untuk kemudahan navigasi dan eksekusi:

```
submission/
├── dashboard/
│   └── dashboard.py
├── data/
│   └── all_data.csv
├── notebook.ipynb
├── README.md
└── requirements.txt
```

- **dashboard/**: Berisi skrip Streamlit untuk visualisasi data.
- **data/**: Berisi dataset bersih (`all_data.csv`) yang dihasilkan dari notebook analisis.
- **notebook.ipynb**: Berisi seluruh proses analisis data, mulai dari data wrangling hingga pembuatan visualisasi untuk menjawab pertanyaan bisnis.
- **README.md**: Dokumentasi proyek.
- **requirements.txt**: Daftar library Python yang dibutuhkan.

## Setup Environment

Untuk menjalankan proyek ini secara lokal, Anda perlu menginstal semua library yang dibutuhkan.

1.  Buat sebuah virtual environment (opsional, namun sangat disarankan).
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk pengguna Linux/macOS
    .\venv\Scripts\activate    # Untuk pengguna Windows
    ```
2.  Install semua library yang ada di `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## Cara Menjalankan Proyek

Proyek ini terdiri dari dua bagian utama: notebook analisis dan dashboard interaktif.

### 1. Menjalankan Notebook Analisis
Buka dan jalankan file `notebook.ipynb` (atau nama file notebook Anda) menggunakan Jupyter Notebook atau Google Colab. Pastikan untuk menjalankan semua sel dari awal hingga akhir. Proses ini akan menghasilkan file `all_data.csv` yang akan digunakan oleh dashboard.

### 2. Menjalankan Dashboard Streamlit
Setelah `all_data.csv` berhasil dibuat, jalankan dashboard dengan perintah berikut di terminal Anda:

```bash
streamlit run dashboard.py
```

Setelah perintah dijalankan, dashboard akan terbuka secara otomatis di browser Anda.

## Live Dashboard
Dashboard interaktif untuk proyek ini dapat diakses melalui tautan berikut:
[Dashboard Analisis E-Commerce](https://submissionpythondbs.streamlit.app/)

## Penulis

- **Nama:** Bivandira Aurel Maha Dewa
- **Email:** bivandiraaurel@gmail.com
- **ID Dicoding:** bivandira17