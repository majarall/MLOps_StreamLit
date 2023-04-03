import streamlit as st 
import pandas as pd 
import numpy as np 

#TODO - Step 0 - Quick env setup
#TODO - Step 1 - Streamlit 101
#TODO - Step 2 - Emulate a model service using Huggingface inference API 
#TODO - Step 3 - Deploy the app (create Github repo)


#st.write(""" Hello world, first time using *streamlit*""")
#st.text("What is the differece between the methods st.write() and st.text()")

"""
df = pd.read_csv("./avocado.csv")
df_small = df[['year','Total Bags']]

st.line_chart(df_small)
"""

if st.checkbox("Show dataframe"):
    df1 = pd.DataFrame({
        'Apple' : [12,12,23],
        'Orange' : [13,2,3]
    })

    df1


#map_data = pd.DataFrame(np.random.randn(1000,2) / [50,50] + [59.9, 10.75], columns=['lat', 'lon'])
#st.map(map_data)

x = st.slider('x') #this is a widget 
st.write(x, "squared is", x*x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name