import streamlit as st
import pandas as pd

df = pd.read_csv('data_sheet.csv')

st.dataframe(df)
