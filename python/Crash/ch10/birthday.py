pifile = 'data/pi_million_digits.txt'

pi = ''
with open(pifile) as infile:
    for line in infile:
        pi += line.strip()

print(pi[:50])

bday = input("Enter you birthday (YYYYMMDD): ")
if bday in pi:
    print("Your birthday occurs in the first one million digits of PI")
else:
    print("Your birthday does NOT occur in the first one million digits of PI")
