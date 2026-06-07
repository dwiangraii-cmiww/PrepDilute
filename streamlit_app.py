import streamlit as st

# ==========================================
# KONFIGURASI & DATA
# ==========================================

st.set_page_config(
    page_title="Kalkulator Kimia",
    page_icon="⚗️",
    layout="centered"
)

# Custom CSS untuk warna dan tampilan
st.markdown("""
<style>
    .stApp {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e3a8a;
        text-align: center;
    }
    .info-box {
        background-color: #dbeafe;
        border-left: 4px solid #3b82f6;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .rumus-box {
        background-color: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .referensi-box {
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .unsur-card {
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    section[data-testid="stSidebar"] {
        background-color: #f1f5f9;
    }
</style>
""", unsafe_allow_html=True)

# Data Unsur Periodik (Sumber: IUPAC 2024)
UNSUR = {
    "H": {"nomor": 1, "nama": "Hidrogen", "massa": 1.008, "golongan": "Non-logam", "warna": "#FF6B6B"},
    "He": {"nomor": 2, "nama": "Helium", "massa": 4.0026, "golongan": "Gas mulia", "warna": "#FFE66D"},
    "Li": {"nomor": 3, "nama": "Litium", "massa": 6.94, "golongan": "Logam alkali", "warna": "#FF8C42"},
    "Be": {"nomor": 4, "nama": "Berilium", "massa": 9.0122, "golongan": "Logam alkali tanah", "warna": "#4ECDC4"},
    "B": {"nomor": 5, "nama": "Boron", "massa": 10.81, "golongan": "Metaloid", "warna": "#95E1D3"},
    "C": {"nomor": 6, "nama": "Karbon", "massa": 12.011, "golongan": "Non-logam", "warna": "#2C3E50"},
    "N": {"nomor": 7, "nama": "Nitrogen", "massa": 14.007, "golongan": "Non-logam", "warna": "#3498DB"},
    "O": {"nomor": 8, "nama": "Oksigen", "massa": 15.999, "golongan": "Non-logam", "warna": "#E74C3C"},
    "F": {"nomor": 9, "nama": "Fluor", "massa": 18.998, "golongan": "Halogen", "warna": "#9B59B6"},
    "Ne": {"nomor": 10, "nama": "Neon", "massa": 20.180, "golongan": "Gas mulia", "warna": "#F39C12"},
    "Na": {"nomor": 11, "nama": "Natrium", "massa": 22.990, "golongan": "Logam alkali", "warna": "#E67E22"},
    "Mg": {"nomor": 12, "nama": "Magnesium", "massa": 24.305, "golongan": "Logam alkali tanah", "warna": "#27AE60"},
    "Al": {"nomor": 13, "nama": "Aluminium", "massa": 26.982, "golongan": "Logam pasca-transisi", "warna": "#95A5A6"},
    "Si": {"nomor": 14, "nama": "Silikon", "massa": 28.085, "golongan": "Metaloid", "warna": "#7F8C8D"},
    "P": {"nomor": 15, "nama": "Fosfor", "massa": 30.974, "golongan": "Non-logam", "warna": "#E74C3C"},
    "S": {"nomor": 16, "nama": "Belerang", "massa": 32.06, "golongan": "Non-logam", "warna": "#F1C40F"},
    "Cl": {"nomor": 17, "nama": "Klor", "massa": 35.45, "golongan": "Halogen", "warna": "#1ABC9C"},
    "Ar": {"nomor": 18, "nama": "Argon", "massa": 39.948, "golongan": "Gas mulia", "warna": "#8E44AD"},
    "K": {"nomor": 19, "nama": "Kalium", "massa": 39.098, "golongan": "Logam alkali", "warna": "#D35400"},
    "Ca": {"nomor": 20, "nama": "Kalsium", "massa": 40.078, "golongan": "Logam alkali tanah", "warna": "#2ECC71"},
    "Fe": {"nomor": 26, "nama": "Besi", "massa": 55.845, "golongan": "Logam transisi", "warna": "#CD6133"},
    "Cu": {"nomor": 29, "nama": "Tembaga", "massa": 63.546, "golongan": "Logam transisi", "warna": "#E67E22"},
    "Zn": {"nomor": 30, "nama": "Seng", "massa": 65.38, "golongan": "Logam transisi", "warna": "#BDC3C7"},
    "Br": {"nomor": 35, "nama": "Brom", "massa": 79.904, "golongan": "Halogen", "warna": "#922B21"},
    "Ag": {"nomor": 47, "nama": "Perak", "massa": 107.87, "golongan": "Logam transisi", "warna": "#ECF0F1"},
    "I": {"nomor": 53, "nama": "Iodium", "massa": 126.90, "golongan": "Halogen", "warna": "#4A235A"},
    "Au": {"nomor": 79, "nama": "Emas", "massa": 196.97, "golongan": "Logam transisi", "warna": "#F7DC6F"},
    "Hg": {"nomor": 80, "nama": "Raksa", "massa": 200.59, "golongan": "Logam transisi", "warna": "#7F8C8D"},
    "Pb": {"nomor": 82, "nama": "Timbal", "massa": 207.2, "golongan": "Logam pasca-transisi", "warna": "#566573"}
}

