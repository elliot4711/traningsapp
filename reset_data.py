import csv

returns_path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/traningsapp_data.csv"
file = open(returns_path, "w")
writer = csv.writer(file)
writer.writerow(["sets", "benchpress", "squats", "deadlift", "military press"])
writer.writerow(["4x8", 50, 70, 110, 30])