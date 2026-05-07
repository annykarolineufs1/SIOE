import streamlit as st

st.set_page_config(
    page_title="SIOE",
    page_icon="📧",
    layout="centered"
)

# ESTILO VISUAL
st.markdown("""
<style>

.stApp {
    background-color: #0F172A;
    color: white;
}

.titulo {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #22C55E;
    margin-bottom: 0;
}

.subtitulo {
    text-align: center;
    color: #CBD5E1;
    font-size: 16px;
    margin-top: 5px;
    margin-bottom: 30px;
}

.card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

.stButton button {
    background-color: #22C55E;
    color: black;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border: none;
    font-weight: bold;
}

.stTextArea textarea {
    background-color: #111827;
    color: white;
    border-radius: 10px;
}

.rodape {
    text-align: center;
    color: #94A3B8;
    font-size: 12px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown("""
<div class="titulo">
📧 SIOE
</div>
""", unsafe_allow_html=True)

# SUBTÍTULO
st.markdown("""
<div class="subtitulo">
Sistema Inteligente de Organização de E-mails
</div>
""", unsafe_allow_html=True)

# CARD CENTRAL
st.markdown("""
<div class="card">
O sistema realiza análise automática de e-mails, classificando mensagens e auxiliando na tomada de decisão.
</div>
""", unsafe_allow_html=True)

# CAMPO EMAIL
email = st.text_area(
    "Cole o conteúdo do e-mail:",
    height=200,
    placeholder="Digite ou cole aqui o e-mail para análise..."
)

# BOTÃO
if st.button("ANALISAR E-MAIL"):

    texto = email.lower()

    # URGENTE
    if "urgente" in texto or "agora" in texto or "imediato" in texto:

        st.error("🔴 E-mail classificado como URGENTE")
        
        st.info(
            "Recomendação do sistema: Confirmar urgência antes de tomar a decisão."
        )

    # MALICIOSO
    elif "senha" in texto or "link" in texto or "download" in texto:

        st.warning("⚠️ E-mail classificado como MALICIOSO")

        st.info(
            "Recomendação do sistema: Excluir ou reportar imediatamente."
        )

    # IMPORTANTE
    elif "prazo" in texto or "reunião" in texto or "relatório" in texto:

        st.info("🟡 E-mail classificado como IMPORTANTE")

        st.success(
            "Recomendação do sistema: Verificar prioridade antes de responder."
        )

    # NORMAL
    else:

        st.success("🟢 E-mail classificado como NORMAL")

        st.write(
            "Recomendação do sistema: Responder quando possível."
        )

# RODAPÉ
st.markdown("""
<div class="rodape">
SIOE • Sistema Inteligente de Organização de E-mails
</div>
""", unsafe_allow_html=True)
