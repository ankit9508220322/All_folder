# Regular expressions (regex) are powerful tools for pattern matching in strings. Python's re module provides support for regex.
import re
text = "jai ram ji ki jai ho hanuman ji"
match = re.search("ram",text)
print(match)
if match:
    print("found match")
    print("start index:", match.start())
    print("end index:", match.end())
    
# import re
# text = "ram sita krishna radha mohan ram ram"
# match = re.findall(r"ram",text, re.IGNORECASE)
# print("matches:", match);

# # Replace all occurrences of a pattern
# new_text = re.sub("ram", "ankit", text)
# print("New text:", new_text)
 
# # Compile a regex for efficiency (if used multiple times)
# pattern = re.compile(r"\b\w+\b")  # Matches whole words
# words = pattern.findall(text)
# print("Words:", words)