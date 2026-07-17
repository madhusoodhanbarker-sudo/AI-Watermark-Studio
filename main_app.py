import streamlit as st
import os

from utils import (
    create_directories,
    save_uploaded_file,
    output_path
)

from image_processor import add_text_watermark as image_watermark
from video_processor import add_text_watermark as video_watermark
from pdf_processor import add_text_watermark as pdf_watermark
from docx_processor import add_text_watermark as docx_watermark

# -----------------------------
# Create folders
# -----------------------------
create_directories()

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Watermark Studio",
    page_icon="💧",
    layout="wide"
)

st.title("💧 AI Watermark Studio")
st.write("Upload an Image, Video, PDF, or Word Document and add a watermark.")

# -----------------------------
# Sidebar Settings
# -----------------------------
st.sidebar.header("Watermark Settings")

watermark_type = st.sidebar.radio(
    "Watermark Type",
    ["Text", "Logo"]
)

watermark_text = "CONFIDENTIAL"

if watermark_type == "Text":
    watermark_text = st.sidebar.text_input(
        "Watermark Text",
        "CONFIDENTIAL"
    )

opacity = st.sidebar.slider(
    "Opacity",
    0,
    255,
    128
)

font_size = st.sidebar.slider(
    "Font Size",
    10,
    100,
    40
)

position = st.sidebar.selectbox(
    "Position",
    [
        "Center",
        "Top Left",
        "Top Right",
        "Bottom Left",
        "Bottom Right"
    ]
)

# -----------------------------
# Upload File
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload File",
    type=[
        "png","jpg","jpeg","webp",
        "mp4","avi","mov","mkv","webm",
        "pdf",
        "docx"
    ]
)

if uploaded_file:

    extension = uploaded_file.name.split(".")[-1].lower()

    st.success("File Uploaded Successfully!")

    if extension in ["png","jpg","jpeg","webp"]:
        st.image(uploaded_file)

    elif extension in ["mp4","avi","mov","mkv","webm"]:
        st.video(uploaded_file)

    elif extension == "pdf":
        st.info("PDF Uploaded")

    elif extension == "docx":
        st.info("Word Document Uploaded")
