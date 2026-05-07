import streamlit as st

st.set_page_config(
    page_title="SIOE",
    page_icon="📧",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    textarea {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='color:#16A34A; text-align:center;'>📧 SIOE</h1>",
    unsafe_allow_html=True
)

st.subheader("Sistema Inteligente de Organização de E-mails")

email = st.text_area(
    "Cole o conteúdo do e-mail:",
    height=200,
    placeholder="Digite ou cole aqui o e-mail para análise..."
)

if st.button("ANALISAR E-MAIL"):

    texto = email.lower()

    if (
        "urgente" in texto or
        "agora" in texto or
        "imediato" in texto
    ):
        st.error("🔴 E-mail classificado como URGENTE")
        st.write("Confirmar urgência antes da decisão.")

    elif (
        "senha" in
