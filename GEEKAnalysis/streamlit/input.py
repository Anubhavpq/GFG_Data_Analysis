import streamlit as st 

st.subheader("1. Enter your name")
name = st.text_input("enter name")
st.text(name)

st.subheader("2. password input :")
st.text_input("enter your password", type = "password" , help = "maximum 8 characters please")

st.subheader('4. Numeric Input')
st.number_input('Enter your age : ', min_value = 0, max_value = 110, step = 1, )

st.subheader("text area")
st.text_area("describe yourself ..")

