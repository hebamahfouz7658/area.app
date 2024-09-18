import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('/content/housing.csv')
data.head()
%%writefile app.py
st.time
st.sidebar.title('sidebar')
st.header("calculating area")
with st.sidebar:
  choose=st.selectbox('choose the shape',['circle','rectangle'])
if choose=='circle':
  r=st.number_input("enter radius",min_value=1,max_value=100)
  area=r*r*3.14
elif choose =='rectangle':
     w=st.number_input("enter width",min_value=1,max_value=100)
     h=st.number_input("enter height",min_value=1,max_value=100)
     area=h*w
     st.button("calculate")
     if btn:
       with st.spinner('loading....'):
          time.sleep(2)
       st.write(f"the area is {area}")

