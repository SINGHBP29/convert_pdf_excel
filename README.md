
# 📝 PDF to Excel Converter (OCR-Based)  

### 🔍 Convert Scanned PDFs into Structured Excel Sheets Using OCR  

This project provides an **OCR-based PDF to Excel converter** using **Tesseract OCR, OpenCV, and Streamlit**. It helps extract text from **scanned PDFs** and convert them into a structured **Excel file (.xlsx)** while preserving the tabular format.  

---

## 🚀 Features  

✔️ **Extracts text from scanned PDFs** using **Tesseract OCR**  
✔️ **Preprocessing techniques** for noise reduction & better accuracy  
✔️ **Streamlit Web UI** for easy file upload & download  
✔️ **No need for Tabula or Camelot**  
✔️ **Avoids image conversion**, ensuring direct text extraction  
✔️ **User-friendly & lightweight** solution  

---

## 📂 Project Structure  

```
📁 convert_pdf_excel  
│── 📜 convert_pdf.py       # Core OCR-based PDF to Excel conversion logic  
│── 📜 streamlit_file.py               # Streamlit web app for file upload & download  
│── 📜 requirements.txt     # Required Python dependencies  
│── 📜 README.md            # Project documentation (this file)  
```

---

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

🔹 **Ensure Tesseract is installed** (for Windows users, update the Tesseract path in `convert_pdf.py` if needed).  

---

## 🎯 How to Use  

### 📌 Method 1: Run the Python Script  
```bash
python convert_pdf.py --input input.pdf --output output.xlsx  
```

### 📌 Method 2: Run the Streamlit Web App  
```bash
streamlit run streamlit_file.py  
```

👆 **This will launch a browser-based UI** where you can upload a PDF and download the extracted Excel file.  

---

## 📌 Requirements  

✅ Python 3.7+  
✅ Tesseract OCR (`sudo apt install tesseract-ocr` for Linux)  
✅ Dependencies from `requirements.txt`  

---

## 🏆 Contributors  

👨‍💻 **Bhanu Pratap Singh** - *Developer*  
📌 **GitHub:** [SINGHBP29](https://github.com/SINGHBP29/)  

