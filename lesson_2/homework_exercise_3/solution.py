import string

sentence = "As he crossed toward the pharmacy at the corner, he involuntarily turned his head, because of a burst of light, that had ricocheted from his temple, and saw, with that quick smile - with which we greet a rainbow or a rose - a blindingly white parallelogram of sky being unloaded from the dresser with mirrors across..."

# Remove punctuation
cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

# Split the sentence into words
words = cleaned_sentence.split()

# Iterate over the words and print those with an even number of letters
for word in words:
    if len(word) % 2 == 0:
        print(word)

# Alternative solution using list comprehension
print("\nSolution using list comprehension:\n")
print("\n".join([word for word in words if len(word) % 2 == 0]))

# Alternative solution using filter and lambda and map for everything
print("\nSolution using filter and lambda:\n")
print("\n".join(filter(lambda word: len(word) % 2 == 0 and len(word) > 0, "".join(
    filter(lambda character: character.isalnum() or character.isspace(),
           sentence.translate(str.maketrans('', '', string.punctuation)))).split(" "))))
