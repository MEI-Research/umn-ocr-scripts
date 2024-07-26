# UMN-OCR-Scripts

This repository includes several options to access the text content in surveys.

## Option 1: Image
Using `ocr.py`, you can specify an image file, and it will print the text output.

## Option 2: Readable PDF to Text
Using `pdf.py`, you can select a readable PDF file, and it will print the text output.

## Option 3: Image to PDF to Text
Using `image2pdf.py`, you can convert an image into a PDF, then use `pdf.py` to print the text output.

## Results
- **Option 1:** Not fully accurate.
- **Option 2:** Very accurate as long as the PDF is original.
- **Option 3:** Did not produce any results.

## Conclusion
If possible, configure the scanner to produce a text-readable PDF instead of an image. This PDF can then be processed with Option 2 for the best results. If not, use Option 1 with a scanned image file.