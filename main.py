"""One Star, Five Stars for the Food — make.fun entry.

Writes a single one-sentence alien tourist review of Earth
(one star, with a sincere compliment about the food) to entry.txt.
The line (142 characters): Earth made the tourist fill in twelve
forms just to eat lunch, but the hawker's satay smoke was so good
the last form was framed as a souvenir.
Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, one sentence.
Output goes to $MAKEFUN_OUTPUT_DIR (default /output), never to output/ in the repo:
the grader mounts the repo read-only, so a repo-local output/ path fails.
"""

import os

LINE = "One star: Earth made me fill in twelve forms just to eat lunch, but the hawker's satay smoke was so good I framed the last form as a souvenir."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
