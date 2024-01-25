# main.py
from pdf_reader import read_pdf
from extract import extract_plan_information
from comprehensive_read import extract_text_and_paragraphs,extract_tables
from basic_filter import basic_filter

def main():
    file_path = './your_pdf_file.pdf'  # Replace with the path to your PDF file
    text_content = read_pdf(file_path)
    benefits_detail=basic_filter(text_content)
    
        
    final_json=extract_plan_information(text_content)
    # text_data, paragraph_data = extract_text_and_paragraphs(file_path)
    # table_data = extract_tables(file_path)
    # Display the extracted data
    # print("Text Data:")
    # for text in text_data:
    #     print(text)

    # print("\nParagraph Data:")
    # for paragraph in paragraph_data:
    #     print(paragraph)

    # print("\nTable Data:")
    # for i, table in enumerate(table_data):
        #print(f"Table {i + 1}:\n{table}\n")
    print(final_json)

if __name__ == "__main__":
    main()
