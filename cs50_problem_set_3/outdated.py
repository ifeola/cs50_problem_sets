months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    date = split_date("Date: ")
    result = outdated(date)
    print(result)


def split_date(prompt):
    while True:
        try:
            date = input(prompt)
            if "/" in date:
                split_date = date.strip().split("/")
                if int(split_date[0]) <= 12 and int(split_date[1]) <= 31:
                    return split_date
                else:
                    continue
            elif "," in date:
                split_date = date.replace(",", "").split()
                if split_date[0] in months and int(split_date[1]) <= 31:
                    index = months.index(split_date[0]) + 1
                    split_date[0] = str(index)
                    return split_date
                else:
                    continue
            else:
                continue
        except ValueError:
            pass


def outdated(date):
    return f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}"


main()
