import streamlit as st

st.set_page_config(
    page_title="SIOE",
    page_icon="📧",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background-color: #0F172A;
    color: white;
}

h1 {
    color: #22C55E;
    text-align: center;
    font-size: 50px;
}

textarea {
    background-color: #1E293B !important;
    color: white !important;
}

.stButton button {
    background-color: #22C55E;
    color: black;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border: none;
    font-weight: bold;
}

.card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1>📧 SIOE</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>Sistema Inteligente de Organização de E-mails</h3>
<p>
O sistema analisa automaticamente os e-mails e fornece suporte para tomada de decisão.
</p>
</div>
""", unsafe_allow_html=True)

email = st.text_area(
    "Cole o conteúdo do e-mail:",
    height=200
)

if st.button("ANALISAR"):

    texto = email.lower()

    if "urgente" in texto or "agora" in texto or "imediato" in texto:

        st.error("🔴 E-mail classificado como URGENTE")

        st.markdown("""
        <div class="card">
        <h4>Recomendação do Sistema</h4>
        <p>Confirmar urgência antes de tomar a decisão.</p>
        </div>
        """, unsafe_allow_html=True)

    elif "senha" in texto or "link" in texto or "download" in texto:

        st.warning("⚠️ E-mail classificado como MALICIOSO")

        st.markdown("""
        <div class="card">
        <
