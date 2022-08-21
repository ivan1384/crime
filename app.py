import streamlit as st
from predict_alarm import predict_alarm
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Hotspot", ("Hotspot", "Explore"))

if page == "Hotspot":
    show_predict_page()
else:
    show_explore_page()
