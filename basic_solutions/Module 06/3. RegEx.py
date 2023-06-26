# You are given an HTML file containing various elements. Your task is to create a Python class that utilizes regular expressions to perform the following operations:
#
# 1.	Extract all the URLs from the HTML file.
# 2.	Replace all occurrences of a given tag with a specified replacement string.
# 3.	Split the HTML file into a list of HTML elements.
# 4.	Find and print all the attributes of a specific tag in the HTML file.
#
# Your class should have the following methods:
#
# 1.	extract_urls(html): This method takes a string html as input and uses regular expressions to find and extract all the URLs present in the HTML. It should return a list of extracted URLs.
#
# 2.	replace_tag(html, tag, replacement): This method takes a string html, a tag name tag, and a replacement string replacement. It uses the re.sub function to replace all occurrences of the specified tag in the HTML with the replacement string. It should return the modified HTML.
#
# 3.	split_elements(html): This method takes a string html as input and uses regular expressions to split the HTML into a list of HTML elements. Each element should be a separate string in the list. It should return the list of HTML elements.
#
# 4.	find_attributes(html, tag): This method takes a string html and a tag name tag as input. It uses regular expressions to find all occurrences of the specified tag in the HTML and prints all the attributes of that tag.

import re


class HTMLAnalyzer:
    def extract_urls(self, html):
        pattern = r'(?<=href=")[^"]+'
        urls = re.findall(pattern, html)
        return urls

    def replace_tag(self, html, tag, replacement):
        pattern = fr'<{tag}[^>]*>(.*?)</{tag}>'
        modified_html = re.sub(pattern, replacement, html)
        return modified_html

    def split_elements(self, html):
        elements = re.findall(r'<[^>]+>', html)
        return elements

    def find_attributes(self, html, tag):
        pattern = fr'<{tag}\s+([^>]+)>'
        matches = re.findall(pattern, html)
        if matches:
            for match in matches:
                attributes = re.findall(r'(\w+)="([^"]*)"', match)
                for attr in attributes:
                    print(f"Attribute: {attr[0]}, Value: {attr[1]}")
        else:
            print(f"No attributes found for tag '{tag}'.")

# Example usage:
html_file = """
<html>
<head>
<title>Sample Page</title>
</head>
<body>
<h1>Welcome</h1>
<p>This is a sample paragraph.</p>
<a href="https://example.com">Visit Example</a>
<img src="image.jpg" alt="Sample Image">
</body>
</html>
"""

analyzer = HTMLAnalyzer()

# Extract URLs
urls = analyzer.extract_urls(html_file)
print("Extracted URLs:", urls)

# Replace tag
modified_html = analyzer.replace_tag(html_file, 'h1', '<h2>Modified Heading</h2>')
print("Modified HTML:\n", modified_html)

# Split elements
elements = analyzer.split_elements(html_file)
print("HTML Elements:", elements)

# Find attributes
analyzer.find_attributes(html_file, 'a')
