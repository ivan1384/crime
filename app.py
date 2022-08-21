import streamlit as st
from predict_alarm import show_alarm_page
from explore_page import show_explore_page
from crimeclassifier import show_classifier_page

page = st.sidebar.selectbox("Explore Or Hotspot", ("Hotspot", "Classifier","Explore"))

if page == "Hotspot":
    show_alarm_page()
 if page == "Classifier":
    show_classifier_page()
else:
    show_explore_page()
