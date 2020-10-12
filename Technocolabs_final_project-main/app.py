import streamlit as st
import pickle as pickle
import numpy as np
model = pickle.load(open('blood_donation.pickle', 'rb'))

st.title("Blood donation predictor")
st.subheader("Please Enter the following details :")

recency = st.number_input('number of months since the last donation')

frequency = st.number_input('total number of donations done')
blood = st.number_input('total blood donated in c.c.')
time = st.number_input('number of months since the first donation')

if st.button("Predict"):
    predicts = model.predict([[recency,frequency,blood,time]])
    output = round(predicts[0], 2)
   # probability = model.predict_proba(recency,frequency,blood,time)
    #y = probability[0]
    #y = max(y)
    #z = int(round(y * 100))
    if output == 1:
        st.success("You might successfully donate blood next month")
        st.balloons()
    else:
        st.warning("You might not donate blood next month ")
        

st.sidebar.header("     About this App")
st.sidebar.text(
    " This app predicts if the user will \n donate in the next month \n based on the previous donations \n of the user")

st.markdown("""
<style>
body {
    color: #111;
    background-color:#AB9F38;
}
.sidebar .sidebar-content {
        background-image:
        background-color:linear-gradient(#474D49,#474D49);
        color: black;
    }
</style>
    """, unsafe_allow_html=True)
