import streamlit as st
from predict_alarm import show_alarm_page
from explore_page import show_explore_page
from crimeclassifier import show_classifier_page
from arima_ts import show_arima_page

page = st.sidebar.selectbox("Explore Or Hotspot", ("Hotspot", "Classifier","Arima","Explore"))

if page == "Hotspot":
    show_alarm_page()
elif page == "Classifier":
    show_classifier_page()
elif page == "Arima":
    show_arima_page()
else:
    show_explore_page()
