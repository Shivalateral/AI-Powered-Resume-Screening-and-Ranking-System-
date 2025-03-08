import fitz  # PyMuPDF
import logging

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)  # Open the PDF
        if doc.page_count == 0:
            raise Exception(f"The PDF {pdf_path} has no pages.")
        
        text = ""
        for page in doc:
            text += page.get_text("text")  # Extract text from each page
        return text
    except Exception as e:
        logging.error(f"Error processing file {pdf_path}: {str(e)}")
        raise ValueError(f"Error processing file {pdf_path}: {str(e)}")
