import string

text = """ChatGPT (short for Chat Generative Pre-trained Transformer) is a chatbot. It was launched by OpenAI in November 2022. The program is built on top of OpenAI's GPT-3.5 family of large language models. It is fine-tuned with both supervised and reinforcement learning techniques.
ChatGPT was launched as a prototype on November 30, 2022. The website had more than one billion users after five days. By January 2023, ChatGPT reached over 100 million users. It got attention for its responses and answers in many areas of knowledge. Its uneven accuracy was said to be a major drawback.
As of December 2022, the chatbot was a 'Research Preview' according to its website. While the chatbot is free to use, there have been announcements and rumours over a paid version called ChatGPT Professional. The website also warns users that the bot may give wrong information or have biased content."""

# 1. Print the length of the text
length_of_text = len(text)
print(f"The length of the text is {length_of_text}.")

# 2. Count occurrences of 'a', 't', and 'r' using the count method
count_a = text.count('a')
count_t = text.count('t')
count_r = text.count('r')
print(f"The letter 'a' appears {count_a} times.")
print(f"The letter 't' appears {count_t} times.")
print(f"The letter 'r' appears {count_r} times.")

# Alternative solution using a dictionary
letter_counts = {letter: text.count(letter) for letter in ['a', 't', 'r']}
print(f"The letter 'a' appears {letter_counts['a']} times.")
print(f"The letter 't' appears {letter_counts ['t']} times.")
print(f"The letter 'r' appears {letter_counts['r']} times.")

# 3. Transform text to uppercase and count 'C'
uppercase_text = text.upper()
count_C = uppercase_text.count('C')
print(f"The letter 'C' appears {count_C} times.")

# Alternative solution using a one liner
print(f"The letter 'C' appears {text.upper().count('C')} times.")

# 4. Remove all punctuation marks
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
print("Text without punctuation:")
print(cleaned_text)