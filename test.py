import inflect

names = ["ram", "shee", "reap"]

p = inflect.engine()
print(p.join(names))
