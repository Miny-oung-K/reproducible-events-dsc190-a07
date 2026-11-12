"""Remove invalid events and normalize timestamps without changing row order."""
import csv
from datetime import datetime
from pathlib import Path

VALID_EVENTS = {"click", "view", "scroll", "purchase", "login"}
FORMATS = ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y %H:%M:%S")


def normalize_timestamp(value):
    for fmt in FORMATS:
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%dT%H:%M:%S")
        except ValueError:
            continue
    raise ValueError(f"Unsupported timestamp: {value!r}")


def main():
    target = Path("data/clean/events.csv")
    target.parent.mkdir(parents=True, exist_ok=True)
    with open("data/raw/events.csv", newline="") as source, target.open("w", newline="") as output:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if any(value is None or not value.strip() for value in row.values()):
                continue
            if row["event_type"] not in VALID_EVENTS:
                continue
            duration = int(row["duration_seconds"])
            if duration <= 0:
                continue
            row["duration_seconds"] = duration
            row["timestamp"] = normalize_timestamp(row["timestamp"])
            writer.writerow(row)


if __name__ == "__main__":
    main()
