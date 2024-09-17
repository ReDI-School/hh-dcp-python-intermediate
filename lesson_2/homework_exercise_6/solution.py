import string

text = """
Python is an open source programming language. It was made to be easy-to-read-and-understand and powerful. A Dutch programmer named Guido van Rossum made Python in 1991. He named it after the television program Monty Python's Flying Circus. Many Python examples and tutorials include jokes from the show.
Python is an interpreted language. Interpreted languages do not need to be compiled to run. A program called an interpreter runs Python code on almost any kind of computer. This means that a programmer can change the code and quickly see the results. This also means Python is slower than a compiled language like C, because it is not turned into machine code ahead of time. Instead, this happens as the program is running.
Python has become one of the most famous programming languages on the world as of late. It's utilized in all that from AI to building sites and programming testing. It tends to be utilized by engineers and non-designers the same.
Python drew inspiration from other programming languages like C, C++, Java, Perl, and Lisp.
Python's developers try to avoid changing the language to make it better until they have a lot of things to change. Also, they try not to make small repairs, called patches, to unimportant parts of the CPython reference implementation that would make it faster. When speed is important, a Python programmer can move some of the work of the program to other parts written in programming languages like C or PyPy, a just-in-time compiler. It translates a Python script into C and makes direct C-level API calls into the Python interpreter.
Keeping Python fun to use is an important goal of Python’s developers. It reflects in the language's name, a tribute to the British comedy group Monty Python. On occasions, there are playful approaches to tutorials and reference materials, such as referring to spam and eggs instead of the standard foo and bar.
"""

# Remove punctuation
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

# Split the text into words
words = cleaned_text.split()

# Initialize counters
the_count = 0
python_count = 0
language_count = 0

# Iterate over the words and count occurrences
for word in words:
    if word.lower() == "the":
        the_count += 1
    elif word.lower() == "python":
        python_count += 1
    elif word.lower() == "language":
        language_count += 1

# Print the results using string formatting
print(f"The word 'the' appears {the_count} times.") # The word 'the' appears 16 times.
print(f"The word 'Python' appears {python_count} times.") # The word 'Python' appears 13 times.
print(f"The word 'language' appears {language_count} times.") # The word 'language' appears 4 times.

# Alternative solution using the Counter class from the collections module
from collections import Counter

# Count occurrences of words
word_counts = Counter(words)
print(f"The word 'the' appears {word_counts['the']} times.") # The word 'the' appears 16 times.
print(f"The word 'Python' appears {word_counts['Python']} times.") # The word 'Python' appears 13 times.
print(f"The word 'language' appears {word_counts['language']} times.") # The word 'language' appears 4 times.

# Another alternative solution using the count method
the_count = words.count("the")
python_count = words.count("Python")
language_count = words.count("language")
print(f"The word 'the' appears {the_count} times.") # The word 'the' appears 16 times.
print(f"The word 'Python' appears {python_count} times.") # The word 'Python' appears 13 times.
print(f"The word 'language' appears {language_count} times.") # The word 'language' appears 4 times.

# Yet another alternative solution using a dictionary
word_counts = {"the": 0, "Python": 0, "language": 0}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
print(f"The word 'the' appears {word_counts['the']} times.") # The word 'the' appears 16 times.
print(f"The word 'Python' appears {word_counts['Python']} times.") # The word 'Python' appears 13 times.
print(f"The word 'language' appears {word_counts['language']} times.") # The word 'language' appears 4 times.