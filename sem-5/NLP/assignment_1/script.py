import re

# Read the file
with open("hiText.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into sentences
sentences = re.split(r'(?<=[.!?।])\s+', text)

# Remove empty sentences
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

# Save to a file
with open("sentences.txt", "w", encoding="utf-8") as file:
    for sentence in sentences:
        file.write(sentence + "\n")

print("Total sentences:", len(sentences))