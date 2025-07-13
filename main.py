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

### Fitur:
- **Input**: Permintaan tahunan, biaya pemesanan, dan biaya penyimpanan
- **Output**: EOQ, total biaya persediaan, jumlah pemesanan per tahun
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
biaya_total_persediaan = EOQ / 2 * H + (D / EOQ) * S

# Output hasil
st.subheader("Hasil Perhitungan EOQ")
st.write(f"**Jumlah Pemesanan Optimal (EOQ)**: {EOQ:.2f} unit")
st.write(f"**Jumlah Pemesanan per Tahun**: {jumlah_order_per_tahun:.2f} kali")
st.write(f"**Total Biaya Persediaan**: Rp {biaya_total_persediaan:,.2f}")

# Grafik EOQ
st.subheader("Grafik Biaya Total vs Kuantitas Order")
order_qty_range = np.arange(1, D + 1)
holding_cost = (order_qty_range / 2) * H
ordering_cost = (D / order_qty_range) * S
total_cost = holding_cost + ordering_cost

fig, ax = plt.subplots(figsize=(10, 5))

# Plot Total Cost
ax.plot(order_qty_range, total_cost, label='Total Biaya', color='blue')
ax.scatter(order_qty_range, total_cost, color='blue', s=10)

# Plot Holding Cost
ax.plot(order_qty_range, holding_cost, '--', label='Biaya Penyimpanan', color='green')
ax.scatter(order_qty_range, holding_cost, color='green', s=10)

# Plot Ordering Cost
ax.plot(order_qty_range, ordering_cost, '--', label='Biaya Pemesanan', color='red')
ax.scatter(order_qty_range, ordering_cost, color='red', s=10)

# Garis EOQ
ax.axvline(EOQ, color='orange', linestyle=':', label=f'EOQ ≈ {EOQ:.0f}')

# Label dan grid
ax.set_xlabel('Jumlah Order per Kali Pesan (unit)')
ax.set_ylabel('Biaya (Rp)')
ax.set_title('Analisis Biaya Persediaan terhadap Kuantitas Order')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

st.pyplot(fig)
