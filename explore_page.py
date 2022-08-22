import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit-folium
import folium




def show_explore_page():
    Longitude = st.number_input('Insert a number',max_value=-122.364937,min_value=-122.513642)
    st.write('The current number is ', Longitude)
    Latitude = st.number_input('Insert a number',max_value=37.819975,min_value=37.707879)
    st.write('The current number is ', Latitude)
