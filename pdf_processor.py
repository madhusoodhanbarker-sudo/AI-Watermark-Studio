import fitz  # PyMuPDF

def add_text_watermark(
    input_pdf,
    output_pdf,
    text="CONFIDENTIAL",
    font_size=40,
    color=(1, 0, 0),
    opacity=0.3
):
    # Open PDF
    pdf = fitz.open(input_pdf)

    # Process each page
    for page in pdf:
        rect = page.rect

        # Center position
        x = rect.width / 2 - 100
        y = rect.height / 2

        # Add watermark
        page.insert_text(
            (x, y),
            text,
            fontsize=font_size,
            color=color,
            rotate=45,
            fill_opacity=opacity
        )

    # Save output
    pdf.save(output_pdf)
    pdf.close()

    return output_pdf
  
