import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

with open('dataset.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

df = pd.read_parquet('datasets/employee_data_completed.parquet')
df.rename(columns={'hora': 'hour'}, inplace=True)

st.title('Original Data Samples Visualization')
st.write('##')
col0, col1, col2 = st.columns(3, gap='small')
col0.metric('Data Rows', df.shape[0])
col1.metric('Data Columns', df.shape[1])
col2.metric('Data Samples', 20000)
st.write('##')

st.dataframe(data=df.head(20000), width=3000, height=550, column_config={'emp_id': st.column_config.NumberColumn(format='%d')})
