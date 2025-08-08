from collections import Counter
import string
import os

# paragraph input
paragraph = """
Python is powerful. Python is easy to learn. Python is open source.
Many developers love Python for data analysis, machine learning, and web development.
"""

# list of stop words to ignore
stopwords = {
    'is', 'to', 'for', 'and', 'the', 'a', 'of', 'in', 'on', 'with', 'as', 'an', 'this', 'that', 'it', 'at'
}

# clean and tokenize the paragraph
words = [
    word.strip(string.punctuation)
    for word in paragraph.lower().split()
    if word.strip(string.punctuation) not in stopwords
]

# count word frequencies
word_count = Counter(words)

# sort by frequency
sorted_word_count = word_count.most_common()

print("word frequency count:\n")
for word, count in sorted_word_count:
    print(f"{word}: {count}")

output_path = "/Users/sadhikavarakala/Practice/word_frequencies.txt"

with open(output_path, 'w') as f:
    f.write("word frequency count:\n\n")
    for word, count in sorted_word_count:
        f.write(f"{word}: {count}\n")

print(f"\nWord frequency count saved to {output_path}")