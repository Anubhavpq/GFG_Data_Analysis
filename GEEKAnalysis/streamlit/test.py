import streamlit as st 
import numpy as np 
import pandas as pd
import time 

st.title("Spinner with Countdown")

duration = 10  # total time in seconds

placeholder = st.empty()

with st.spinner("Processing..."):
    for remaining in range(duration, 0, -1):
        placeholder.write(f"⏳ Time remaining: {remaining} seconds")
        time.sleep(1)

placeholder.write("✅ Task completed!")