import streamlit as st

col1 , col2 , col3 = st.columns(3)
with col1:
    st.header('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg', width = 200)
with col2:
    st.header('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg', width = 200)
with col3:
    st.header('Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg', width = 200)

#dynamic 
n = st.number_input("enter the number of picture you want", 1 , 10)
cols = st.columns(n)

for col in cols :
    st.image('https://static.streamlit.io/examples/dog.jpg')