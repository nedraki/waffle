import streamlit as st
import streamlit.components.v1 as components


st.header('Hello world')

#Testing importing script

st.write("test html import:")
html_file = open("test.html", 'r', encoding='utf-8')
source_code = html_file.read() 
print(source_code)
components.html(source_code)
