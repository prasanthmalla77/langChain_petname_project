import langchain_helper as lch
import streamlit as st

st.title("study plan Generator using LangChain")

role = st.text_input("Animal type")
months = st.text_input("Pet color")

st.write(lch.generate_pet_name(role, months))
