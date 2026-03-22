import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("line chart")
chart_data = pd.DataFrame(np.random.randn(20 , 4) , columns= ["L-1" , 'L -2' , 'L-3' , 'L-4'])
st.line_chart(chart_data)

st.title("Area chart")
chart_data = pd.DataFrame(np.random.randn(20 , 4) , columns= ["L-1" , 'L -2' , 'L-3' , 'L-4'])
st.area_chart(chart_data)

st.title("bar chart")
chart_data = pd.DataFrame(np.random.randn(20 , 4) , columns= ["L-1" , 'L -2' , 'L-3' , 'L-4'])
st.bar_chart(chart_data)

st.title("data_visualization with seaboarn and matplotlib")
data = pd.read_csv("GEEKAnalysis/streamlit/iris.csv")
st.dataframe(data)

st.text('2. Bar Plot using Matplotlib')
fig = plt.figure(figsize= (15,8))
data['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)