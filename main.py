import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

@st.cache_data()
def load_data():
    return pd.read_csv('datasets/data.csv')

with st.spinner("Loading dataset..."):
       df = load_data()

st.title('My Datascience App')
st.dataframe(df)

st.header('Data Visulization')
st.subheader('Job titles of the employees')
job_count = df['job_title'].value_counts().head(10)


fig1 = px.bar(job_count,
              job_count.index,
              job_count.values,
              title='job titles of the employees')
st.plotly_chart(fig1,use_container_width=True)
st.subheader("these are the popular jobs")
st.info(" ,".join(job_count.index.tolist()))
