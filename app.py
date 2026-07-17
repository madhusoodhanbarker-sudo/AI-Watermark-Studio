import streamlit as st

from modules.image_watermark import image_watermark_ui
from modules.video_watermark import video_watermark_ui
from modules.pdf_watermark import pdf_watermark_ui
from modules.word_watermark import word_watermark_ui

st.set_page_config(
    page_title="AI Watermark Studio",
    page_icon="💧",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:38px;
    font-weight:bold;
    color:#0E76FD;
}
.sub-title{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}
.stButton>button{
    width:100%;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown('<p class="main-title">💧 AI Watermark Studio</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="sub-title">Add Text & Logo Watermarks to Images, Videos, PDF and Word Documents</p>',
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙️ Navigation")

page = st.sidebar.radio(
    "Choose Module",
    [
        "🏠 Home",
        "🖼 Image Watermark",
        "🎥 Video Watermark",
        "📄 PDF Watermark",
        "📝 Word Watermark",
        "ℹ️ About",
    ],
)

# -----------------------------
# Home
# -----------------------------
if page == "🏠 Home":

    st.header("Welcome")

    st.write("""
AI Watermark Studio is an all-in-one Streamlit application for adding
professional watermarks to multiple file formats.

### Supported Files

- PNG
- JPG
- JPEG
- WEBP

- MP4
- AVI
- MOV
- MKV
- WEBM

- PDF

- DOCX

---

### Features

✅ Text Watermark

✅ Logo Watermark

✅ Adjustable Opacity

✅ Rotation

✅ Scaling

✅ Position Selection

✅ Batch Processing

✅ Download Processed Files
""")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🖼 Image Watermark")

        st.write("""
- Text
- Logo
- Transparency
- Rotation
- Tiling
- Font Size
- Color
""")

    with col2:
        st.info("🎥 Video Watermark")

        st.write("""
- Text
- Logo
- FFmpeg
- OpenCV
- Preview
- Download
""")

    col3, col4 = st.columns(2)

    with col3:
        st.info("📄 PDF Watermark")

        st.write("""
- Text
- Logo
- Entire PDF
- Selected Pages
- Diagonal Watermark
""")

    with col4:
        st.info("📝 Word Watermark")

        st.write("""
- Header Watermark
- Logo
- Draft
- Confidential
- Save DOCX
""")

# -----------------------------
# Image Module
# -----------------------------
elif page == "🖼 Image Watermark":
    image_watermark_ui()

# -----------------------------
# Video Module
# -----------------------------
elif page == "🎥 Video Watermark":
    video_watermark_ui()

# -----------------------------
# PDF Module
# -----------------------------
elif page == "📄 PDF Watermark":
    pdf_watermark_ui()

# -----------------------------
# Word Module
# -----------------------------
elif page == "📝 Word Watermark":
    word_watermark_ui()

# -----------------------------
# About
# -----------------------------
elif page == "ℹ️ About":

    st.header("About AI Watermark Studio")

    st.write("""
### Built With

- Streamlit
- Pillow
- OpenCV
- MoviePy
- FFmpeg
- PyMuPDF
- python-docx
- ReportLab
- NumPy

---

### Project Features

✔ Image Watermark

✔ Video Watermark

✔ PDF Watermark

✔ Word Watermark

✔ Batch Processing

✔ Text & Logo Watermarks

✔ Custom Fonts

✔ Adjustable Opacity

✔ Rotation

✔ Position Selection

✔ Download Processed Files

---

Made with ❤️ using Python and Streamlit.
""")
