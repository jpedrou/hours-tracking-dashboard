import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

with open('dataset.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

df = pd.read_parquet('datasets/employee_data_completed.parquet')
df.rename(columns={'hora': 'hour'}, inplace=True)

st.title('Original Data Visualization')
st.write('##')
st.dataframe(data=df, width=3000, height=700, column_config={'emp_id': st.column_config.NumberColumn(format='%d')})
