#libraries
import io
import pymupdf  # PyMuPDF


def extract_text_from_cv(uploaded_file : ...) -> str | None:
    try:
        # Read uploaded file as BytesIO
        cv_data = pymupdf.open(stream=io.BytesIO(uploaded_file.file.read()), filetype="pdf")
        full_text = []

        for page_num in range(cv_data.page_count):
            page = cv_data.load_page(page_num)
            page_text = page.get_text("text")  # Extract plain text
            full_text.append(page_text)

        cv_data.close()
        return "\n".join(full_text)
    except Exception as e:
        return f"Error reading PDF: {e}"

"""def extract_text_from_cv_path(pdf_path: str) -> str | None:

    try:
        doc = pymupdf.open(pdf_path)
        full_text = []
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            page_text = page.get_text("text") # Extract plain text
            full_text.append(page_text)
        doc.close()
        return "\n".join(full_text) # Join pages with a newline
    except Exception as e:
        print(f"Error reading PDF (PyMuPDF) '{pdf_path}': {e}")
        return None"""





#print(extract_text_from_cv(r"D:\Work\Projects\Ultragenius\Monil\Kavi\onboarding_process\CVs\Ninad AIML.pdf"))