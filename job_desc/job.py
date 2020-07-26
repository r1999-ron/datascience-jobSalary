# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:49:13 2020

@author: KIIT
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image
pickle_in = open("model_file.p", "rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome All"
def predict(Rating,num_comp, hourly, employer_provided, same_state, age):
    
    prediction = classifier.predict([[Rating,num_comp, hourly, employer_provided, same_state, age]])
    print(prediction)
    return prediction

def main():
    st.title("Data Scientist Job Salary")
    html_temp="""
    
    <div style = "background-color:tomato:padding:10px">
    <h2 style = "color:white;text-align:center;">Streamlit Job Salary ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    rating = st.text_input("Rating","Type Here")
    comp = st.text_input("num_comp", "Type Here")
    hour = st.text_input("hourly","Type Here")
    emp = st.text_input("employer_provided","Type Here")
    state = st.text_input("same_state","Type Here")
    found = st.text_input("age","Type Here")    
    result = " "
    if st.button("Predict"):
        result = predict(rating, comp, hour,emp, state, found)
    st.success('The output is {}'.format(result))
    
    if st.button('About'):
        st.text("Let's Learn")
        st.text("Built an streamline App")
if __name__=='__main__':
    main()