import argparse
from asciinator.transformers import image_to_ascii, gif_to_ascii

def main():
    parser = argparse.ArgumentParser(description="Convert images or GIFs to ASCII art.")
    parser.add_argument("file_path", help="Path to the image or GIF file.")
    parser.add_argument("--width", type=int, default=100, help="Output width of the ASCII art.")
    parser.add_argument("--output", help="Path to save the output file. If not specified, ASCII art is printed on the console.")
    parser.add_argument("--gif", action="store_true", help="Indicate if the input file is a GIF.")

    args = parser.parse_args()

    if args.gif:
        # Process a GIF
        if args.output:
            gif_to_ascii(args.file_path, output_width=args.width, save_to_gif=True, output_gif_path=args.output)
        else:
            print(gif_to_ascii(args.file_path, output_width=args.width, save_to_gif=False))
    else:
        # Process a static image
        if args.output:
            image_to_ascii(args.file_path, output_width=args.width, save_to_file=True, output_file_path=args.output)
        else:
            print(image_to_ascii(args.file_path, output_width=args.width))

if __name__ == "__main__":
    main()
