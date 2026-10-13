import streamlit as st
import streamlit.components.v1 as components
# Konfigurasi halaman
st.set_page_config(
    page_title="AAS AA-7000 — Simulasi 3D Interaktif",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Hilangkan header, footer, padding putih bawaan Streamlit, dan buat iframe 100% layar
st.markdown("""
<style>
    /* Sembunyikan header Streamlit dan toolbar atas */
    header[data-testid="stHeader"], footer, #MainMenu {
        display: none !important;
        visibility: hidden !important;
    }
    /* Hilangkan padding putih di sekeliling halaman */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    /* Buat tampilan simulasi 3D memenuhi seluruh layar browser (Full Viewport) */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 99999 !important;
    }
    /* Atur warna latar belakang agar menyatu dengan tema simulasi */
    html, body {
        overflow: hidden !important;
        background-color: #0e1030 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)
# URL Simulasi 3D
url_simulasi = "https://mdaffaarrafi1-tamvan.github.io/3D-AAS-Shimdzu-AA-7000/"
# Render iframe
components.iframe(url_simulasi)
