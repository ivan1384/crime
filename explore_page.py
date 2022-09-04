import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as px
import datetime as dt

def show_explore_page():
    st.title("Sanfrancisco Crime analysis ")
    st.markdown('Crime in Sanfrancisco')
    st.sidebar.title('Sanfrancisco Crime analysis')
    st.sidebar.subheader('Crime in Sanfrancisco')
    @st.cache(persist=True)
    def load_data():
      data = pd.read_csv('https://www.dropbox.com/s/ug5mkq9ija3mmpn/train.csv?dl=1')
      data['Dates']=pd.to_datetime(data['Date'] + ' ' + data['Time'])
      return data
    
    data = load_data()
    data =data[['Dates','Category','Descript','DayOfWeek','PdDistrict','Resolution','Address','X','Y']]
    data.columns = ['Dates','Category','Descript','DayOfWeek','PdDistrict','Resolution','Address','longitude','latitude']
    
    st.sidebar.markdown('Type of crimes and their stats')
    select = st.sidebar.selectbox('visualization type',['Histogram','Pie chart'])
    crime_count = data['Category'].value_counts()
    crime_count = pd.DataFrame({'Crime':crime_count.index, 'Numbers': crime_count.values})
    st.markdown("Rate of crime as per type")
    if select == "Histogram":
        fig = px.bar(crime_count,x="Crime",y="Numbers",color="Numbers",height =600,width=900)
        st.plotly_chart(fig)
    else:
        fig = px.pie(crime_count,values="Numbers",names="Crime")
        st.plotly_chart(fig)
    
    st.sidebar.subheader("crime based on the time of day")
    hour = st.sidebar.slider("Hours of day",0,23)
    year = st.sidebar.slider("Year",2003,2018)
    month = st.sidebar.slider("Month",1,12)
    day = st.sidebar.slider("day",1,31)
    mod_dat = data[data['Dates'].dt.hour == hour]
    mod_dat = mod_dat[data['Dates'].dt.year == year]
    mod_dat = mod_dat[data['Dates'].dt.month == month]
    mod_dat = mod_dat[data['Dates'].dt.day == day]
    if not st.sidebar.checkbox("Don't show map",False):
        st.markdown("Crime location based on time")
        st.markdown("%i crime between %i:00 and %i:00 in the Month of %i" % (len(mod_dat),hour,hour+1%24,month))
        st.map(mod_dat)