# ==========================================
# INISIALISASI SESSION STATE
# ==========================================

if 'riwayat' not in st.session_state:
    st.session_state.riwayat = []

# ==========================================
# FUNGSI-FUNGSI LOGIKA
# ==========================================

def simpan_riwayat(data):
    st.session_state.riwayat.insert(0, data)

def hapus_riwayat():
    st.session_state.riwayat = []

def hitung_larutan(mr, volume, molaritas):
    if mr <= 0 or volume <= 0 or molaritas <= 0:
        return None
    massa = molaritas * (volume / 1000) * mr
    return massa

def hitung_v2(m1, v1, m2):
    if m1 <= 0 or v1 <= 0 or m2 <= 0:
        return None
    v2 = (m1 * v1) / m2
    return v2

def hitung_v1(m1, m2, v2):
    if m1 <= 0 or m2 <= 0 or v2 <= 0:
        return None
    v1 = (m2 * v2) / m1
    return v1

def hitung_m2(m1, v1, v2):
    if m1 <= 0 or v1 <= 0 or v2 <= 0:
        return None
    m2 = (m1 * v1) / v2
    return m2

def hitung_m1(v1, m2, v2):
    if v1 <= 0 or m2 <= 0 or v2 <= 0:
        return None
    m1 = (m2 * v2) / v1
    return m1

# ==========================================
# TAMPILAN UTAMA
# ==========================================

# Header Utama
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h1 style="font-size: 48px; margin-bottom: 10px;">⚗️ Kalkulator Kimia</h1>
    <p style="font-size: 18px; color: #666;">Aplikasi Perhitungan Larutan & Pengenceran</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Tab Menu
tab_larutan, tab_pengenceran, tab_periodik = st.tabs([
    "🧪 Pembuatan Larutan", 
    "💧 Pengenceran", 
    "📊 Tabel Periodik"
])

