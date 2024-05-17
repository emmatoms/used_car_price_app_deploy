import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page



page =  st.sidebar.selectbox("Your Car Value or Explore", ("Your Car Value", "Explore"))

if page == "Your Car Value":
    show_predict_page()
else:
    show_explore_page()