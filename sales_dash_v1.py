import streamlit as st
import pandas as pd

df = pd.read_csv('data_sheet.csv')

date1 = st.selectbox('Start Date',options = [1,2,...,365])
date2 = st.selectbox('End Date', options = [1,2,...,365])

st.dataframe(df)
