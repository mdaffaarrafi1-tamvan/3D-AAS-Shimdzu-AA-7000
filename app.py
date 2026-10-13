import streamlit as st
import streamlit.components.v1 as components
# Atur tata letak lebar (wide) agar tampilan 3D maksimal
st.set_page_config(
    page_title="Simulasi 3D AAS AA-7000",
    page_icon="🔬",
    layout="wide"
)
st.title("🔬 Simulasi 3D Interaktif AAS Shimadzu AA-7000")
st.write("Eksplorasi komponen instrumen Atomic Absorption Spectrophotometer secara interaktif.")
# Masukkan link GitHub Pages Anda
url_simulasi = "https://mdaffaarrafi1-tamvan.github.io/3D-AAS-Shimdzu-AA-7000/"
# Tampilkan via iframe (sesuaikan height sesuai kebutuhan)
components.iframe(url_simulasi, height=850, scrolling=True)
