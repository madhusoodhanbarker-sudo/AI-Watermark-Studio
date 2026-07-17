import cv2

def add_text_watermark(
    input_video,
    output_video,
    text="CONFIDENTIAL",
    position="Bottom Right",
    font_scale=1,
    color=(255, 255, 255),
    thickness=2
):
    cap = cv2.VideoCapture(input_video)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        text_size = cv2.getTextSize(
            text,
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            thickness
        )[0]

        if position == "Top Left":
            x, y = 20, 40

        elif position == "Top Right":
            x = width - text_size[0] - 20
            y = 40

        elif position == "Bottom Left":
            x = 20
            y = height - 20

        elif position == "Center":
            x = (width - text_size[0]) // 2
            y = height // 2

        else:   # Bottom Right
            x = width - text_size[0] - 20
            y = height - 20

        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            color,
            thickness,
            cv2.LINE_AA
        )

        out.write(frame)

    cap.release()
    out.release()

    return output_video
