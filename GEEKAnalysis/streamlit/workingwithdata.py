import streamlit as st 
import numpy as np
import pandas as pd
from PIL import Image

img = Image.open("D:/pan card.jpg")
st.image(img)

st.write("import the image from link")
st.image("https://media.geeksforgeeks.org/gfg-gg-logo.svg")

video_file = ("D:/papa ji/20250324_111536.mp4")
st.video(video_file)

