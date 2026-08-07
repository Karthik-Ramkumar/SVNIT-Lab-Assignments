import re

# Sentence tokenizer
def sentence_tokenize(text):
    pattern = r'(?<=[.!?।])["\'”’]*\s+'
    sentences = re.split(pattern, text)

    new_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            new_sentences.append(sentence)

    return new_sentences


input_file = "hiText.txt"
output_file = "sentence_tokenized.txt"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:

        line = line.strip()

        if not line:
            continue

        sentences = sentence_tokenize(line)

        for sentence in sentences:
            outfile.write(sentence + "\n")

print("Sentence tokenization completed.")