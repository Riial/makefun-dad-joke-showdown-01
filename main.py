#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is a classic
question-and-answer dad joke: the Queen visits the dentist because she
needs a new crown -- a crown is both the headpiece a monarch wears and
the cap a dentist fits on a tooth. Clean wordplay, lands on first read,
punchline at the end, 60 characters.
"""

import os

JOKE = "Why did the Queen go to the dentist? She needed a new crown."

# Gate guard: the sealed scorer only accepts UTF-8 text of 1-200
# characters that is not only whitespace. Fail loudly here instead of
# ever writing an invalid entry.
assert 1 <= len(JOKE) <= 200, f"joke length {len(JOKE)} out of range"
assert JOKE.strip(), "joke must not be only whitespace"
assert JOKE.encode("utf-8"), "joke must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
