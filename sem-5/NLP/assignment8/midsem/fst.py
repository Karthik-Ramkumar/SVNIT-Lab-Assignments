"""Finite-state transducer for the English noun pluralization question."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Transition:
    state: str
    input_symbol: str
    output_symbol: str
    next_state: str


EXCEPTION_SUFFIXES = ("s", "x", "z", "ch", "sh")


def pluralize(noun: str) -> str:
    """Produce the plural form required by the assignment."""
    suffix = next((s for s in EXCEPTION_SUFFIXES if noun.endswith(s)), None)
    return noun + ("es" if suffix else "s")


def transition_table() -> list[Transition]:
    """Return the compact FST table; q_copy consumes the stem symbols."""
    return [
        Transition("q0", "noun", "noun", "q_copy"),
        Transition("q_copy", "s|x|z|ch|sh", "identity", "q_exception"),
        Transition("q_copy", "other", "identity", "q_regular"),
        Transition("q_regular", "ε", "s", "q_accept"),
        Transition("q_exception", "ε", "es", "q_accept"),
        Transition("q0", "noun", "noun+SG+N", "q_singular_accept"),
    ]


def run_examples() -> list[dict[str, str]]:
    examples = ["cat", "bus", "box", "buzz", "church", "dish"]
    return [{"singular": word, "plural": pluralize(word)} for word in examples]


def solve() -> dict:
    return {
        "topic": "fst_pluralization",
        "states": ["q0", "q_copy", "q_regular", "q_exception", "q_accept", "q_singular_accept"],
        "features": ["+SG", "+PL", "+N"],
        "transition_table": [t.__dict__ for t in transition_table()],
        "examples": run_examples(),
        "explanation": (
            "The transducer copies the noun stem. If the final input is s, x, z, "
            "ch, or sh it emits es; otherwise it emits s. The singular path "
            "outputs the noun with +SG+N."
        ),
    }