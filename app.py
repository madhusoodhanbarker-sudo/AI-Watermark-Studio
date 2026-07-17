import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Watermark Studio",
    page_icon="💧",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("💧 AI Watermark Studio")
st.write("Add Text or Logo Watermarks to Images, Videos, PDFs and Word Documents.")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("Watermark Settings")

watermark_type = st.sidebar.radio(
    "Watermark Type",
    ["Text", "Logo"]
)

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload a File",
    type=[
        "png", "jpg", "jpeg", "webp",
        "mp4", "avi", "mov", "mkv", "webm",
        "pdf",
        "docx"
    ]
)

# -------------------------------
# Text Watermark
# -------------------------------
if watermark_type == "Text":
    watermark_text = st.sidebar.text_input(
        "Watermark Text",
        "CONFIDENTIAL"
    )

# -------------------------------
# Logo Watermark
# -------------------------------
else:
    logo = st.sidebar.file_uploader(
        "Upload Logo",
        type=["png", "jpg", "jpeg"]
    )

# -------------------------------
# Watermark Options
# -------------------------------
opacity = st.sidebar.slider(
    "Opacity",
    0,
    100,
    50
)

rotation = st.sidebar.slider(
    "Rotation",
    0,
    360,
    45
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

# -------------------------------
# Display Uploaded File
# -------------------------------
if uploaded_file is not None:

    st.success("File uploaded successfully!")

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension in ["png", "jpg", "jpeg", "webp"]:
        st.image(uploaded_file, caption="Uploaded Image")

    elif extension in ["mp4", "avi", "mov", "mkv", "webm"]:
        st.video(uploaded_file)

    elif extension == "pdf":
        st.info("PDF uploaded successfully.")

    elif extension == "docx":
        st.info("Word document uploaded successfully.")

# -------------------------------
# Process Button
# -------------------------------
if st.button("Apply Watermark"):
    st.success("Watermark processing will start here.")
