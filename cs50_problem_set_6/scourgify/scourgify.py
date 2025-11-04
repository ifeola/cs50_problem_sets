import csv
import sys


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if not ".csv" in sys.argv[1] and not ".csv" in sys.argv[2]:
        sys.exit("Not a CSV file")
    try:
        before = reader(sys.argv[1])
        writer(sys.argv[2], before)
    except FileNotFoundError:
        sys.exit("Could not read 1.csv")


def reader(before):
    people = []
    with open(before) as file:
        dict_reader = csv.DictReader(file)
        for row in dict_reader:
            name, house = row["name"], row["house"]
            first, last = name.split(",")
            person = {"first": first, "last": last.strip(), "house": house}
            people.append(person)
    return people


def writer(writer_file, after):
    with open(writer_file, "a") as file:
        dict_writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        dict_writer.writeheader()
        for row in after:
            dict_writer.writerow(row)


if __name__ == "__main__":
    main()
