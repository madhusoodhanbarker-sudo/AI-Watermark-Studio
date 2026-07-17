import os
import shutil
from pathlib import Path


# ----------------------------
# Create folders if missing
# ----------------------------
def create_directories():
    folders = [
        "temp",
        "output",
        "assets",
        "assets/fonts"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


# ----------------------------
# Save uploaded file
# ----------------------------
def save_uploaded_file(uploaded_file, folder="temp"):
    create_directories()

    file_path = os.path.join(folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


# ----------------------------
# Get file extension
# ----------------------------
def get_extension(filename):
    return Path(filename).suffix.lower()


# ----------------------------
# Check image file
# ----------------------------
def is_image(filename):
    return get_extension(filename) in [
        ".png",
        ".jpg",
        ".jpeg",
        ".webp"
    ]


# ----------------------------
# Check video file
# ----------------------------
def is_video(filename):
    return get_extension(filename) in [
        ".mp4",
        ".avi",
        ".mov",
        ".mkv",
        ".webm"
    ]


# ----------------------------
# Check PDF
# ----------------------------
def is_pdf(filename):
    return get_extension(filename) == ".pdf"


# ----------------------------
# Check DOCX
# ----------------------------
def is_docx(filename):
    return get_extension(filename) == ".docx"


# ----------------------------
# Output filename
# ----------------------------
def output_path(filename):
    create_directories()

    name = Path(filename).stem
    ext = Path(filename).suffix

    return os.path.join(
        "output",
        f"{name}_watermarked{ext}"
    )


# ----------------------------
# Delete temp folder
# ----------------------------
def clear_temp():
    if os.path.exists("temp"):
        shutil.rmtree("temp")

    os.makedirs("temp", exist_ok=True)
