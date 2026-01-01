from datetime import date

today = date.today()
format_string = '%Y-%m-%d'
print(today.strftime(format_string))