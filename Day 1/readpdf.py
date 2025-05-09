import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # loads page number (0-indexed)
        text = page.get_text()
        print(f"--- Page {page_num + 1} ---")
        print(text)

# Example usage
read_pdf("LAB Exercise.pdf")