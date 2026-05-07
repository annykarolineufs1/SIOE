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
Sistema Inteligente de Organização de E-mails
</div>
""", unsafe_allow_html=True)

email = st.text_area(
    "Cole o e-mail:",
    height=200
)

if st.button("ANALISAR"):

    texto = email.lower()

    if "urgente" in texto or "agora" in texto:
        st.error("🔴 URGENTE")

    elif "senha" in texto or "link" in texto:
        st.warning("⚠️ MALICIOSO")

    elif "prazo" in texto or "reunião" in texto:
        st.info("🟡 IMPORTANTE")

    else:
        st.success("🟢 NORMAL")
