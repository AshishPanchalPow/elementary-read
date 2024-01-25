import fitz  # PyMuPDF
import camelot

def extract_text_and_paragraphs(pdf_path):
    text_data = []
    paragraph_data = []

    # Use PyMuPDF to extract text and paragraphs
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text_data.append(page.get_text())
            paragraph_data.extend([paragraph.strip() for paragraph in page.get_text("textblock").split('\n') if paragraph.strip()])

    return text_data, paragraph_data

def extract_tables(pdf_path):
    table_data = []

    # Use camelot-py to extract tables
    tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')

    
    for i, table in enumerate(tables):
        df = table.df
        table_data.append(df)

    return table_data

# if __name__ == "__main__":
#     pdf_path = "path/to/your/file.pdf"

#     # Extract text and paragraphs
#     text_data, paragraph_data = extract_text_and_paragraphs(pdf_path)

#     # Extract tables
#     table_data = extract_tables(pdf_path)

#     # Display the extracted data
#     print("Text Data:")
#     for text in text_data:
#         print(text)

#     print("\nParagraph Data:")
#     for paragraph in paragraph_data:
#         print(paragraph)

#     print("\nTable Data:")
#     for i, table in enumerate(table_data):
#         print(f"Table {i + 1}:\n{table}\n")
