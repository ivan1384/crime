import streamlit as st
import streamlit.components.v1 as components


def show_arima_page():
  st.header("Arima output ")
  
  
  HtmlFile = open("prediction_assault.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read(height = 600) 
  print(source_code)
  components.html(source_code)
  
  
  
