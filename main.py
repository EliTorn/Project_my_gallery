import streamlit as st
from data import show

st.title("גלרייה !!")


def get_image():
    data = show()
    for image in data:
        st.image(image['picture'], caption=image['name'])


get_image()
