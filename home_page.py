import streamlit as st
from PIL import Image


def show_home_page():
    """
    This function displays the Home Page.
    """

    st.header("Self Driving Car using Deep Neural Network")
    st.text("")
    st.text("")
    img = Image.open("home.jpg")
    st.image(img, caption="Credits: theweek.com")
    st.text("")

    st.caption("**OVERVIEW :**")
    st.write("""An autonomous vehicle is broadly defined as one equipped with technology that senses the conditions
                around it, including traffic, pedestrians, and physical hazards and can adjust its course and speed
                without a human at the controls. It uses “technology to partially or entirely replace the human driver
                in navigating a vehicle from an origin to a destination while avoiding road hazards and responding to
                traffic conditions.”
              """)
    st.text("")
    st.write("""Self-driving cars see what’s going on around them using three main electronic “eyes”—radar, cameras and
                laser-based LiDar, which stands for light detection and ranging. All three feed data into on-board
                processors, using sophisticated software, algorithms and machine learning to send signals to the
                vehicle’s actuators to trigger appropriate actions such as braking, steering and acceleration.
             """)
    st.text("")
    st.write("""Self-driving cars offer a number of advantages over vehicles requiring hands-on drivers including
                convenience, access to mobility, efficiency, cost-savings and traffic congestion. For those incapable of
                driving due to age or disabilities or without access to conventional methods of public transportation,
                self-driving taxis and other transit vehicles are seen as a way to provide mobility to get to errands,
                work or medical appointments. Commercial operators see self-driving vehicles as boosting cost-savings
                and efficiency because they can run for longer hours without having to stop for meals or breaks, and
                they require fewer employees.
             """)
    st.divider()

    st.caption("**OBJECTIVE :**")
    st.markdown("""For every image, there is an angle associated with it. This angle basically tells us the "angle
                   at which the steering was at that current moment". **Now with the help of a given image, we need to
                   predict the angle of tilt for our steering wheel**.
                """)
    st.divider()

    st.caption("**DATA DESCRIPTION :**")
    st.write("Dataset : [link](https://github.com/SullyChen/driving-datasets)")
    st.markdown("""We have 2 datasets. One was published in **2017** while the other was published in  **2018**. We will
                   use the later one.
                """)
    st.markdown("Data file's information :")
    img = Image.open("sdc_data.jpg")
    st.image(img)
    st.markdown("""As we can see in the above image, after unzipping the original file we get 2 things: **1. data folder**
                   which contains all the images and **2. data.txt** file which contains information such as the name of
                   that image, corresponding angle of each image, date and time. We have a total of **~47 minutes** of data
                   and **for each second we have ~23 images**. So in total we have roughly **~63k images(47x60x23)**
                """)
    st.divider()

    st.caption("""**LIBRARIES : `cv2`, `matplotlib`, `numpy`, `pandas`, `pickle`, `PIL`,
                `scikit-learn`, `scipy`, `seaborn`, `streamlit`, `tensorflow`**""")
