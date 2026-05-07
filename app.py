import streamlit as st

st.title("SIOE - Sistema Inteligente de Organização de E-mails")

email = st.text_area("Cole o conteúdo do e-mail")

if st.button("Analisar"):

    texto = email.lower()

    if "urgente" in texto or "agora" in texto:
        resultado = "🔴 URGENTE"
        recomendacao = "Confirmar urgência antes da decisão."

    elif "senha" in texto or "clique no link" in texto:
        resultado = "⚠️ MALICIOSO"
        recomendacao = "Excluir ou reportar."

    elif "reunião" in texto or "prazo" in texto:
        resultado = "🟡 IMPORTANTE"
        recomendacao = "Verificar prioridade."

    else:
        resultado = "🟢 NORMAL"
        recomendacao = "Responder quando possível."

    st.subheader(resultado)
    st.write(recomendacao)
