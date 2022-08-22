import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit-folium
import folium




def show_explore_page():
    m = fl.Map()

    m.add_child(fl.LatLngPopup())

    map = st_folium(m, height=350, width=700)
