import streamlit as st
import numpy as np
from multiapp import MultiApp
from PIL import  Image
from apps import segmentation_repeatbuyer, tmall_o2o # import your app modules here

app = MultiApp()

# Title of the main page
display = Image.open('Tmall-logo_2.png')
display = np.array(display)

col1, col2 = st.columns([1,3])
col1.image(display, width = 180)
col2.title("Retail Personalization in Practice")

# Add all your application here
app.add_app("Customer Segmentation", segmentation_repeatbuyer.app)
app.add_app("Coupon Prediction", tmall_o2o.app)

# The main app
app.run()