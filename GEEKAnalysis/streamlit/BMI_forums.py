import streamlit as st 
st.title("BMI Index Calculator")

with st.form("BMI Index Calculator"):
    col1 , col2 , col3 = st.columns([3,2,1])

with col1: 
    weight = st.number_input("enter your weight" , min_value= 0 , max_value= 150 ,step= 1)

with col2:
    hieght = st.number_input("enter the hieght")

with col3:
   submit = st.form_submit_button("calculate the results ")

if submit:
    BMI = round((weight / hieght**2),2)
    if (BMI <= 18.5):
        st.error("Underweight")
    elif(BMI >18.5 and BMI <= 24.9 ):
        st.success ("Healthy/ Normal BMI")
    elif (BMI>=25 and BMI <= 29.9):
        st .warning("Overweight")
    elif (BMI>=30.0):
        st.error ("OBESE")