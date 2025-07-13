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
Aplikasi ini menghitung **jumlah pemesanan optimal (EOQ)**, total biaya pemesanan, biaya penyimpanan, dan total biaya persediaan secara lengkap.

### Rumus EOQ:
\[ EOQ = \sqrt{\frac{2DS}{H}} \]

**Dimana:**
- D = Permintaan Tahunan (unit)
- S = Biaya Pemesanan per Order (Rp)
- H = Biaya Penyimpanan per Unit per Tahun (Rp)

### Fitur:
- **Input**: Permintaan tahunan, biaya pemesanan, dan biaya penyimpanan
- **Output**: EOQ, biaya pemesanan per order, biaya penyimpanan per unit per tahun, total biaya pemesanan per tahun, total biaya penyimpanan per tahun, total biaya persediaan, jumlah pemesanan per tahun
- **Grafik**: Menampilkan titik koordinat dan keterangan EOQ
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

# Biaya per order dan per unit per tahun (input dasar)
st.subheader("Biaya Dasar")
st.write(f"📝 **Biaya Pemesanan per Order**: Rp {S:,.2f}")
st.write(f"🏬 **Biaya Penyimpanan per Unit per Tahun**: Rp {H:,.2f}")

# Rincian biaya total
st.subheader("Rincian Biaya Persediaan per Tahun")
st.write(f"📝 **Total Biaya Pemesanan**: Rp {biaya_pemesanan_total:,.2f}")
st.write(f"🏬 **Total Biaya Penyimpanan**: Rp {biaya_penyimpanan_total:,.2f}")
st.write(f"💰 **Total Biaya Persediaan (Pemesanan + Penyimpanan)**: Rp {biaya_total_persediaan:,.2f}")

# Grafik EOQ dengan titik koordinat dan keterangan EOQ
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

# Garis EOQ dan titik EOQ spesifik
ax.axvline(EOQ, color='orange', linestyle=':', label=f'EOQ ≈ {EOQ:.0f}')
ax.scatter(EOQ, biaya_total_persediaan, color='orange', s=50, marker='X', label='Titik EOQ Optimal')

# Penambahan anotasi pada EOQ
ax.annotate(f'EOQ = {EOQ:.0f} unit\nTotal Cost = Rp {biaya_total_persediaan:,.0f}',
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
- **EOQ = {EOQ:.2f} unit**, artinya perusahaan sebaiknya memesan barang sebanyak ini setiap kali melakukan pemesanan untuk **meminimalkan total biaya persediaan**.
- **Jumlah pemesanan per tahun = {jumlah_order_per_tahun:.2f} kali**, yaitu frekuensi pembelian.
- **Biaya Pemesanan per Order**: Rp {S:,.2f}
- **Biaya Penyimpanan per Unit per Tahun**: Rp {H:,.2f}
- **Total biaya pemesanan = Rp {biaya_pemesanan_total:,.2f}**
- **Total biaya penyimpanan = Rp {biaya_penyimpanan_total:,.2f}**
- **Total biaya persediaan = Rp {biaya_total_persediaan:,.2f}**

📊 **Grafik di atas menunjukkan:**
- Titik **EOQ (marker X orange)** adalah jumlah order dengan total biaya terendah.
- **Kurva biru**: Total biaya persediaan.
- **Kurva merah**: Biaya pemesanan.
- **Kurva hijau**: Biaya penyimpanan.
- Garis vertikal orange menunjukkan posisi EOQ optimal.
""")

st.markdown("---")
st.caption("Dibuat untuk simulasi EOQ dalam sistem manajemen persediaan.")
