text = """Data science is the study of the extraction of knowledge from data. It uses various techniques from many fields, including signal processing, mathematics, probability, machine learning, computer programming, statistics, data engineering, pattern matching, and data visualization, with the goal of extracting useful knowledge from the data. With computer systems able to handle more data, big data is an important aspect of data science.
A person that does data science is called a data scientist. Data scientists solve complicated data problems using mathematics, statistics and computer science, although very good skill in these subjects are not required. However, a data scientist is most likely to be an expert in only one or two of these disciplines, meaning that cross disciplinary teams can be a key component of data science.
Good data scientists are able to apply their skills to achieve many kinds of purposes. Their skills and competencies vary widely."""

# Split the text into words
words = text.split()

# Count words starting with 'a' or 'A'
count = 0
for word in words:
    if word[0].lower() == 'a':
        count += 1

# Print the result
print(f"The number of words starting with 'a' or 'A' is {count}.")

# Alternative solution using list comprehension
print(f"The number of words starting with 'a' or 'A' is {len([word for word in words if word[0].lower() == 'a'])}.")