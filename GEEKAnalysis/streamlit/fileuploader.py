import streamlit as st
from PIL import Image
import numpy as np 
import pandas as pd

st.subheader("Image upload")

Img = st.file_uploader("upload an image" , type = ['jpg' , 'png'])
if Img is not None :
    file_details = {"file_name": Img.name, "file_size": Img.size, "file_type": Img.type}
    print(file_details)
    st.image(Img)

#Audio
st.subheader(" Upload an audio")

audio = st.file_uploader("uplad audio")

if audio is not None :
    file_details = {"file_name": Img.name, "file_size": Img.size, "file_type": Img.type}
    print(file_details)
    st.audio(audio)

#video upload
st.subheader("Image upload")

video = st.file_uploader("upload you video" , type = ["mp4"])
if video is not None :
    file_details = {"file_name": Img.name, "file_size": Img.size, "file_type": Img.type}
    print(file_details)

    st.video(video)

#working with csv file
st.subheader("csv uload")

video = st.file_uploader("upload you csv" , type = ["csv"])
if video is not None :
    file_details = {"file_name": Img.name, "file_size": Img.size, "file_type": Img.type}
    print(file_details)

    st.video(video)
