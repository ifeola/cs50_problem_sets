from datetime import date, timedelta
import re, sys

class Date:
  def __init__(self, datee):
    self.datee = datee
    
  @property
  def datee(self):
    return self._datee
  
  @datee.setter  
  def datee(self, datee):
    format_string = '%Y-%m-%d'
    formatted_date = datee.strftime(format_string)
    match = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", formatted_date)
    if not match:
      sys.exit("Invalid date of birth.")
    self._datee = datee

  def __sub__(self, other):
    today = self.datee - other.datee
    today = today.days
    return Date(today)
  
  def __str__(self):
    return f"{self.datee}"


def main():
  dob = Date(date.fromisoformat("1995-01-23"))
  today_date = Date(date.today())
  date_of_birth = today_date - dob
  # minutes = convert_date_to_seconds(dob)
  print(date_of_birth)


def convert_date_to_seconds(days):
  minutes = int(days) * 24 * 60
  return minutes



if __name__ == "__main__":
    main()