# Reproducible event analysis

Assignment 07: a three-stage DVC pipeline and a reactive Marimo report.

## Reproduce

Install uv, clone this repository, and run from the repository root:

```sh
uv sync
uv run dvc repro
uv run marimo edit notebooks/report.py
```

The raw CSV is committed to git. Derived CSVs are ignored by git and managed
by DVC's local cache; no remote is required. A fresh clone regenerates them.

`clean` removes missing fields, non-positive durations, and event types outside
`click`, `view`, `scroll`, `purchase`, and `login`. It parses ISO timestamps
(with or without fractional seconds), space-separated timestamps, and US
month/day/year timestamps, then writes whole-second ISO timestamps and integer
durations. `transform` adds the date. `features` adds minutes and the full
English weekday name without changing row order or count.

The notebook plots a histogram of duration_minutes from the feature output.

Data source: https://github.com/dsc-courses/dsc190-tools-2026-fa/tree/main/assignments/07-reproducibility
