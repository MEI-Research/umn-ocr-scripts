# Reference: https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module

# pip install img2pdf
import img2pdf
# pip install pillow
from PIL import Image
import os
 
# storing image path
img_path = "s1.png"
 
# storing pdf path
pdf_path = "new1.pdf"
 
# opening image
image = Image.open(img_path)
 
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
 
# opening or creating pdf file
file = open(pdf_path, "wb")
 
# writing pdf files with chunks
file.write(pdf_bytes)
 
# closing image file
image.close()
 
# closing pdf file
file.close()
 
# output
print("Successfully made pdf file")