import os
from utils import save_uploaded_file, output_path
from image_processor import add_text_watermark as image_watermark
from video_processor import add_text_watermark as video_watermark
from pdf_processor import add_text_watermark as pdf_watermark
from docx_processor import add_text_watermark as docx_watermark

os.makedirs("temp", exist_ok=True)
os.makedirs("output", exist_ok=True)

if st.button("Apply Watermark"):

    if uploaded_file is None:
        st.warning("Please upload a file first.")

    else:
        # Save uploaded file
        input_path = save_uploaded_file(uploaded_file)
        output_path_file = output_path(uploaded_file.name)

        ext = uploaded_file.name.split(".")[-1].lower()

        if ext in ["png", "jpg", "jpeg", "webp"]:

            result = image_watermark(
                input_path,
                text=watermark_text,
                opacity=128,
                position=position,
                font_size=40
            )

            result.save(output_path_file)

            st.image(result)
            st.success("Image Watermarked Successfully")

            with open(output_path_file, "rb") as f:
                st.download_button(
                    "Download Image",
                    f,
                    file_name=os.path.basename(output_path_file)
                )

        elif ext in ["mp4", "avi", "mov", "mkv", "webm"]:

            video_watermark(
                input_path,
                output_path_file,
                text=watermark_text,
                position=position
            )

            st.video(output_path_file)

            with open(output_path_file, "rb") as f:
                st.download_button(
                    "Download Video",
                    f,
                    file_name=os.path.basename(output_path_file)
                )

        elif ext == "pdf":

            pdf_watermark(
                input_path,
                output_path_file,
                text=watermark_text
            )

            with open(output_path_file, "rb") as f:
                st.download_button(
                    "Download PDF",
                    f,
                    file_name=os.path.basename(output_path_file)
                )

        elif ext == "docx":

            docx_watermark(
                input_path,
                output_path_file,
                text=watermark_text
            )

            with open(output_path_file, "rb") as f:
                st.download_button(
                    "Download DOCX",
                    f,
                    file_name=os.path.basename(output_path_file)
                )

        st.success("Processing Completed Successfully!")
