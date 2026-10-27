"""Run only the five midsem question solutions."""

import json
from pathlib import Path

from .fst import solve as solve_fst
from .kneser_knee import solve as solve_kneser_ney
from .naive_bias import solve as solve_naive_bayes
from .tfidf import solve as solve_tfidf
from .wordpiece import solve as solve_wordpiece


def run(output_path: Path | None = None) -> Path:
    output_path = output_path or Path(__file__).parent / "midsem_outputs.json"
    solutions = [
        solve_fst(),
        solve_wordpiece(),
        solve_tfidf(),
        solve_naive_bayes(),
        solve_kneser_ney(),
    ]
    output_path.write_text(
        json.dumps({"assignment": "NLP Midsem", "solutions": solutions}, indent=2),
        encoding="utf-8",
    )
    for solution in solutions:
        print(f"[done] {solution['topic']}")
    print(f"Results written to {output_path}")
    return output_path


if __name__ == "__main__":
    run()