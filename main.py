#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only words and images they could grasp:
roads, houses, letters, ink, books, libraries.
"""

SENTENCE = (
    "Imagine a road joining every house on earth, carrying letters "
    "that arrive before the ink dries and lending the books of every "
    "library to anyone who asks."
)


def main() -> None:
    import os

    # The gate allows 1 to 200 characters of UTF-8 text, one sentence.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), (
        "sentence must be a single sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
