#!/usr/bin/env python3
"""One-star review of something essential (make.fun).

Writes a single deadpan one-star review, at most 160 characters, of an
everyday essential to /output/entry.txt.

The essential is rain: the sharpest true grievance is that rain is never
punctual when it is wanted (a drought) and always punctual when it hurts
(the laundry on the line). The turn lands in the last few words.
"""

import os

REVIEW = "Rain: one star. Never on time for the drought, always on time for the laundry."

def main():
    text = REVIEW.strip()
    assert 1 <= len(text) <= 160, "review is %d characters" % len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
