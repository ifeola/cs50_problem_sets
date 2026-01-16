from datetime import date

today = date.today() - date.fromisoformat("1995-01-23")
today = today.days
print(type(today))