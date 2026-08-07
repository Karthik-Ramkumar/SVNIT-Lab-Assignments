input_file = "word_tokenized.txt"
output_file = "stats.txt"

total_sentences = 0
total_words = 0
total_characters = 0

unique_tokens = set()

current_sentence_words = 0

with open(input_file, "r", encoding="utf-8") as infile:

    for line in infile:

        token = line.strip()

        # Blank line means end of a sentence
        if token == "":
            if current_sentence_words > 0:
                total_sentences += 1
                current_sentence_words = 0
            continue

        total_words += 1
        current_sentence_words += 1

        total_characters += len(token)

        unique_tokens.add(token)

if current_sentence_words > 0:
    total_sentences += 1

average_sentence_length = total_words / total_sentences
average_word_length = total_characters / total_words
ttr = len(unique_tokens) / total_words

with open(output_file, "w", encoding="utf-8") as outfile:

    outfile.write(f"Total Sentences        : {total_sentences}\n")
    outfile.write(f"Total Words            : {total_words}\n")
    outfile.write(f"Total Characters       : {total_characters}\n")
    outfile.write(f"Average Sentence Length: {average_sentence_length:.2f}\n")
    outfile.write(f"Average Word Length    : {average_word_length:.2f}\n")
    outfile.write(f"Type/Token Ratio (TTR) : {ttr:.4f}\n")

print("Statistics saved to stats.txt")