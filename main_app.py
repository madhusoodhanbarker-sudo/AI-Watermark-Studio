import streamlit as st
import os

from utils import create_directories

# Create required folders
create_directories()

st.set_page_config(
    page_title="AI Watermark Studio",
    page_icon="💧",
    layout="wide"
)

st.title("💧 AI Watermark Studio")
st.write("Add Text or Logo Watermarks to Images, Videos, PDFs, and Word Documents.")

uploaded_file = st.file_uploader(
    "Upload a File",
    type=[
        "png", "jpg", "jpeg", "webp",
        "mp4", "avi", "mov", "mkv", "webm",
        "pdf", "docx"
    ]
)

if uploaded_file:
    ext = uploaded_file.name.split(".")[-1].lower()

    if ext in ["png", "jpg", "jpeg", "webp"]:
        st.success("Image uploaded successfully.")
        st.image(uploaded_file)

    elif ext in ["mp4", "avi", "mov", "mkv", "webm"]:
        st.success("Video uploaded successfully.")
        st.video(uploaded_file)

    elif ext == "pdf":
        st.success("PDF uploaded successfully.")

    elif ext == "docx":
        st.success("Word document uploaded successfully.")

if st.button("Apply Watermark"):
    st.info("Connect this button to image_processor.py, video_processor.py, pdf_processor.py, or docx_processor.py.")
