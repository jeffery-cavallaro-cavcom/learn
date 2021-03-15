age = int(input("How old are you? "))
message = "You are "
if age < 0:
    message += "not even born yet."
elif age < 2:
    message += "just a baby."
elif age < 4:
    message += "a toddler."
elif age < 13:
    message += "just a kid."
elif age < 20:
    message += "a teenager."
elif age < 65:
    message += "an adult."
else:
    message += "an elderly person."
print(message)
