from PIL import Image, ImageEnhance

# Open an image file
with Image.open('947678.png') as img:
    # Create enhancer
    enhancer = ImageEnhance.Brightness(img)

    # Decrease the brightness to darken the image
    img_darkened = enhancer.enhance(0.25)  # Decrease brightness by 75%

    # Make the image transparent
    img_darkened = img_darkened.convert("RGBA")  # Ensure the image has an alpha channel
    img_darkened.putalpha(64)  # Set alpha to 128. Change this to the transparency level you want.

    # Save the transparent image with a new name
    img_darkened.save('transparent_image.png')