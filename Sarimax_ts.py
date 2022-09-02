import streamlit as st
import streamlit.components.v1 as components


def show_arima_page():
  st.header("SARIMAX output ")
  
  st.subheader("Predicted cases for top 4 crimes")
  HtmlFile = open("prediction_top10 crimes.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  print(source_code)
  components.html(source_code,height = 600)
  
  st.subheader("Predicted Theft cases ")
  HtmlFile2 = open("prediction_theft.html", 'r', encoding='utf-8')
  source_code2 = HtmlFile2.read() 
  components.html(source_code2,height = 600)
  
  st.subheader("Predicted Assault cases ")
  HtmlFile3 = open("prediction_Assault.html", 'r', encoding='utf-8')
  source_code3 = HtmlFile3.read() 
  components.html(source_code3,height = 600)
  
  st.subheader("Predicted Vehicle Theft cases ")
  HtmlFile4 = open("prediction_Vehicle.html", 'r', encoding='utf-8')
  source_code4 = HtmlFile4.read() 
  components.html(source_code4,height = 600)
