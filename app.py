import streamlit as st
import pickle
import numpy as np
import pandas as pd


pic = pd.read_pickle('https://www.dropbox.com/s/msfjuvuk9satqg9/alarmmodelrandomforest.pkl?dl=1')

rf = pic["model"]


def show_predict_page():
    st.title("Crime Alarm For Each police District")

    st.write("""### We need some the district,time and date to predict the alarm""")

    PdDistrict = ('SOUTHERN':0, 
                  'MISSION':1, 
                  'NORTHERN':2, 
                  'CENTRAL':3, 
                  'BAYVIEW':4, 
                  'INGLESIDE':5, 
                  'TENDERLOIN':6, 
                  'TARAVAL':7, 
                  'PARK':8, 
                  'RICHMOND':9
    )


    if ok:
        st.subheader(PdDistrict)
