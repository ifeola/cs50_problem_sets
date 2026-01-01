import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(0?\d|1[0-2])(?:\:|\s)?(0\d|[1-4]\d|5[0-9])?\s(AM|PM)"
    match = re.search(rf"^{pattern} to {pattern}$", s)
    if not match:
      raise ValueError("out-of-range times")
    first = "0" + str(match.group(1)) if int(match.group(1)) < 10 else match.group(1)
    seconds_one = "00" if match.group(2) == None else match.group(2)
    meridiem_one = match.group(3)
    second = "0" + str(match.group(4)) if int(match.group(4)) < 10 else match.group(4)
    seconds_two = "00" if match.group(5) == None else match.group(5)
    meridiem_two = match.group(6)
    if meridiem_one == "PM" and meridiem_two == "PM":
      first = "00" if int(first) + 12 == 24 else int(first) + 12
      second = "00" if int(second) + 12 == 24 else int(second) + 12
      return f"{first}:{seconds_one:02} to {second}:{seconds_two:02}"
    elif meridiem_two == "AM" and int(second) == 12:
      second = "00"
      return f"{first}:{seconds_one:02} to {second}:{seconds_two:02}"    
    elif meridiem_one == "AM" and int(first) == 12:
      first = "00"
      return f"{first}:{seconds_one:02} to {second}:{seconds_two:02}"
    elif meridiem_one == "PM" and int(first) != 12:
      first = "00" if int(first) + 12 == 24 else int(first) + 12
      return f"{first}:{seconds_one:02} to {second}:{seconds_two:02}"
    elif meridiem_two == "PM" and int(second) != 12:
      second = "00" if int(second) + 12 == 24 else int(second) + 12
      return f"{first}:{seconds_one:02} to {second}:{seconds_two:02}"
    else:
      return f"{first}:{seconds_one:02} to {second}:{seconds_two:02}"

    
if __name__ == "__main__":
    main()