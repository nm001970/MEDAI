import streamlit as st
import  pandas as pd
from PIL import Image
import os

st.write (''' 
# visualizing forex data
** MOHAMMAD NADERI
''')

img = Image.open(r'C:\Users\White Ram\Desktop\my_streamlit_app\pythonProject\img\robot-with-tablet.jpg')
st.image(img,width=300, caption='MED_group')
st.sidebar.header('Input Data')