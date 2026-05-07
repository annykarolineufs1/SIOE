import streamlit as st

st.set_page_config(
    page_title="SIOE",
    page_icon="📧",
    layout="centered"
)

st.title("📧 SIOE")

st.markdown(
    "<h2 style='color:#22C55E;'>Sistema Inteligente de Organização de E-mails</h2>",
    unsafe_allow_html=True
)

st.write(
    "O sistema analisa automaticamente os e-mails e auxilia na tomada de decisão."
)

email = st.text_area(
    "Cole o conteúdo do e-mail:",
    height=200
)

if st.button("ANALISAR"):

    texto = email.lower()

    if "urgente" in texto or "agora" in texto or "imediato" in texto:

        st.error("🔴 E-mail classificado como URGENTE")
        st.write("Recomendação: Confirmar urgência antes de tomar a decisão.")

    elif "senha" in texto or "link" in texto or "download" in texto:

        st.warning("⚠️ E-mail classificado como MALICIOSO")
        st.write("Recomendação: Excluir ou reportar imediatamente.")

    elif "prazo" in texto or "reunião" in texto or "relatório" in texto:

        st.info("🟡 E-mail classificado como IMPORTANTE")
        st.write("Recomendação: Verificar prioridade antes de responder.")

    else:

        st.success("🟢 E-mail classificado como NORMAL")
        st.write("Recomendação: Responder quando possível.")

st.caption("SIOE • Sistema Inteligente de Organização de E-mails")
