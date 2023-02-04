import streamlit as st
import pandas as pd

df = pd.read_csv('data_sheet.csv')
branch_list = df.BRANCH_CODE.unique().tolist()
branch_list.insert(0,'ALL')

col1, col2, col3, col4, col5 = st.columns(5)

date1 = col1.selectbox('Start Date',options = [1,2,...,365])
date2 = col2.selectbox('End Date', options = [1,2,...,365])
branch = col3.selectbox('Select Branch',options = branch_list)

st.dataframe(df)
