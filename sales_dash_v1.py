import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('data_sheet.csv')

col1, col2, col3, col4, col5 = st.columns(5)

date1 = col1.selectbox('Start Date',options = list(range(1,366)))
date2 = col2.selectbox('End Date', options = list(range(1,366)))

branch_list = df.BRANCH_CODE.unique().tolist()
branch_list.insert(0,'COUNTRY')
branch = col3.selectbox('Select Branch',options = branch_list)


if branch == 'COUNTRY':
  emp_list = df.EMP_ID.unique().tolist()
else:
  emp_list = df['EMP_ID'][(df['BRANCH_CODE']==branch)].unique().tolist()

emp_list.insert(0,'OVERALL')
emp = col4.selectbox('Select EMP_ID',options = emp_list)

product_list = df.PRODUCT_CODE.unique().tolist()
product_list.insert(0,'ALL')
product = col5.selectbox('PRODUCT_CODE',options = product_list)

f1 = (df['LOGIN_DATE']>=date1)
f2 = (df['LOGIN_DATE'] <= date2)

if branch == 'COUNTRY':
  f3 = (1==1)
else:
  f3 = (df['BRANCH_CODE']==branch)
if emp == 'OVERALL':
  f4 = (1==1)
else:
  f4 = (df['EMP_ID']==emp)
if product == 'ALL':
  f5 = (1==1)
else:
  f5 = (df['PRODUCT_CODE']==product)

filter = (f1 & f2 & f3 & f4 & f5)

tab1,tab2 = st.tabs(['Summary','Reportee View'])

with tab1:
  col1, col2 = st.columns(2)
  col1.dataframe(df)
  col2.dataframe(df[filter])

summary0 = df[filter].groupby('FLAG2')["LOGIN_FLAG","INCOME_SANCTION_FLAG","FINAL_SANCTION_FLAG","BOOKING_FLAG"].sum()
#summary1 = pd.melt(summary0, id_vars=['FLAG2'],value_vars = ["LOGIN_FLAG","INCOME_SANCTION_FLAG","FINAL_SANCTION_FLAG","BOOKING_FLAG"])
#summary1 = pd.melt(summary0, id_vars =['FLAG2'], value_vars =["LOGIN_FLAG","INCOME_SANCTION_FLAG","FINAL_SANCTION_FLAG","BOOKING_FLAG"])
st.dataframe(summary0)
#st.dataframe(summary1)

#fig_one = px.bar()
