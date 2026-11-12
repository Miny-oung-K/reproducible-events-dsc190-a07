"""Add a calendar date to each cleaned event."""
import csv
from pathlib import Path


def main():
    target = Path("data/transformed/events.csv")
    target.parent.mkdir(parents=True, exist_ok=True)
    with open("data/clean/events.csv", newline="") as source, target.open("w", newline="") as output:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(output, fieldnames=[*reader.fieldnames, "date"])
        writer.writeheader()
        for row in reader:
            row["date"] = row["timestamp"].split("T")[0]
            writer.writerow(row)


if __name__ == "__main__":
    main()
