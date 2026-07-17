from PIL import Image, ImageDraw, ImageFont


def create_text_watermark(
    text="CONFIDENTIAL",
    size=(600, 200),
    font_size=40,
    color=(255, 255, 255),
    opacity=128,
    rotation=0
):
    """
    Create a transparent text watermark image.
    """

    watermark = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2

    draw.text(
        (x, y),
        text,
        font=font,
        fill=(
            color[0],
            color[1],
            color[2],
            opacity
        )
    )

    if rotation != 0:
        watermark = watermark.rotate(rotation, expand=True)

    return watermark


def create_logo_watermark(
    logo_path,
    scale=0.25,
    opacity=128
):
    """
    Load and prepare a logo watermark.
    """

    logo = Image.open(logo_path).convert("RGBA")

    width = int(logo.width * scale)
    height = int(logo.height * scale)

    logo = logo.resize(
        (width, height),
        Image.LANCZOS
    )

    alpha = logo.getchannel("A")
    alpha = alpha.point(lambda p: int(p * opacity / 255))

    logo.putalpha(alpha)

    return logo


def apply_watermark(
    image,
    watermark,
    position="Center"
):
    """
    Apply watermark to an image.
    """

    image = image.convert("RGBA")

    width, height = image.size
    wm_width, wm_height = watermark.size

    if position == "Top Left":
        x, y = 20, 20

    elif position == "Top Right":
        x = width - wm_width - 20
        y = 20

    elif position == "Bottom Left":
        x = 20
        y = height - wm_height - 20

    elif position == "Bottom Right":
        x = width - wm_width - 20
        y = height - wm_height - 20

    else:
        x = (width - wm_width) // 2
        y = (height - wm_height) // 2

    image.paste(
        watermark,
        (x, y),
        watermark
    )

    return image.convert("RGB")
