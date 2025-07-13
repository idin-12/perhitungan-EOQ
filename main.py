# EOQ Calculator App
# Simulasi sistem persediaan barang menggunakan model EOQ

import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="EOQ Calculator", layout="centered")

# Judul aplikasi
st.title("Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.write("""
### Deskripsi:
Simulasi ini digunakan untuk menghitung jumlah pemesanan optimal berdasarkan permintaan tahunan,
biaya pemesanan, dan biaya penyimpanan per unit.

### Rumus EOQ:
\[ EOQ = \sqrt{\frac{2DS}{H}} \]

**Dimana:**
- D = Permintaan Tahunan (unit)
- S = Biaya Pemesanan per Order (Rp)
- H = Biaya Penyimpanan per Unit per Tahun (Rp)

### Fitur:
- **Input**: Permintaan tahunan, biaya pemesanan, dan biaya penyimpanan
- **Output**: EOQ, total biaya persediaan, jumlah pemesanan per tahun, rincian biaya
- **Konsep**: Inventory Model – EOQ formula
""")

# Input pengguna
st.sidebar.header("Input Parameter")
D = st.sidebar.number_input("Permintaan Tahunan (unit)", min_value=1, value=1000)
S = st.sidebar.number_input("Biaya Pemesanan per Order (Rp)", min_value=1, value=50000)
H = st.sidebar.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1, value=2000)

# Hitung EOQ
def hitung_eoq(D, S, H):
    return math.sqrt((2 * D * S) / H)

EOQ = hitung_eoq(D, S, H)
jumlah_order_per_tahun = D / EOQ

# Hitung rincian biaya
biaya_pemesanan_total = jumlah_order_per_tahun * S
biaya_penyimpanan_total = (EOQ / 2) * H
biaya_total_persediaan = biaya_pemesanan_total + biaya_penyimpanan_total

# Output hasil
st.subheader("Hasil Perhitungan EOQ")
st.write(f"📦 **Jumlah Pemesanan Optimal (EOQ)**: {EOQ:.2f} unit")
st.write(f"🔁 **Jumlah Pemesanan per Tahun**: {jumlah_order_per_tahun:.2f} kali")
st.write(f"💰 **Total Biaya Persediaan**: Rp {biaya_total_persediaan:,.2f}")

# Rincian biaya
st.subheader("Rincian Biaya Persediaan")
st.write(f"📝 **Biaya Pemesanan Total**: Rp {biaya_pemesanan_total:,.2f}")
st.write(f"🏬 **Biaya Penyimpanan Total**: Rp {biaya_penyimpanan_total:,.2f}")

# Grafik EOQ dengan titik koordinat
st.subheader("Grafik Biaya Total vs Kuantitas Order")
order_qty_range = np.arange(1, D + 1)
holding_cost = (order_qty_range / 2) * H
ordering_cost = (D / order_qty_range) * S
total_cost = holding_cost + ordering_cost

fig, ax = plt.subplots(figsize=(10, 5))

# Plot Total Cost dengan titik koordinat
ax.plot(order_qty_range, total_cost, label='Total Biaya', color='blue')
ax.scatter(order_qty_range, total_cost, color='blue', s=10)

# Plot Holding Cost dengan titik koordinat
ax.plot(order_qty_range, holding_cost, '--', label='Biaya Penyimpanan', color='green')
ax.scatter(order_qty_range, holding_cost, color='green', s=10)

# Plot Ordering Cost dengan titik koordinat
ax.plot(order_qty_range, ordering_cost, '--', label='Biaya Pemesanan', color='red')
ax.scatter(order_qty_range, ordering_cost, color='red', s=10)

# Garis EOQ
ax.axvline(EOQ, color='orange', linestyle=':', label=f'EOQ ≈ {EOQ:.0f}')

# Penambahan anotasi pada EOQ
ax.annotate(f'EOQ = {EOQ:.0f} unit',
            xy=(EOQ, biaya_total_persediaan),
            xytext=(EOQ + D*0.05, biaya_total_persediaan),
            arrowprops=dict(facecolor='orange', shrink=0.05),
            fontsize=9, color='black')

# Label dan grid
ax.set_xlabel('Jumlah Order per Kali Pesan (unit)')
ax.set_ylabel('Biaya (Rp)')
ax.set_title('Analisis Biaya Persediaan terhadap Kuantitas Order')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

st.pyplot(fig)

# Interpretasi hasil
st.subheader("Interpretasi")
st.markdown(f"""
Dengan hasil perhitungan:
- **EOQ = {EOQ:.2f} unit**, artinya perusahaan sebaiknya memesan barang sebanyak ini setiap kali melakukan pemesanan.
- **Jumlah pemesanan per tahun = {jumlah_order_per_tahun:.2f} kali**, yaitu frekuensi pembelian untuk memenuhi permintaan tahunan.
- **Total biaya persediaan = Rp {biaya_total_persediaan:,.2f}**, yang terdiri dari:
  - **Biaya Pemesanan Total**: Rp {biaya_pemesanan_total:,.2f}
  - **Biaya Penyimpanan Total**: Rp {biaya_penyimpanan_total:,.2f}

**Kesimpulan:**  
Model EOQ membantu perusahaan dalam menentukan **jumlah pembelian optimal** sehingga biaya total persediaan berada pada titik minimum.
""")

st.markdown("---")
st.caption("Dibuat untuk simulasi EOQ dalam sistem manajemen persediaan.")
