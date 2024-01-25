# Provided string
your_string = """
... (your entire string)
Supplementary Dental Beneﬁts (In-Network)
Maximum supplementary dental beneﬁt:
Oral exam: Covered
... (other lines related to dental benefits)
Supplementary Vision Beneﬁts (In-Network)
Maximum supplementary vision beneﬁt:$300.00
Every year
Routine eye exam:$0 Copay
Authorization Required, Referral Required
Eyeglasses (frames and lenses): $0 Copay
Contact lenses: $0 Copay
Supplementary Hearing Beneﬁts (In-Network)
Maximum supplementary hearing beneﬁt:
Fitting/evaluation:$0 Copay
Authorization Required, Referral Required, Limitations Apply
Hearing aids:Covered
Limits may apply
Hearing exam:$0 Copay
Authorization Required, Referral Required
... (remaining lines in your string)
"""

# Split the string into lines
lines = your_string.split('\n')

# Find the start index for the desired text
start_index = next((i for i, line in enumerate(lines) if 'Dental Beneﬁts (In-Network)' in line), None)

# Find the end index for the desired text
end_index = len(lines)

# Iterate through the lines after the start index
for i, line in enumerate(lines[start_index + 1:], start=start_index + 1):
    if "Beneﬁts" in line.strip() and "(In-Network)" in line.strip():
        end_index = i
        break

# Extract the desired text between the start and end indices
desired_text = '\n'.join(lines[start_index:end_index])

print(desired_text)
