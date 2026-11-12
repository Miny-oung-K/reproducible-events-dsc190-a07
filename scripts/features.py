"""Add event duration in minutes and the English weekday name."""
import csv
from datetime import date
from pathlib import Path

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def main():
    target = Path("data/features/events.csv")
    target.parent.mkdir(parents=True, exist_ok=True)
    with open("data/transformed/events.csv", newline="") as source, target.open("w", newline="") as output:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(output, fieldnames=[*reader.fieldnames, "duration_minutes", "weekday"])
        writer.writeheader()
        for row in reader:
            row["duration_minutes"] = int(row["duration_seconds"]) / 60
            row["weekday"] = WEEKDAYS[date.fromisoformat(row["date"]).weekday()]
            writer.writerow(row)


if __name__ == "__main__":
    main()
