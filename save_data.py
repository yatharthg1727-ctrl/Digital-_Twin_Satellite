import csv


def save_data(data):
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data["battery"],
            data["temperature"],
            data["fuel"],
            data["signal"],
        ])


save = save_data