import streamlit as st
import pandas as pd

df = pd.read_csv('data_sheet.csv')

col1, col2, col3, col4, col5 = st.columns(5)

date1 = col1.selectbox('Start Date',options = [1,2,...,365])
date2 = col2.selectbox('End Date', options = [1,2,...,365])

branch_list = df.BRANCH_CODE.unique().tolist()
branch_list.insert(0,'COUNTRY')
branch = col3.selectbox('Select Branch',options = branch_list)


if branch == 'COUNTRY':
  emp_list = df.EMP_ID.unique().tolist()
else:
  emp_list = df['EMP_ID'][(df['BRANCH_CODE']==branch)].unique().tolist()

emp_list.insert(0,'Overall')
emp = col4.selectbox('Select EMP_ID',options = emp_list)

product_list = df.PRODUCT_CODE.unique().tolist()
product_list.insert(0,'ALL')
product = col5.selectbox('Select PRODUCT_CODE',options = product_list)





st.dataframe(df)
