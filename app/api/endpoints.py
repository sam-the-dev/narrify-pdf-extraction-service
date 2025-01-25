from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Dict
from ..services.pdf_service import extract_text_from_pdf

router = APIRouter()

@router.get("/")
async def root() -> Dict[str, str]:
    """
    Root endpoint to check if the API is working.
    
    Returns:
        Dict[str, str]: Dictionary containing a message that confirms the API is working
    """
    return {
        "message": "The API is working"
    }


@router.post("/extract-text-from-pdf", response_model=Dict[str, str])
async def extract_text_endpoint(file: UploadFile = File(...)) -> Dict[str, str]:
    """
    Extract text from an uploaded PDF file.
    
    Args:
        file (UploadFile): The PDF file to process
        
    Returns:
        Dict[str, str]: Dictionary containing extracted text and success message
        
    Raises:
        HTTPException: If text extraction fails
    """
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Uploaded file must be a PDF"
        )
    
    try:
        text = await extract_text_from_pdf(file)
        return {
            "extracted_text": text,
            "message": "Text extracted successfully!"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error extracting text: {str(e)}"
        )
    finally:
        await file.close()

