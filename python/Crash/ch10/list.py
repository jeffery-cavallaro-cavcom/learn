filename = 'data/pi.txt'

with open(filename) as infile:
    lines = infile.readlines()

for line in lines:
    print(line.rstrip())
