import fitz  # PyMuPDF

def extract_subheadings_with_color(pdf_path, subheading_color):
    subheadings = []

    with fitz.open(pdf_path) as pdf_document:
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]

            # Iterate through the text blocks on the page
            for block in page.get_text("blocks"):
                text = block[4]  # Extracting text

                # Check if the block contains text
                if text:
                    color = block[10] if len(block) > 10 else (0, 0, 0)  # Extracting color if available
                else:
                    continue

                # Check if the text color matches the specified subheading color
                if color == subheading_color:
                    subheading = text.strip()
                    subheadings.append(subheading)

    return subheadings

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = 'your_pdf_file.pdf'

# Replace (R, G, B) with the actual RGB color values of your subheading
subheading_color = (37, 150, 90)  # Adjust the color code as needed

# Extract subheadings from the PDF using the specified color
subheadings = extract_subheadings_with_color(pdf_path, subheading_color)

# Print the subheadings
for subheading in subheadings:
    print(subheading)
