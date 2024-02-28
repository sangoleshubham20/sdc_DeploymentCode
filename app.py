from home_page import show_home_page
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st

img = Image.open("sdc.jpg")
page_config = {"page_title": "Self Driving Car", "page_icon": img, "layout": "centered"}
st.set_page_config(**page_config)

page = option_menu(
    menu_title=None,
    options=["Home", "Model in Action", "Code"],
    icons=["house-fill", "motherboard", "file-earmark-code"],
    default_index=0,
    orientation="horizontal",
    styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "12px"},
            "nav-link": {
                "font-size": "12px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "red"}
            }
)

# Home page
if page == "Home":
    show_home_page()

# Model in Action
if page == "Model in Action":
    st.text("")
    st.write("""**After taking predictions from the model, below is a nice visualization of pictures and rotated steering
                angle based on model prediction.**
             """)
    st.text("")
    video_file = open('sdc.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


# Code page
if page == "Code":

    st.text("")
    st.write("###### If you are more interested in the code you can directly jump into these repositories :")
    st.text("")
    st.caption("**DEPLOYMENT : [link](https://github.com/sangoleshubham20/sdc_DeploymentCode)**")
    st.caption("**MODELLING : [link](https://github.com/sangoleshubham20/sdc_ModellingCode)**")