import streamlit as st
from predict_alarm import show_alarm_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Hotspot", ("Hotspot", "Explore"))

if page == "Hotspot":
    show_alarm_page()
else:
    show_explore_page()
