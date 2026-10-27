"""Two-merge WordPiece/BPE calculation from the midsem corpus."""

from collections import Counter


CORPUS = ["low", "lower", "low", "lower", "lowest", "low", "lowest", "low", "lowest", "low",
          "new", "new", "new", "newer", "newer", "new"]


def word_symbols(word: str) -> tuple[str, ...]:
    return tuple(word) + ("</w>",)


def pair_counts(vocabulary: Counter[tuple[str, ...]]) -> Counter[tuple[str, str]]:
    counts: Counter[tuple[str, str]] = Counter()
    for symbols, frequency in vocabulary.items():
        counts.update({pair: frequency for pair in zip(symbols, symbols[1:])})
    return counts


def merge(vocabulary: Counter[tuple[str, ...]], target: tuple[str, str]) -> Counter[tuple[str, ...]]:
    result: Counter[tuple[str, ...]] = Counter()
    for symbols, frequency in vocabulary.items():
        merged: list[str] = []
        index = 0
        while index < len(symbols):
            if index + 1 < len(symbols) and (symbols[index], symbols[index + 1]) == target:
                merged.append(symbols[index] + symbols[index + 1])
                index += 2
            else:
                merged.append(symbols[index])
                index += 1
        result[tuple(merged)] += frequency
    return result


def tokenize(word: str, merges: list[tuple[str, str]]) -> list[str]:
    symbols = list(word_symbols(word))
    for target in merges:
        merged: list[str] = []
        index = 0
        while index < len(symbols):
            if index + 1 < len(symbols) and (symbols[index], symbols[index + 1]) == target:
                merged.append(symbols[index] + symbols[index + 1])
                index += 2
            else:
                merged.append(symbols[index])
                index += 1
        symbols = merged
    return symbols


def solve() -> dict:
    vocabulary = Counter(word_symbols(word) for word in CORPUS)
    merges: list[tuple[str, str]] = []
    snapshots = []
    for _ in range(2):
        pair, count = pair_counts(vocabulary).most_common(1)[0]
        merges.append(pair)
        vocabulary = merge(vocabulary, pair)
        snapshots.append({"pair": list(pair), "frequency": count})
    return {
        "topic": "wordpiece_two_merges",
        "corpus": CORPUS,
        "merges": snapshots,
        "newest_tokens": tokenize("newest", merges),
        "explanation": "Character symbols include an end-of-word marker; the two most frequent adjacent pairs are merged greedily.",
    }