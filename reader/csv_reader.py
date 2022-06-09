import csv

# file = open("test.csv", "a",  encoding="utf8")
# data = csv.writer(file)
# data.writerow(["003", "Pinarello", 28, 10000])


with open("test.csv", encoding="utf8") as file:
    data = list(csv.reader(file))

print(data)