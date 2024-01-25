import re
import json
from basic_filter import basic_filter

def extract_plan_information(pdf_text):
    # Define regular expressions for extracting information
    plan_name_pattern = re.compile(r'Plan ID: (.+)')
    premium_pattern = re.compile(r'Premium: (.+)')
    deductible_pattern = re.compile(r'Health Deductible: (.+)')
    max_oop_pattern = re.compile(r'Max Out-of-Pocket: (.+)')
    drug_plan_pattern = re.compile(r'Includes Drug Plan: (.+)')
    dental_pattern = re.compile(r'Supplementary Dental Beneﬁts \(In-Network\)(.+?)Supplementary Vision Beneﬁts', re.DOTALL)
    vision_pattern = re.compile(r'Supplementary Vision Beneﬁts \(In-Network\)(.+?)Supplementary Hearing Beneﬁts', re.DOTALL)
    hearing_pattern = re.compile(r'Supplementary Hearing Beneﬁts \(In-Network\)(.+?)Part D Monthly Premiums', re.DOTALL)
    costs_benefits_pattern = re.compile(r'Plan Costs & Beneﬁts(.+?)Part D Monthly Premiums', re.DOTALL)

    # Extract information using regular expressions
    plan_name_match = plan_name_pattern.search(pdf_text)
    premium_match = premium_pattern.search(pdf_text)
    deductible_match = deductible_pattern.search(pdf_text)
    max_oop_match = max_oop_pattern.search(pdf_text)
    drug_plan_match = drug_plan_pattern.search(pdf_text)
    dental_match = dental_pattern.search(pdf_text)
    vision_match = vision_pattern.search(pdf_text)
    hearing_match = hearing_pattern.search(pdf_text)
    costs_benefits_match = costs_benefits_pattern.search(pdf_text)

    # Create a dictionary to store the extracted information
    extracted_info = {
        'Plan_ID': plan_name_match.group(1) if plan_name_match else None,
        'Premium': premium_match.group(1) if premium_match else None,
        'Health_Deductible': deductible_match.group(1) if deductible_match else None,
        'Max_Out_of_Pocket': max_oop_match.group(1) if max_oop_match else None,
        'Includes_Drug_Plan': drug_plan_match.group(1) if drug_plan_match else None,
        'Dental_Benefits': basic_filter(pdf_text),
        #'Costs_and_Benefits': costs_benefits_match.group(1).strip() if costs_benefits_match else None,
    }

    # Convert the dictionary to JSON
    json_data = json.dumps(extracted_info, indent=2)
    
    return json_data

# Example usage
# with open('path/to/your/pdf_content.txt', 'r', encoding='utf-8') as file:
#     pdf_content = file.read()

# result = extract_plan_information(pdf_content)
# print(result)
