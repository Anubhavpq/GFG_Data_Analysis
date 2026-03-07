import streamlit as st

st.subheader("1. Radio button;")
st.radio("select gender" , options= ("male", "female"))

st.subheader("2.select Box ")
st.selectbox("select your options :" , options= ("AI" , "ML" , "DSA" , "data analytics") )

st.subheader("Multiselect box")
st.multiselect("select your options :" ,  options= ("AI" , "ML" , "DSA" , "data analytics") )

st.subheader("button")
if st.button("say hi") :
    st.write("hi")

st.subheader("Checkbox")
if st.checkbox("agree to terms and conditions :" , help= "you must agree to all the terms and conditions please") :
    st.write("thanks")

st.subheader('6. Color Picker')
color = st.color_picker('Select your favourite color : ', "#C3E1BA")
st.write("You've selected ",color,'color')