import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import datetime
import string as str
from dateutil.parser import parse

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
    Hour_zone = ( "12:00AM-5:59AM","6:00AM-11:59AM","12:00PM-5:59PM","6:00PM-11:59PM" 
            )
    Pdoptions = list(range(len(PdDistrict)))
    Pdvalue = st.selectbox("PdDistrict", Pdoptions, format_func=lambda x: PdDistrict[x])

    crimed= st.date_input("When's the crime",datetime.date(2019, 7, 6))
    
    houroptions = list(range(len(Hour_zone)))
    hourvalue =st.selectbox("Hour_zone", houroptions, format_func=lambda x: Hour_zone[x])
    
    
    ok = st.button("Predict Alarm")
    if ok:
        dayofweek=crimed.weekday()
        scrimed = crimed.strftime('%Y-%m-%d')
        dt = parse(scrimed)
        year=dt.year
        month=dt.month
        day=dt.day
        season = (dt.month%12 + 3)//3
        st.write(hourvalue)
        X = np.array([[year,month,day,dayofweek,hourvalue,Pdvalue,season]])
        alarm=rf.predict(X)
        
        if alarm == 0:
            print("Low Crime at this precinct and time")
        elif alarm == 1:
            print("Medium Crime Rate at this precinct and time")
         elif alarm == 2:
            print("High Crime at this precinct and time")
        
        
        
