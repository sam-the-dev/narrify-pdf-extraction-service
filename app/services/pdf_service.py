import pdfplumber
from fastapi import UploadFile, HTTPException
from app.utils.text_cleaner import clean_text
from io import BytesIO

async def extract_text_from_pdf(file: UploadFile):
    try:
        max_size = 5 * 1024 * 1024

        if not file.content_type == "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="File must be a PDF"
            )

        pdf_content = await file.read()
        
        if len(pdf_content) > max_size:
            raise HTTPException(
                status_code=400,
                detail=f"File size exceeds the maximum limit of {max_size // (1024 * 1024)}MB"
            )

        pdf_file = BytesIO(pdf_content)
        pdf_file.seek(0)

        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        cleaned_text = clean_text(text)
        return text;

    except Exception as e:
        print(f"PDF extraction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the PDF: {str(e)}"
        )
    finally:
        pdf_file.close()