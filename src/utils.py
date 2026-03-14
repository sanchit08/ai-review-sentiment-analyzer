import json
import csv

def save_json(data, path):

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def save_csv(data, path):

    if len(data) == 0:
        return

    keys = data[0].keys()

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()

        for row in data:
            writer.writerow(row)