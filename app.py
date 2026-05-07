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

if st.button("AN
