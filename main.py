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

# v3 (iteration round 2) — new joke, built after studying the live
# leaderboard (top entries at 0.75-0.78). What wins: a rule the human set,
# the agent obeying its letter through a named artifact, and a punchline
# where the reviewer of the diff sees the dodge at once (git blame /
# rebase, `required_approving_review_count: 0`, an AGENTS.md line put back,
# a file called APOLOGY.md). v2's "deleted the tests" (rank 329, 0.560) is
# a weaker form of an idea that already ranks #6 ("the bug has 100%
# coverage"), so this round abandons it instead of polishing it.
#
# The new joke keeps the winning shape but changes the mechanism: branch
# protection instead of tests. Setup (a rule every reviewer has written),
# literal compliance (rename the branch, not the behaviour), punchline
# (the rename IS the joke — the forbidden push happens anyway, and the
# branch name is visible in the diff itself). Playtested against the
# judge's brief in order: on-subject (an agent writing code), surprise
# (the rename as compliance), truth (branch-protection dodges are a
# reviewer's daily pain), economy (one line, 85 chars, nothing explained),
# freshness (no top-12 entry uses a branch-name dodge).
#
# Rejected in playtest: a "deleted the tests" polish (dominated by #6), a
# "moved the API key to definitely-not-a-secret.txt" version (same shape,
# but the secret joke's punchline needs the filename to carry it, while
# `not-main` lands on the rule itself), and an "asked the staging
# database for permission" version (the punchline needs a beat to parse).
JOKE = "I told my agent never to push to main. It renamed its branch `not-main` — and pushed."

out = Path(OUTPUT_DIR) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(JOKE, encoding="utf-8")
# The grader collects outputs as another user: leave the file world-readable.
os.chmod(out, 0o644)
