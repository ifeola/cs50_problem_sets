import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

# 255
# [0-2][0-2]?[0-5]?\.[0-2]?[0-2]?[0-5]?\.[0-2]?[0-2]?[0-5]?\.[0-2]?[0-2]?[0-5]?
def validate(ip):
  pattern = r"(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])"
  match = re.fullmatch(rf"{pattern}\.{pattern}\.{pattern}\.{pattern}", ip)
  if match:
    return True
  else:
    return False


if __name__ == "__main__":
    main()