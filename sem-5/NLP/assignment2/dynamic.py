import math


def dynamic_segment(text, word_counts):
    n = len(text)

    dp = [-float("inf")] * (n + 1)
    best_word = [None] * (n + 1)

    dp[0] = 0

    total_count = sum(word_counts.values())
    max_length = max(len(word) for word in word_counts)

    for i in range(1, n + 1):

        for length in range(1, min(max_length, i) + 1):

            word = text[i - length:i]

            if word in word_counts:

                probability = word_counts[word] / total_count
                log_probability = math.log(probability)

                score = dp[i - length] + log_probability

                if score > dp[i]:
                    dp[i] = score
                    best_word[i] = word

    result = []
    i = n

    while i > 0:

        word = best_word[i]

        if word is None:
            word = text[i - 1]
            i -= 1
        else:
            result.append(word)
            i -= len(word)

    result.reverse()

    return result