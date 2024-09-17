words = "atnegam,neerg,egnaro,yerg,etihw,kcalb,wolley,eulb,der"

# Split the string into a list of reversed words
reversed_words = words.split(',')

# Reverse each word in the list
result = []
for word in reversed_words:
    result.append(word[::-1])

# Use list-comprehension to achieve the same result
# result = [word[::-1] for word in reversed_words]


# Join the reversed words back into a single string
result = ','.join(result)

# Print the resulting string
print(result)  # Output: magenta,green,orange,grey,white,black,yellow,blue,red