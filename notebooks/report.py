import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import csv
    from pathlib import Path
    import matplotlib.pyplot as plt
    import marimo as mo
    return Path, csv, mo, plt


@app.cell
def _(mo):
    mo.md("# Event durations\nDistribution of event durations after cleaning and feature engineering.")
    return


@app.cell
def _(Path, csv):
    # Resolve relative to the notebook so launching from another folder also works.
    features_path = Path(__file__).resolve().parents[1] / "data/features/events.csv"
    with features_path.open(newline="") as source:
        durations = [float(row["duration_minutes"]) for row in csv.DictReader(source)]
    return (durations,)


@app.cell
def _(durations, plt):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(durations, bins=30, edgecolor="white")
    ax.set(title="Distribution of event durations", xlabel="Duration (minutes)", ylabel="Number of events")
    fig.tight_layout()
    fig
    return


if __name__ == "__main__":
    app.run()
