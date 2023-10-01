import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator using LangChain")

animal_type = st.text_input("Animal type")
pet_color = st.text_input("Pet color")

st.write(lch.generate_pet_name(animal_type, pet_color))
