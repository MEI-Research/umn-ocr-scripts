# Installation instructions: https://www.educative.io/answers/how-to-extract-text-from-an-image-in-python

import pytesseract
from PIL import Image

# Open the image file
image = Image.open('s1.png')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)