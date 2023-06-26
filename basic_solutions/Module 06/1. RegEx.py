# You are given a text document that contains various lines of text. Your task is to create a Python class that utilizes regular expressions to perform the following operations:
#
# 1.	Extract all the email addresses from the text document.
# 2.	Replace all occurrences of a given pattern with a specified replacement string.
# 3.	Split the text document into a list of sentences.
# 4.	Find and print all the occurrences of a particular pattern in the text document.
# Your class should have the following methods:
# 1.	extract_emails(text): This method takes a string text as input and uses the re.search function to find and extract all the email addresses present in the text. It should return a list of extracted email addresses.
# 2.	replace_pattern(text, pattern, replacement): This method takes a string text, a regular expression pattern, and a replacement string replacement. It uses the re.sub function to replace all occurrences of the pattern in the text with the specified replacement string. It should return the modified text.
# 3.	split_sentences(text): This method takes a string text as input and uses the re.split function to split the text into a list of sentences. It should return the list of sentences.
# 4.	find_pattern(text, pattern): This method takes a string text and a regular expression pattern as input. It uses the re.finditer function to find all occurrences of the pattern in the text and prints them.

import re


class TextProcessor:
    def extract_emails(self, text):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}\b'
        emails = re.findall(pattern, text)
        return emails

    def replace_pattern(self, text, pattern, replacement):
        modified_text = re.sub(pattern, replacement, text)
        return modified_text

    def split_sentences(self, text):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return sentences

    def find_pattern(self, text, pattern):
        matches = re.finditer(pattern, text)
        for match in matches:
            print("Match found:", match.group())

# Example usage:
doc = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Email addresses: john.doe@example.com, jane_smith@example.com, info@example.com.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius nisl id urna blandit, 
eu fringilla nunc consequat. Nulla facilisi.
"""

processor = TextProcessor()

# Extract email addresses
emails = processor.extract_emails(doc)
print("Extracted emails:", emails)

# Replace pattern
modified_doc = processor.replace_pattern(doc, r'Lorem', 'REPLACED')
print("Modified doc:\n", modified_doc)

# Split sentences
sentences = processor.split_sentences(doc)
print("Sentences:", sentences)

# Find pattern
processor.find_pattern(doc, r'\b\w+@example\.com\b')
