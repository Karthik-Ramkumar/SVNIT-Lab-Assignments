"""Bigram interpolated Kneser-Ney probabilities for the five sentences."""

from collections import Counter


SENTENCES = [
    ["I", "like", "NLP"], ["I", "like", "AI"], ["You", "like", "NLP"],
    ["You", "love", "AI"], ["We", "love", "NLP"],
]


def solve(discount: float = 0.5) -> dict:
    bigrams = Counter((sentence[index], sentence[index + 1])
                      for sentence in SENTENCES for index in range(len(sentence) - 1))
    followers = Counter(left for left, _ in bigrams)
    continuations = Counter(right for _, right in bigrams)
    total_types = len(bigrams)
    distinct_left = {right: sum(1 for left, candidate in bigrams if candidate == right) for right in continuations}

    def probability(left: str, right: str) -> dict:
        count = bigrams[(left, right)]
        first = max(count - discount, 0) / followers[left]
        lambda_left = discount * len({candidate for candidate in bigrams if candidate[0] == left}) / followers[left]
        continuation = distinct_left.get(right, 0) / total_types
        return {"count": count, "first_term": first, "lambda": lambda_left, "continuation": continuation,
                "probability": first + lambda_left * continuation}

    return {
        "topic": "kneser_ney",
        "discount": discount,
        "bigram_counts": {f"{left}|{right}": count for (left, right), count in bigrams.items()},
        "probabilities": {"P(AI|love)": probability("love", "AI"), "P(NLP|like)": probability("like", "NLP")},
        "explanation": "For bigram Kneser-Ney, P(w|h) = max(c(hw)-d,0)/c(h) + lambda(h)P_continuation(w), with d=0.5.",
    }