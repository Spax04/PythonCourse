# You are given a log file containing various log entries from a server. Your task is to create a Python class that utilizes regular expressions to perform the following operations:
#
# 1.	Extract all the IP addresses from the log file.
# 2.	Replace all occurrences of a given pattern with a specified replacement string.
# 3.	Split the log file into a list of log entries.
# 4.	Find and print all the log entries that match a specific pattern.
# Your class should have the following methods:
#
# 1.	extract_ip_addresses(log): This method takes a string log as input and uses regular expressions to find and extract all the IP addresses present in the log. It should return a list of extracted IP addresses.
# 2.	replace_pattern(log, pattern, replacement): This method takes a string log, a regular expression pattern, and a replacement string replacement. It uses the re.sub function to replace all occurrences of the pattern in the log with the specified replacement string. It should return the modified log.
# 3.	split_log_entries(log): This method takes a string log as input and uses regular expressions to split the log into a list of log entries. Each log entry should be a separate string in the list. It should return the list of log entries.
# 4.	find_pattern(log, pattern): This method takes a string log and a regular expression pattern as input. It uses regular expressions to find all log entries that match the pattern in the log and prints them.

import re


class LogAnalyzer:
    def extract_ip_addresses(self, log):

    # Your code here

    def replace_pattern(self, log, pattern, replacement):

    # Your code here

    def split_log_entries(self, log):

    # Your code here

    def find_pattern(self, log, pattern):


# Your code here


# Example usage:
log_file = """
2023-06-15 14:23:45 - [INFO] - User with IP 192.168.0.1 logged in.
2023-06-15 14:25:32 - [ERROR] - Connection timed out for IP 10.0.0.2.
2023-06-15 14:27:18 - [WARNING] - Excessive failed login attempts from IP 192.168.0.5.
"""

analyzer = LogAnalyzer()

# Extract IP addresses
ip_addresses = analyzer.extract_ip_addresses(log_file)
print("Extracted IP addresses:", ip_addresses)

# Replace pattern
modified_log = analyzer.replace_pattern(log_file, r'\bIP\b', 'IPAddress')
print("Modified log:\n", modified_log)

# Split log entries
log_entries = analyzer.split_log_entries(log_file)
print("Log Entries:", log_entries)

# Find pattern
analyzer.find_pattern(log_file, r'\[ERROR\].*')
