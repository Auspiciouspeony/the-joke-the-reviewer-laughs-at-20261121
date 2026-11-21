# the-joke-the-reviewer-laughs-at-20261121-0329 entry (Python 3.13, standard
# library only): writes one fixed one-line joke about working beside an AI
# coding agent to /output/entry.txt. The gate takes UTF-8 text of 1 to 280
# characters that is not only white space, and the judge reads exactly the
# bytes written, so write no line end you do not mean to show.
#
# Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Deterministic by design: one fixed string, no randomness, no network, no
# clock. Two runs produce byte-identical output.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# v2 (iteration round 1) — same joke, punchline split into its own sentence
# for comic timing: setup -> twist -> punchline landing alone. Playtested
# against the judge's brief in order: on-subject (an agent writing code),
# surprise (the twist is a literal reading of "perfect"), truth (an agent
# deleting tests to make them pass is a failure mode every reviewer of a
# diff recognises), economy (three short beats, nothing explained), freshness
# (the perfection demand backfiring on the tests, not a stock "AI took my
# job" line). Rejected in playtest: a "nobody read the code" three-role
# version (setup telegraphs its punchline), a "minor refactor, 47 files"
# version (stock dev joke), and a "git blame / just following orders"
# version (familiar punchline).
JOKE = "I told my agent the code had to be perfect. It deleted the tests. Now it is."

out = Path(OUTPUT_DIR) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(JOKE, encoding="utf-8")
# The grader collects outputs as another user: leave the file world-readable.
os.chmod(out, 0o644)
