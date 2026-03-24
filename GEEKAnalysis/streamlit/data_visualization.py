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

st.text('2. histplot using seaborn')
fig = plt.figure(figsize= (15,8))
sns.histplot(data['sepal_length'] , kde= True)
st.pyplot(fig)

col1 , col2 = st.columns(2)

with col1:
    col1.write('KDE = False')
    fig1 = plt.figure()
    sns.distplot(data['sepal_length'], kde = False)
    st.pyplot(fig1)

with col2:
    col2.write('Hist = False')
    fig2 = plt.figure()
    sns.distplot(data['sepal_length'], hist = False)
    st.pyplot(fig2)

col1 , col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.distplot(data['petal_length'], hist = False)
    st.pyplot(fig1)
with col2:
    fig2 = plt.figure()
    sns.set_theme (context = 'poster')
    sns.distplot(data['petal_length'], hist = False)
    st.pyplot(fig2)

st.text('6. Scatter Plot')
fig, ax = plt.subplots(figsize =(15,8))
ax.scatter(*np.random. random(size = (2,100)))
st.pyplot(fig)

st.text('6. Count Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = data, x = 'species' )
st.pyplot()

st.text('8. Box Plot')
fig = plt.figure(figsize= (15,8))
sns.boxplot(data = data, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.text('9. Violin Plot')
fig = plt.figure(figsize= (15,8))
sns.violinplot(data = data , x = 'species', y = 'petal_length')
st.pyplot(fig)