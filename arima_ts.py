import streamlit as st
import streamlit.components.v1 as components


def show_arima_page():
  st.header("Arima output ")
  
  st.subheader("Predicted Assault cases ")
  HtmlFile = open("prediction_assault.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  print(source_code)
  components.html(source_code,height = 600)
  
  st.subheader("Predicted Theft cases ")
  HtmlFile2 = open("prediction_theft.html", 'r', encoding='utf-8')
  source_code2 = HtmlFile2.read() 
  print(source_code)
  components.html(source_code2,height = 600)
  
