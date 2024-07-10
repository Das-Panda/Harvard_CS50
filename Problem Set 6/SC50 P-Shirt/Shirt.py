import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python Shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Check if the file extensions are correct and match
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png"]

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid file extension. Only .jpg, .jpeg, or .png files are allowed.")
    if input_ext != output_ext:
        sys.exit("Input and output file extensions do not match.")

    # Check if the input file exists
    if not os.path.exists(input_path):
        sys.exit("Input file does not exist.")

    try:
        # Open the input image and shirt image
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")

        # Resize and crop the input image to match the shirt image's size
        fitted_image = ImageOps.fit(input_image, shirt_image.size, method=0, bleed=0.0, centering=(0.5, 0.5))

        # Overlay the shirt image on the fitted input image
        fitted_image.paste(shirt_image, shirt_image)

        # Save the result to the output file
        fitted_image.save(output_path)

    except FileNotFoundError:
        sys.exit("Input file not found.")

if __name__ == "__main__":
    main()