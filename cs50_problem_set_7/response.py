from validators import email

def main():
  email = validate(input("What's your email address? "))
  print(email)
  
def validate(email_address):
  if is_valid := email(email_address):
    return "Valid"
  else:
    return "Invalid"
  
if __name__ == "__main__":
  main()