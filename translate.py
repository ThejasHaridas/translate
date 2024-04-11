import streamlit as st
from googletrans import Translator

st.header('Machine Transilation Demo')
input=st.text_area("please enter the text",value="")
option=st.selectbox(
    'to which language you wish to translate this text to?',
    ('Malayalam','Hindi','Tamil')
)
if st.button("Translate"):
    transilator=Translator()
    transilation=transilator.translate(input,dest=option)
    st.write(transilation.text)