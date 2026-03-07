import streamlit as st
import numpy as np
import pandas as pd
import time

cases = []
for x in range(100):
   cases.append(np.random.random_integers(1,7))

data = []
for i in range(1,7):
   data.append(cases.count(i))

st.write("the frequency of data is :")
st.bar_chart(data)

with st.expander("see explaination"):
   st.write('this is the frequency distribution graph for the following dice rolled')

with st.empty():
    st.write('You need to wait for 10 seconds')
    for seconds in range(11):
     st.write('%'+ str(seconds))
     time.sleep(1)
     st.write('10 seconds completed')

with st.spinner("wait for 5 seconds"):
     time.sleep(5)
     st.write("thanks for being patient")

with st.empty():
   for x in range(100):
    time.sleep(.1)
    st.progress( x + 1 , text= 'processing')

st.write("project completed")