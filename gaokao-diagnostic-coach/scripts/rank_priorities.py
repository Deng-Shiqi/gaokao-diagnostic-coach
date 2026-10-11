#!/usr/bin/env python3
"""Rank Gaokao weakness candidates from a JSON file.

Input is a JSON array. Each item needs: name, loss, exam_value,
improvability, transfer, urgency (all 0..5), and confidence (0..1).
The script writes a ranked JSON array to stdout.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


RATING_FIELDS = ("loss", "exam_value", "improvability", "transfer", "urgency")
WEIGHTS = {
    "loss": 0.30,
    "exam_value": 0.25,
    "improvability": 0.20,
    "transfer": 0.15,
    "urgency": 0.10,
}


def bounded_number(item: dict[str, Any], field: str, low: float, high: float) -> float:
    if field not in item:
        raise ValueError(f"missing field: {field}")
    value = float(item[field])
    if not low <= value <= high:
        raise ValueError(f"{field} must be between {low} and {high}: {value}")
    return value


def label(score: float) -> str:
    if score >= 80:
        return "S"
    if score >= 65:
        return "A"
    if score >= 50:
        return "B"
    return "C"


def rank(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output = []
    for item in items:
        if not str(item.get("name", "")).strip():
            raise ValueError("each item needs a non-empty name")
        values = {field: bounded_number(item, field, 0, 5) for field in RATING_FIELDS}
        confidence = bounded_number(item, "confidence", 0, 1)
        base = sum(values[field] * WEIGHTS[field] for field in RATING_FIELDS) / 5 * 100
        score = round(base * (0.7 + 0.3 * confidence), 1)
        output.append({**item, "priority_score": score, "priority_label": label(score)})
    return sorted(output, key=lambda row: (-row["priority_score"], str(row["name"])))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON array of weakness candidates")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("input must be a JSON array")
    print(json.dumps(rank(data), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
