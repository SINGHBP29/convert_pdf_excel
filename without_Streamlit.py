!apt-get install poppler-utils
!sudo apt-get install poppler-utils 
import os
os.environ['PATH'] += os.pathsep + '/usr/bin' # Adding the path to poppler to PATH enviroment variable

import cv2
import pytesseract
import pandas as pd
from pdf2image import convert_from_path
import numpy as np

# Set Tesseract path (Windows users may need this)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image):
    """Apply preprocessing for better OCR accuracy."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)     # Reduce noise
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)  # Thresholding
    return thresh

def extract_text_from_image(image):
    """Extract text from an image using OCR."""
    custom_config = r'--oem 3 --psm 6'  # Set OCR mode (6 = assume a uniform block of text)
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def pdf_to_excel(pdf_path, output_excel):
    """Convert PDF to structured Excel using OCR."""
    images = convert_from_path(pdf_path)  # Convert PDF to images
    extracted_data = []

    for page_num, img in enumerate(images):
        # Convert PIL image to OpenCV format
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

        # Preprocess the image
        processed_img = preprocess_image(img_cv)

        # Extract text using OCR
        extracted_text = extract_text_from_image(processed_img)

        # Split text into rows based on new lines
        rows = extracted_text.split("\n")
        for row in rows:
            if row.strip():  # Ignore empty rows
                extracted_data.append([row])

    # Save extracted data to Excel
    df = pd.DataFrame(extracted_data, columns=["Extracted Text"])
    df.to_excel(output_excel, index=False)

    print(f"✅ Conversion Complete! Excel saved at: {output_excel}")

# 🔥 Run the conversion
pdf_to_excel("/content/test6 (1) (1).pdf", "/content/output.xlsx")
