def basic_filter(input):
    # Split the string into lines
    # Split the string into lines
# Split the string into lines
# Split the string into lines
    lines = input.split('\n')

    # Find the start index for the desired text
    start_index = next((i for i, line in enumerate(lines) if 'Dental Beneﬁts (In-Network)' in line), None)

    # Find the end index for the desired text
    end_index = len(lines)

    # Iterate through the lines after the start index to find the first occurrence not related to dental benefits
    for i, line in enumerate(lines[start_index + 1:], start=start_index + 1):
        if 'Beneﬁts' in line and 'In-Network' in line and 'Dental' not in line:
            end_index = i
            break

    # Extract the desired text between the start and end indices
    desired_text = '\n'.join(lines[start_index:end_index])

    #print(desired_text)
    lines = desired_text.split('\n')

    # Initialize an empty list to store covered elements
    covered_elements = []

    # Iterate through the lines
    for line in lines:
        # Check if the line starts with a number
        if not line.lstrip().isdigit():
            # Extract covered elements
            if 'Covered' in line:
                covered_elements.append(line.split(':')[0].strip())

    # Print the result
    return covered_elements