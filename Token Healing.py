import re

def heal_tokens(text):
    # Define or creating the healing patterns
    patterns = [
        (r"\b(\w+)\.(\w+)\b", r"\1 DOT \2"),  # Replace dot in the middle of words
        (r"\b(\w+)/(\w+)\b", r"\1 SLASH \2"),  # Replace slash in the middle of words
        (r"\b(\w+)\$(\w+)\b", r"\1 Dollar \2"),  # Replace Dollar in the middle of words
        (r"\b(\w+)\%(\w+)\b", r"\1 PARCENTAGE \2"),  # Replace percentage in the middle of words
        (r"\b(\w+)\&(\w+)\b", r"\1 AMPERSAND \2"),  # Replace ampersand in the middle of words
        (r"\b(\w+)-(\w+)\b", r"\1 HYPHEN \2"),  # Replace hyphen in the middle of words
        (r"\b(\w+)_(\w+)\b", r"\1 UNDERSCORE \2"),  # Replace underscore in the middle of words
        (r"\b(\w+)\|(\w+)\b", r"\1 VERTICAL PIPE \2"),  # Replace vertical pip or bar in the middle of words
    ]

    # Apply healing patterns to the text
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    return text

# Example usage
text = "This$is%an&example/sentence_with-dots|and.hyphens."
healed_text = heal_tokens(text)
print(healed_text)
