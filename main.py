import streamlit as st
from pathlib import Path

# Set page config (optional)
st.set_page_config(page_title="DeepVision", page_icon="🔍", layout="wide")

# Define image path (ensuring compatibility in deployment)
def get_image_path(image_name):
    return str(Path(__file__).parent / "static" / image_name)

# Main content
st.title("Welcome to DeepVision")
st.write("AI-powered image generation at its best! 🚀")

# Display images
c1, c2, c3 = st.columns(3)
with c1:
    st.image(get_image_path("image1.webp"))
with c2:
    st.image(get_image_path("image2.webp"))
with c3:
    st.image(get_image_path("image3.webp"))

c4, c6 = st.columns(2)
with c4:
    st.image(get_image_path("image4.webp"))
with c6:
    st.image(get_image_path("image6.webp"))

c7, c8, c9 = st.columns(3)
with c7:
    st.image(get_image_path("image7.webp"))
with c8:
    st.image(get_image_path("image8.webp"))
with c9:
    st.image(get_image_path("image9.webp"))