# ======================
# TAB 1: PEMBUATAN LARUTAN
# ======================
with tab_larutan:
    st.markdown("### 🧪 Hitung Massa Zat Terlarut")
    
    st.markdown("""
    <div class="info-box">
        <b style="font-size: 18px;">📝 Cara Menggunakan:</b><br>
        Masukkan nilai Mr zat, volume larutan yang diinginkan, dan konsentrasi molar (M) lalu klik tombol Hitung.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📐 Lihat Rumus & Referensi"):
        st.markdown("""
        <div class="rumus-box">
            <b style="font-size: 20px;">📐 Rumus Pembuatan Larutan:</b><br><br>
            <code style="font-size: 24px; color: #d32f2f;">Massa = M × (V/1000) × Mr</code><br><br>
            <b>Keterangan:</b><br>
            - M = Molaritas larutan (mol/L)<br>
            - V = Volume larutan (mL)<br>
            - Mr = Massa molar zat (g/mol)
        </div>
        
        <div class="referensi-box">
            <b style="font-size: 18px;">📚 Sumber Referensi:</b><br>
            1. Petrucci, R.H. et al. (2017). General Chemistry: Principles & Modern Applications. Pearson.<br>
            2. Atkin, P. (2020). Chemical Principles. Oxford University Press.<br>
            3. IUPAC (2024). Compendium of Chemical Terminology.
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**<code>🔢 Masukan Data:</code>**")
        mr = st.number_input("Massa Molar (Mr) [g/mol]", min_value=0.0, key="mr_input")
        volume = st.number_input("Volume (V) [mL]", min_value=0.0, key="vol_input")
    with col2:
        st.markdown("**<code>🎯 Target:</code>**")
        molaritas = st.number_input("Konsentrasi (M) [mol/L]", min_value=0.0, key="mol_input")
    
    st.markdown("<br>", unsafe_allow_html=True)
    hitung_btn = st.button("🔬 Hitung Massa", type="primary", use_container_width=True)
    
    if hitung_btn:
        if mr <= 0 or volume <= 0 or molaritas <= 0:
            st.error("❌ Semua nilai harus lebih dari 0!")
        else:
            massa = hitung_larutan(mr, volume, molaritas)
            hasil_teks = "Massa yang dibutuhkan: " + "{:.4f}".format(massa) + " gram"
            st.success("✅ " + hasil_teks)
            simpan_riwayat("Larutan -> " + hasil_teks)
            st.rerun()

# ======================
# TAB 2: PENGENCERAN
# ======================
with tab_pengenceran:
    st.markdown("### 💧 Pengenceran Larutan")
    
    st.markdown("""
    <div class="info-box">
        <b style="font-size: 18px;">📝 Cara Menggunakan:</b><br>
        Pilih variabel yang ingin dicari (V1, V2, M1, atau M2), masukkan nilai yang diketahui, lalu klik tombol Hitung.
    </div>
    """, unsafe_allow_html=True)
    
    subtab_v2, subtab_v1, subtab_m2, subtab_m1 = st.tabs(["📏 Hitung V2", "📏 Hitung V1", "📐 Hitung M2", "📐 Hitung M1"])
    
    # --- Hitung V2 ---
    with subtab_v2:
        st.markdown("**Mencari Volume Akhir (V2)**")
        
        with st.expander("📐 Rumus"):
            st.markdown("""
            <div class="rumus-box">
                <code style="font-size: 24px; color: #d32f2f;">V2 = (M1 × V1) / M2</code><br><br>
                Berdasarkan persamaan pengenceran:<br>
                <b>M1 × V1 = M2 × V2</b>
            </div>
            """, unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            m1 = st.number_input("M1 (konsentrasi awal)", key="m1_v2", min_value=0.0)
        with c2:
            v1 = st.number_input("V1 (volume awal) mL", key="v1_v2", min_value=0.0)
        with c3:
            m2 = st.number_input("M2 (konsentrasi akhir)", key="m2_v2", min_value=0.0)
        
        if st.button("🔬 Hitung V2", key="btn_v2"):
            if m1 <= 0 or v1 <= 0 or m2 <= 0:
                st.error("❌ Semua nilai harus lebih dari 0!")
            else:
                v2 = hitung_v2(m1, v1, m2)
                hasil = "Volume Akhir (V2) = " + "{:.2f}".format(v2) + " mL"
                st.success("✅ " + hasil)
                simpan_riwayat("Pengenceran -> " + hasil)
                st.rerun()
    
    # --- Hitung V1 ---
    with subtab_v1:
        st.markdown("**Mencari Volume Awal (V1)**")
        
        with st.expander("📐 Rumus"):
            st.markdown("""
            <div class="rumus-box">
                <code style="font-size: 24px; color: #d32f2f;">V1 = (M2 × V2) / M1</code><br><br>
                Berdasarkan persamaan pengenceran:<br>
                <b>M1 × V1 = M2 × V2</b>
            </div>
            """, unsafe_allow_html=True)
        
        d1, d2, d3 = st.columns(3)
        with d1:
            m1_v1 = st.number_input("M1 (konsentrasi awal)", key="m1_v1", min_value=0.0)
        with d2:
            m2_v1 = st.number_input("M2 (konsentrasi akhir)", key="m2_v1", min_value=0.0)
        with d3:
            v2_v1 = st.number_input("V2 (volume akhir) mL", key="v2_v1", min_value=0.0)
        
        if st.button("🔬 Hitung V1", key="btn_v1"):
            if m1_v1 <= 0 or m2_v1 <= 0 or v2_v1 <= 0:
                st.error("❌ Semua nilai harus lebih dari 0!")
            else:
                v1 = hitung_v1(m1_v1, m2_v1, v2_v1)
                hasil = "Volume Awal (V1) = " + "{:.2f}".format(v1) + " mL"
                st.success("✅ " + hasil)
                simpan_riwayat("Pengenceran -> " + hasil)
                st.rerun()
    
    # --- Hitung M2 ---
