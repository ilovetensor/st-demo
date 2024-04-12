import streamlit as st 
import pandas as pd

st.title('Hello World!')
st.subheader("The analysis...")

df = pd.read_csv('data.csv')

st.line_chart(df, x='Date', y='Sales')

df['month'] = pd.to_datetime(df['Date']).dt.month

st.bar_chart(df.groupby('month').sum()['Sales'])