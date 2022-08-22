import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
import numpy as np



def show_explore_page():
    Longitude = st.number_input('Insert a number',max_value=-122.364937,min_value=-122.513642)
    st.write('The current number is ', Longitude)
    Latitude = st.number_input('Insert a number',max_value=37.8206208380702,min_value=37.7078790224135)
    st.write('The current number is ', Latitude)
    
    
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(df)
    
    ok = st.button("Show map")
    if ok:
        cor = np.array([[Latitude,Longitude]])
        st.write(cor)
        cor = np.core.records.fromarrays([Latitude,Longitude],names='Latitude,Longitude')
        st.write(cor)
        st.map(cor)
