import re

# ---------------- Sentence Tokenizer ----------------
def sentence_tokenize(text):
    pattern = r'(?<=[.!?।])\s+'
    sentences = re.split(pattern, text)
    return [s.strip() for s in sentences if s.strip()]


# ---------------- Word Tokenizer ----------------
TOKEN_PATTERN = re.compile(r'''
https?://[^\s]+|                                  # URLs
www\.[^\s]+|                                      # URLs starting with www
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|   # Email IDs
\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|                    # Dates
\d+\.\d+|                                         # Decimal numbers
\d+|                                              # Integers
[\u0900-\u097F]+|                                 # Hindi words
[A-Za-z]+|                                        # English words
[^\w\s]                                           # Punctuation
''', re.VERBOSE)


def word_tokenize(sentence):
    return TOKEN_PATTERN.findall(sentence)


# ---------------- Main ----------------

input_file = "hindi.txt"          # Change this
output_file = "tokenized.txt"

total_sentences = 0

with open(hiText.txt, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:

    for paragraph in fin:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        sentences = sentence_tokenize(paragraph)

        for sentence in sentences:

            total_sentences += 1

            tokens = word_tokenize(sentence)

            fout.write(sentence + "\n")
            fout.write(" ".join(tokens))
            fout.write("\n\n")

print("Finished!")
print("Total Sentences:", total_sentences)