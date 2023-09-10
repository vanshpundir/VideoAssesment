# Define the text
text = "This is a sample text containing some words. We want to find specific words in this text."

# Define the target words you want to find
target_words = ["sample", "specific", "text"]

# Split the text into words
words = text.split()

# Initialize a list to store the found words
found_words = []

# Iterate through the words and check if they match the target words
for word in words:
    if word.lower() in [target.lower() for target in target_words]:
        found_words.append(word)

# Print the found words
if found_words:
    print("Found words:", found_words)
else:
    print("No target words found in the text.")
