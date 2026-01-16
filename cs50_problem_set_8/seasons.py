from datetime import date, timedelta
import re, sys, inflect

class Date:
	def __init__(self, datee):
		self.datee = datee
    
	@property
	def datee(self):
		return self._datee
  
	@datee.setter  
	def datee(self, datee):
		match = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", datee)
		if not match:
			sys.exit("Invalid date of birth.")
		self._datee = datee

	def subtract(self, other):
		today = date.fromisoformat(self.datee) - date.fromisoformat(other.datee)
		today = today.days
		return today
  
	def __str__(self):
		return f"{self.datee}"


def main():
  date_of_birth = input("Date of Birth: ")
  result = convert(date_of_birth)
  print(result)

def convert(dob):
	today_date = date.today()
	format_string = "%Y-%m-%d"
	formatted_date = today_date.strftime(format_string)
  
	date_of_birth = Date(dob)
	t_date = Date(formatted_date)
  
	difference = t_date.subtract(date_of_birth)
	minutes = convert_date_to_seconds(difference)
	p = inflect.engine()
	words = p.number_to_words(minutes, andword="")
	return f"{words.capitalize()} minutes"


def convert_date_to_seconds(days):
  minutes = days * 24 * 60
  return minutes



if __name__ == "__main__":
    main()