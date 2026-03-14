import pdfplumber

def extract_reviews_from_pdf(path: str):

    reviews = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                # Assume reviews separated by newline
                page_reviews = text.split("\n\n")
                reviews.extend(page_reviews)

    return [r.strip() for r in reviews if len(r.strip()) > 20]