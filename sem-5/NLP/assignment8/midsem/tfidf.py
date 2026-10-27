"""Raw-count TF-IDF and cosine comparison for the three toy sentences."""

from collections import Counter
from math import log, sqrt


SENTENCES = [["cat", "dog", "animal"], ["cat", "cat", "pet"], ["dog", "pet", "animal", "cat"]]


def solve() -> dict:
    vocabulary = sorted({word for sentence in SENTENCES for word in sentence})
    document_frequency = {word: sum(word in sentence for sentence in SENTENCES) for word in vocabulary}
    idf = {word: log(len(SENTENCES) / document_frequency[word]) for word in vocabulary}
    vectors = []
    for sentence in SENTENCES:
        counts = Counter(sentence)
        vectors.append({word: counts[word] * idf[word] for word in vocabulary})

    def cosine(left: dict[str, float], right: dict[str, float]) -> float:
        numerator = sum(left[word] * right[word] for word in vocabulary)
        denominator = sqrt(sum(value * value for value in left.values()) * sum(value * value for value in right.values()))
        return numerator / denominator if denominator else 0.0

    similarities = []
    for left in range(len(SENTENCES)):
        for right in range(left + 1, len(SENTENCES)):
            similarities.append({"sentences": [left + 1, right + 1], "cosine": cosine(vectors[left], vectors[right])})
    closest = max(similarities, key=lambda item: item["cosine"])
    return {
        "topic": "tfidf",
        "sentences": SENTENCES,
        "vocabulary": vocabulary,
        "idf": idf,
        "tfidf_vectors": vectors,
        "cosine_similarities": similarities,
        "closest_pair": closest["sentences"],
        "explanation": "TF uses raw term counts and IDF is unsmoothed log(N/df). Sentence similarity is cosine similarity.",
    }