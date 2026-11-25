"""The One-Line Cat Joke That Lands — make.fun entry.

Writes a single one-line cat joke (under 200 characters) to
/output/entry.txt, the file the competition's gate scorer reads.
Pure standard library: no third-party packages, no network.
"""

import os

JOKE = "I got a second cat so the first one wouldn't be lonely. Now they ignore me as a team."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
