from collections import Counter
import re
from pathlib import Path

# Step 1: Open and read the file

file_path = Path("C:/Users/DELL/Desktop/day7FileHandling.txt")
with file_path.open('r', encoding='utf-8') as file:
    text = file.read().lower()  # Convert to lowercase for uniformity

# Step 2: Clean and tokenize the text to handle punctuation
words = re.findall(r'\b\w+\b', text)

# Step 3: Count the word frequencies
word_freq = Counter(words)

for word, freq in word_freq.most_common():
    print(f'{word}: {freq}')

