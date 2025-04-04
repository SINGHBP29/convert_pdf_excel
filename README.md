# convert_pdf_excel
# **📌 PDF to Structured Excel Converter using OCR**  

**🔗 GitHub Repository:** [Insert GitHub Link]  

---  

## 🚀 **Project Overview**  
This project extracts tabular data from PDF files and converts it into structured Excel format using OCR techniques. The solution effectively processes scanned or image-based PDFs, making data extraction seamless and automated.  

---  

## 🛠 **Key Features**  
✅ Converts PDFs to Excel using OCR  
✅ Preprocesses images for better text recognition  
✅ Uses adaptive thresholding for noise reduction  
✅ Handles multiple pages in a PDF  
✅ Structured tabular format output  

---  

## 🏗 **Tech Stack Used**  
- **Python** 🐍  
- **OCR (Tesseract)** 📝  
- **OpenCV** 🖼  
- **Pandas** 📊  
- **pdf2image** 📜  
- **Poppler** 🖨  

---  

## 📌 **Installation Guide**  
### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/SINGHBP29/convert_pdf_excel.git
cd convert_pdf_excel
```
  
### **Step 2: Install Required Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Code**  
```bash
python pdf_to_excel.py --input yourfile.pdf --output output.xlsx
```

---  

## 📊 **Workflow**  
1️⃣ Convert PDF pages to images  
2️⃣ Preprocess images for better OCR accuracy  
3️⃣ Extract text from images using **Tesseract OCR**  
4️⃣ Structure extracted text into tabular format  
5️⃣ Save the final output in **Excel (.xlsx)**  

---  

## 🎯 **Usage Example**  
```python
pdf_to_excel("sample.pdf", "output.xlsx")
```
- Input: **Scanned PDF file**  
- Output: **Excel file with structured tabular data**  

---  

## 📬 **Submission Guidelines**  
- **Complete the assignment within 8 hours** ⏳  
- **Upload the project to GitHub** 🖥  
- **Submit the report in the following email format:**  
  ```
  Subject: assignment_nitallahabad_scoreme_rollno
  ```
- **Send the submission to:** `it@scoreme.in` 📩  

---  

## 🔥 **Challenges & Solutions**  
🔹 **Issue:** Extracting structured tables from scanned PDFs  
🔹 **Solution:** Used **OCR & preprocessing techniques** to enhance text recognition  
🔹 **Issue:** Handling multi-page PDFs  
🔹 **Solution:** Processed each page separately & merged results into Excel  

---  

## 🤝 **Contributors**  
👤 **[Your Name]** | [GitHub Profile](https://github.com/yourprofile)  

---  

## 📜 **License**  
This project is licensed under the **MIT License**.  

---

✨ **Happy Coding! 🚀**
