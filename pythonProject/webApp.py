import streamlit as st
import  pandas as pd
from PIL import Image
import os

st.write (''' 
# visualizing forex data
** MOHAMMAD NADERI
''')

img_path = os.path.join('img', 'robot-with-tablet.jpg')
img = Image.open(img_path)
st.image(img,width=300, caption='MED_group')
st.sidebar.header('Input Data')
