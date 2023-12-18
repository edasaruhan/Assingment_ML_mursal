import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
lm = data['model']

def show_lm_predict():
    st.title("Municipal Solid Waste Prediction with LR")


    st.write("""### Input Information Is needed""")

    gdp = st.number_input('GDP')
    population = st.number_input('Population')
    hazardous = st.number_input('Hazardous')
    electronic = st.number_input('Electronic')

    ok = st.button('Calculate MSW')
    if ok:
        X = X = np.array([gdp, population, hazardous, electronic]).reshape(1, -1)
        msw = lm.predict(X)
        st.subheader(f"The Estimated MSW with LR is {msw[0]:.3}")