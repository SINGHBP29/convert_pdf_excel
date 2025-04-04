import streamlit as st
from convert_pdf import pdf_to_excel

# Streamlit App Title
st.title("📄 PDF to Excel Converter using OCR")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your PDF file", type="pdf")

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
    
    if st.button("Convert to Excel"):
        st.info("⏳ Processing... Please wait.")
        
        # Save uploaded file temporarily
        temp_pdf_path = "uploaded.pdf"
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.read())

        # Convert PDF to Excel
        excel_data = pdf_to_excel(temp_pdf_path)

        # Provide download button
        st.download_button(label="📥 Download Excel File",
                           data=excel_data,
                           file_name="converted_output.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        # Cleanup
        os.remove(temp_pdf_path)
