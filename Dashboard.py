import calendar
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state="expanded")

def number_to_month(number):
    return calendar.month_name[number]

# df0 = pd.read_excel('datasets/employee_date_hour_0.xlsx')
# df1 = pd.read_excel('datasets/employee_date_hour_1.xlsx')
# df2 = pd.read_excel('datasets/employee_date_hour_2.xlsx')
# df3 = pd.read_excel('datasets/employee_date_hour_3.xlsx')
# df4 = pd.read_excel('datasets/employee_date_hour_4.xlsx')
# df5 = pd.read_excel('datasets/employee_date_hour_5.xlsx')
# df6 = pd.read_json('datasets/employee_performance_evaluation.json', lines=True)


# df_concatened = pd.concat([df0, df1, df2, df3, df4, df5], axis = 0).sort_values(by=['emp_id'])
# df_merged = pd.merge(df_concatened, df6)
# df_merged.to_parquet('datasets/employee_data_completed.parquet', index=None)

df = pd.read_parquet('datasets/employee_data_completed.parquet')
df.rename(columns={'hora': 'hour'}, inplace=True)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


df['month'] = df['data'].dt.month
df['month'] = (df['month']).map(number_to_month)


st.title('Hours Tracking Report')
st.write('##')
col1, col2, col3, col4 = st.columns(4, gap='small')
col1.metric("Number of Employees", df['emp_id'].nunique())
col2.metric('Average Daily Hours Worked', df['hour'].mean().round(2))
col3.metric("Average Employee Satisfaction", df['last_evaluation'].mean().round(2))
col4.metric("Average Employee Satisfaction", df['satisfaction_level'].mean().round(2))

df['day'] = df['data'].dt.day

hours_per_month = df.groupby('month')['hour'].mean().sort_values(ascending=False)
hours_per_day = df.groupby('day')['hour'].mean().sort_values(ascending=False)

col5, col6 = st.columns(2, gap='small')

fig = px.line(hours_per_month, markers=True,title='Averege Worked Hours per Month', text=hours_per_month.round(3))
fig2 = px.scatter(hours_per_day,title='Averege Worked Hours per Day')
col5.plotly_chart(fig, use_container_width=True)
col6.plotly_chart(fig2, use_container_width=True)
