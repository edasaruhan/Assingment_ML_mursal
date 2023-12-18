import streamlit as st
from lm_predict_page import show_lm_predict
from ann_predict_page import show_ann_predict

pages = st.sidebar.selectbox('Choose a Model', ('LR Model','ANN Model'))
if pages == 'LR Model':
    show_lm_predict()
else:
    show_ann_predict()