from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(
    image_file,
    text="CONFIDENTIAL",
    opacity=128,
    position="Center",
    font_size=40
):
    # Open image
    image = Image.open(image_file).convert("RGBA")

    # Create transparent layer
    watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Calculate text size
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    width, height = image.size

    # Select position
    if position == "Top Left":
        x, y = 20, 20

    elif position == "Top Right":
        x = width - text_width - 20
        y = 20

    elif position == "Bottom Left":
        x = 20
        y = height - text_height - 20

    elif position == "Bottom Right":
        x = width - text_width - 20
        y = height - text_height - 20

    else:  # Center
        x = (width - text_width) // 2
        y = (height - text_height) // 2

    # Draw watermark
    draw.text(
        (x, y),
        text,
        fill=(255, 255, 255, opacity),
        font=font
    )

    # Merge watermark with image
    output = Image.alpha_composite(image, watermark)

    return output.convert("RGB")
