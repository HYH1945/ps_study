# Copilot Instructions — Competitive Programming Solutions Repo

This workspace is a collection of single-file problem solutions (mostly Python, some Java) for online judge problems. Aim to produce small, correct, and idiomatic changes that respect the repository's conventions.

- Repo shape: many files named like `1234_problemname.py` or `bj_2206.java`. Solutions are standalone scripts that read from stdin and print to stdout. See `README.md` for overall context.
- Execution: run a solution with `python 2150_SCC.py < input.txt` (no build system or virtualenv required). For Java files use `javac`/`java` as usual.

- Typical patterns:
  - Use `sys.stdin.readline` for input speed and `sys.setrecursionlimit(10000)` in recursive problems (e.g. `2150_SCC.py`).
  - Graphs implemented as adjacency lists (`adj_list = [[] for _ in range(v+1)]`).
  - Solutions are written for online judges: avoid interactive prompts, keep input/output exact.

- When editing or generating code:
  - Keep changes minimal and focused to one problem file per PR/commit.
  - Preserve file naming pattern (problem number + short title). Don't rename files unless necessary.
  - Do not add external dependencies; prefer the stdlib.

- Where to look for examples:
  - Strong examples of graph and DFS patterns: `2150_SCC.py`, `1753_최단경로.py`, `1916_최소비용구하기.py`.
  - DP examples: `1932_정수삼각형.py`, `9465_스티커.py`.

- Editing guidance for AI agents:
  - Read the target file fully before proposing changes — many solutions rely on subtle input-format assumptions.
  - If adding helper functions across files, prefer local helpers inside the same script.
  - When increasing recursion limits or changing input buffering, match the project's existing conventions.

- Testing & verification:
  - There are no automated tests. Validate by running the modified script with representative inputs: `python <file>.py < sample_input.txt`.
  - Keep sample inputs small and deterministic.

- Commit & PR guidance:
  - One logical change per commit (one problem file fix or new solution per PR).
  - In PR descriptions, reference the BOJ problem number and a short explanation of the change.

If any repository-specific rules are missing or you'd like stricter formatting/typing rules, tell me which files to reference and I'll update this guidance.
