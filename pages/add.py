import streamlit as st
from data import connect

st.title("הוספת תמונה")
c1, c2 = st.columns(2)


def get_image():
    upl_image = c1.button('צלם')
    if upl_image:
        text = st.text_input("What is the title of the image", "")
        image = st.camera_input("Capture Image")

        if image is not None:
            image_bit = image.read()
            st.image(image, text)
            connect(text, image_bit)
            st.success("התמונה הועלתה בהצלחה")


def get_video():
    upl_video = c2.button("העלה תמונה")
    if upl_video:
        text = text = st.text_input("What is the title of the image", "")
        video_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
        if video_file and text:
            st.image(video_file, text)
            connect(text, video_file)
            st.success("התמונה הועלה בהצלחה")


get_image()
get_video()
