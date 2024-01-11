sentence = input("Enter a sentence: ")

# Check if the sentence has at least 10 characters
if len(sentence) >= 10:
    extracted_substring = sentence[4:10]  # Note: Python uses 0-based indexing
    print("Extracted Substring:", extracted_substring)
else:
    print("Input sentence should have at least 10 characters.")