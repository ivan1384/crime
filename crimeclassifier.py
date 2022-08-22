
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import datetime
import string as str
from dateutil.parser import parse
import folium

pic = pd.read_pickle('https://www.dropbox.com/s/msfjuvuk9satqg9/alarmmodelrandomforest.pkl?dl=1')

rf = pic["model"]


def show_classifier_page():
    st.title("Crime Classifier for most probable property crime or drug user/dealer given location")

    st.write("""### We need some the district,time and date to predict the alarm""")

    PdDistrict = ('SOUTHERN', 'MISSION', 'NORTHERN', 'CENTRAL', 'BAYVIEW', 
                  'INGLESIDE', 'TENDERLOIN',  'TARAVAL', 'PARK', 'RICHMOND' )
    Pdoptions = list(range(len(PdDistrict)))
    Pdvalue = st.selectbox("PdDistrict", Pdoptions, format_func=lambda x: PdDistrict[x])
    
    crimed= st.date_input("When's the crime",datetime.date(2019, 7, 6))
    
    Hour = ( 0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 , 12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 )
    Hours = st.selectbox("Hour of the day", Hour)
    
    Blockno = (0 ,100 ,200 ,300 ,400 ,500 ,600 ,700 ,800 ,900 ,1000 ,1100 ,1200 ,1300 ,1400 ,1500 ,1600 ,1700 ,1800 ,1900 ,2000 ,2100 ,2200 ,2300 ,2400 ,
               2500 ,2600 ,2700 ,2800 ,2900 ,3000 ,3100 ,3200 ,3300 ,3400 ,3500 ,3600 ,3700 ,3800 ,3900 ,4000 ,4100 ,4200 ,4300 ,4400 ,4500 ,4600 ,4700 ,
               4800 ,4900 ,5000 ,5100 ,5200 ,5300 ,5400 ,5500 ,5600 ,5700 ,5800 ,5900 ,6000 ,6100 ,6200 ,6300 ,6400 ,6500 ,6600 ,6700 ,6800 ,6900 ,7000 ,
               7100 ,7200 ,7300 ,7400 ,7500 ,7600 ,7700 ,7800 ,7900 ,8000 ,8100 ,8200 ,8300 ,8400)
    blockoptions = list(range(len(Blockno)))
    blockvalue =st.selectbox("Hour_zone", blockoptions, format_func=lambda x: Blockno[x])
    
    Street=('AL', 'AV', 'BL', 'CR', 'CT', 'DR', 'EL CAMINO DEL MAR', 'HY', 'I-80', 
            'INT', 'LN', 'OTHER', 'PL', 'PZ', 'RD', 'ST', 'TR', 'WAY', 'WK', 'WY')
    streetoptions = list(range(len(Street)))
    Streetvalue =st.selectbox("Street Type", streetoptions, format_func=lambda x: Street[x])
    
    Longitude = st.number_input('Insert a number',max_value=-122.364937,min_value=-122.513642)
    st.write('The current number is ', Longitude)
    Latitude = st.number_input('Insert a number',max_value=37.8206208380702,min_value=37.7078790224135)
    st.write('The current number is ', Latitude)
    
    

    map = st.button("Show map to check if coordinates are correct")
    if map:
        cor = np.array([[Latitude,Longitude]])
        df = pd.DataFrame(np.array([[Latitude,Longitude]]),
        columns=['lat', 'lon'])
        st.map(df)

    
    
    
    
    ok = st.button("Predict Alarm")
    if ok:
        dayofweek=crimed.weekday()
        scrimed = crimed.strftime('%Y-%m-%d')
        dt = parse(scrimed)
        year=dt.year
        month=dt.month
        day=dt.day
        season = (dt.month%12 + 3)//3
        # x input should follow this DayOfWeek	PdDistrict	X	Y	Month	Day	Year	Hour	StreetType	BlockNo	Rot30_X	Rot30_Y	Rot45_X	Rot45_Y	Rot60_X	Rot60_Y	Radius	Angle
        #X = np.array([[dayofweek,Pdvalue,xcor,ycor,hourvalue,month,day,year,Hours,,,,,,,]])

        
        
        
