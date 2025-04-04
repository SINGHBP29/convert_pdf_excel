import os
import cv2
import pytesseract
import pandas as pd
import numpy as np
from pdf2image import convert_from_path
from io import BytesIO

def preprocess_image(image):
    """Preprocess image for OCR."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    return thresh

def extract_text_from_image(image):
    """Extract text from an image using OCR."""
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def pdf_to_excel(pdf_path):
    """Convert PDF to structured Excel using OCR."""
    images = convert_from_path(pdf_path)
    extracted_data = []

    for img in images:
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
        processed_img = preprocess_image(img_cv)
        extracted_text = extract_text_from_image(processed_img)

        rows = extracted_text.split("\n")
        for row in rows:
            if row.strip():
                extracted_data.append([row])

    df = pd.DataFrame(extracted_data, columns=["Extracted Text"])
    
    # Save to an in-memory Excel file
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    processed_data = output.getvalue()

    return processed_data
