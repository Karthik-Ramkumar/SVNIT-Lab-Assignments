def greedy_segment(text, vocabulary):
    result = []
    i = 0

    max_length = max(len(word) for word in vocabulary)

    while i < len(text):
        best_word = None

        for length in range(max_length, 0, -1):
            candidate = text[i:i + length]

            if candidate in vocabulary:
                best_word = candidate
                break

        if best_word is None:
            best_word = text[i]

        result.append(best_word)
        i += len(best_word)

    return result

