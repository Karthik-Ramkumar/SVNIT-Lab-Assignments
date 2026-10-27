"""Bernoulli Naive Bayes calculation for the seven labelled emails."""

from fractions import Fraction


ROWS = [
    ((1, 1, 1), "Spam"), ((1, 1, 0), "Spam"), ((1, 0, 1), "Spam"), ((0, 1, 1), "Spam"),
    ((0, 0, 1), "NotSpam"), ((0, 1, 0), "NotSpam"), ((1, 0, 0), "NotSpam"),
]


def solve() -> dict:
    classes = ("Spam", "NotSpam")
    query = (0, 0, 0)
    computations = {}
    for label in classes:
        rows = [features for features, item in ROWS if item == label]
        prior = Fraction(len(rows), len(ROWS))
        likelihoods = [Fraction(sum(row[index] == query[index] for row in rows), len(rows)) for index in range(3)]
        score = prior
        for likelihood in likelihoods:
            score *= likelihood
        computations[label] = {
            "prior": float(prior),
            "feature_likelihoods": [float(value) for value in likelihoods],
            "unnormalized_score": float(score),
            "formula": f"P({label}) * " + " * ".join(f"{float(value):.6f}" for value in likelihoods),
        }
    prediction = max(computations, key=lambda label: computations[label]["unnormalized_score"])
    return {
        "topic": "naive_bayes",
        "features": ["free", "win", "offer"],
        "query": query,
        "computations": computations,
        "prediction": prediction,
        "explanation": "Bernoulli Naive Bayes multiplies the class prior by the three binary feature likelihoods. No smoothing is needed because all query feature values occur in each class.",
    }