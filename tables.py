import tabula

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = './H1468-013-0-17197IL-sob.pdf'

# Read the PDF and extract tables
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Iterate through the tables and print them
for i, table in enumerate(tables, 1):
    print(f"Table {i}:")
    print(table)
    print("\n" + "="*40 + "\n")
