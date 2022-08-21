import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import datetime

pic = pd.read_pickle('https://www.dropbox.com/s/msfjuvuk9satqg9/alarmmodelrandomforest.pkl?dl=1')

rf = pic["model"]


def show_alarm_page():
    st.title("Crime Alarm For each police District")

    st.write("""### We need some the district,time and date to predict the alarm""")

    PdDistrict = ('SOUTHERN', 
                  'MISSION', 
                  'NORTHERN', 
                  'CENTRAL', 
                  'BAYVIEW', 
                  'INGLESIDE', 
                  'TENDERLOIN', 
                  'TARAVAL', 
                  'PARK', 
                  'RICHMOND'
    )
    
    Pdoptions = list(range(len(PdDistrict)))
    value = st.selectbox("PdDistrict", Pdoptions, format_func=lambda x: PdDistrict[x])

    date= st.date_input("When's the crime",datetime.date(2019, 7, 6))
    
    ok = st.button("Predict Alarm")
    if ok:
        day=date.datetime.day
        month=date.datetime.month 
        year=date.datetime.year 
        st.write(day)
        st.write(month)
        st.write(year)

