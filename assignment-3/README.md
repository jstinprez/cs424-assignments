# Assignment 3: Interaction and evaluation

Beggars Pizza customer survey (40 responses). This assignment compares a static and an interactive version of the same visualization in a small user study. The full writeup is in `report.md`.

## Run it

Install the packages:

    python3 -m pip install pandas altair vl-convert-python

Run each script from the `assignment-3` folder:

    python3 code/01_clean.py        # original data -> processed data
    python3 code/02_build_views.py  # makes static.html and interactive.html
    python3 code/03_analysis.py     # study results -> summary table and charts

Then open `static.html` and `interactive.html` in a browser.

## What's in here

- `data/original/`: the survey export, unchanged
- `data/processed/`: the cleaned data used by both versions
- `code/`: scripts for cleaning, building the two versions, and analysis
- `static.html`: the static version
- `interactive.html`: the interactive version
- `study/protocol.md`: instructions, tasks, expected answers, order, scoring
- `study/results.csv`: anonymous task measurements (the two PILOT rows are not counted)
- `study/summary.csv`: accuracy and time per condition, made by `03_analysis.py`
- `figures/`: charts and screenshots used in the report
- `report.md`: the writeup, organized by Tasks 1 to 5

## Where each task lives

| Task | Where |
|---|---|
| 1. Implementing interaction | `static.html`, `interactive.html`, `code/02_build_views.py` |
| 2. Evaluation design | `study/protocol.md` |
| 3. Conducting the evaluation | `study/results.csv`, `report.md` |
| 4. Quantitative analysis | `code/03_analysis.py`, `study/summary.csv`, `figures/accuracy.png`, `figures/time.png`, `report.md` |
| 5. Reflection and recommendations | `report.md` |
