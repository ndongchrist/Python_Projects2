from PIL import Image, ImageDraw, ImageFont

# Open the invitation card image
image = Image.open('marriage_inv.jpg')

# Set the font size and color
font_size = 70
font_color = (0, 0, 0)  # black color

# Set the position to add the name
name_x = 620
name_y = 490

# Load the font
font = ImageFont.truetype('Font.ttf', font_size)

# Open a file containing the list of names
with open('names.txt', 'r') as file:
    names = file.readlines()

# Iterate over the list of names
for name in names:
    # Create a copy of the original image
    modified_image = image.copy()

    # Create a drawing object
    draw = ImageDraw.Draw(modified_image)

    # Add the name to the image
    draw.text((name_x, name_y), name.strip(), font=font, fill=font_color)

    # Save the modified image with the name
    modified_image.save(f"Edited_inv/{name}_inv_card_{name.strip()}.jpg")