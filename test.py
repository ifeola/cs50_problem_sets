result = ["a", "b", "1", "2", "3", "4"]
for char, index in result:
    if type(char) == str:
        print(index, char)
    else:
        print("Non-string character found")
