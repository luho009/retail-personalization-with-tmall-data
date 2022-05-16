import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import os
#from annotated_text import annotated_text

def app():
    # st.image('Tmall-logo_2.png', width=150)
    st.header('Tmall User Segmentation & Prediction')

    def read_file(path):
        #Read types first line of csv
        dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
        #Read the rest of the lines with the types from above
        return pd.read_csv(path, dtype=dtypes, skiprows=[1])
    segment = read_file('data/SegmentationOutputforStreamlit1.csv')
    prediction = read_file("data/buyerpredict.csv")

    def displaysegment():
        cluster = target_df.at[target_df.index.item(),'Cluster']
        st.markdown('This user belongs to segment ' f'**{cluster}**')
        st.text('User Information: ')
        st.table(target_df)

    def displayprediction():
        st.table(pred_target_df)

    target = st.text_input("Please input user id:")
    submitted = st.button('Submit')
    if submitted:
        target_df = segment[segment['User Id']== target]
        displaysegment()
        st.text('Repeat Purchase Prediction: ')
        pred_target_df = prediction[prediction['user_id']== target]
        displayprediction()
