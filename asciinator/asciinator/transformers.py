from PIL import Image, ImageSequence, ImageDraw, ImageFont
import numpy as np


def image_to_ascii(
    image_path, output_width=100, save_to_file=False, output_file_path="ascii_art.txt"
):
    # ASCII characters from dark to light
    ascii_chars = "@%#*+=-:. "

    # Load the image and convert to grayscale
    img = Image.open(image_path).convert("L")

    # Resize the image
    original_width, original_height = img.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(output_width * aspect_ratio)
    img = img.resize((output_width, new_height))

    # Convert image to numpy array
    img_np = np.array(img)

    # Normalize pixel values to match the ASCII scale
    img_normalized = (img_np - img_np.min()) / (img_np.max() - img_np.min())
    img_scaled = (img_normalized * (len(ascii_chars) - 1)).astype(int)

    # Map normalized pixels to ASCII characters
    ascii_image = "\n".join(
        "".join(ascii_chars[pixel] for pixel in row) for row in img_scaled
    )

    # Output the ASCII Art
    if save_to_file:
        with open(output_file_path, "w") as file:
            file.write(ascii_image)
        print(f"ASCII art saved to {output_file_path}")
    else:
        return ascii_image


def gif_to_ascii(
    gif_path, output_width=100, save_to_gif=True, output_gif_path="ascii_art.gif"
):
    # ASCII characters from dark to light
    ascii_chars = "@%#*+=-:. "

    # Load the GIF
    gif = Image.open(gif_path)

    # Prepare to create ASCII frames
    ascii_frames = []
    durations = []

    for frame in ImageSequence.Iterator(gif):
        # Convert frame to grayscale
        frame = frame.convert("L")

        # Resize the frame
        original_width, original_height = frame.size
        aspect_ratio = original_height / float(original_width)
        new_height = int(output_width * aspect_ratio)
        frame = frame.resize((output_width, new_height))

        # Convert frame to numpy array
        frame_np = np.array(frame)

        # Normalize pixel values to match the ASCII scale
        frame_normalized = (frame_np - frame_np.min()) / (
            frame_np.max() - frame_np.min()
        )
        frame_scaled = (frame_normalized * (len(ascii_chars) - 1)).astype(int)

        # Map normalized pixels to ASCII characters
        ascii_frame = "\n".join(
            "".join(ascii_chars[pixel] for pixel in row) for row in frame_scaled
        )

        # Create an image from ASCII characters
        # Estimate size based on the dimensions of the ASCII frame
        ascii_img_size = (
            output_width * 7,
            new_height * 15,
        )  # Adjust multiplier as needed
        ascii_img = Image.new("L", ascii_img_size, "white")
        draw = ImageDraw.Draw(ascii_img)
        draw.text((0, 0), ascii_frame, fill="black")

        ascii_frames.append(ascii_img)
        durations.append(frame.info.get("duration", 100))  # Default duration: 100ms

    # Save frames as an animated GIF
    ascii_frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=ascii_frames[1:],
        loop=0,
        duration=durations,
        optimize=False,
    )

    if save_to_gif:
        print(f"ASCII art GIF saved to {output_gif_path}")
