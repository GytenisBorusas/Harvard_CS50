
import sys
from PIL import Image



def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    before_image = sys.argv[1]
    after_image = sys.argv[2]

    before_image_lower = before_image.lower()
    after_image_lower = after_image.lower()

    if not (before_image_lower.endswith('.jpg') or before_image_lower.endswith('.jpeg') or
            before_image_lower.endswith('.png')):
        print("Invalid input")
        sys.exit(1)
    elif not (after_image_lower.endswith('.jpg') or after_image_lower.endswith('.jpeg') or
            after_image_lower.endswith('.png')):
        print("Invalid input")
        sys.exit(1)


    if not ((before_image.endswith('.jpg') and after_image.endswith('.jpg')) or
            (before_image.endswith('.jpeg') and after_image.endswith('.jpeg')) or
            (before_image.endswith('.png') and after_image.endswith('.png'))):
        print("Input and output have different extensions")
        sys.exit(1)



    try:
        shirt_img = Image.open("shirt.png")
    except FileNotFoundError:
        print("Error: Could not find 'shirt.png'")
        sys.exit(1)

    before_img = Image.open(before_image)

    # Resize the before image
    resized_before_img = before_img.resize(shirt_img.size)

    # Overlay the images (paste the resized image on top of the shirt image)
    shirt_img.paste(resized_before_img, (0, 0))

    # Save the result as after image
    shirt_img.save(after_image)




if __name__ == "__main__":
    main()