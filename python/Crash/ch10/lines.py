filename = 'data/pi.txt'

with open(filename) as infile:
    for line in infile:
        print(line.rstrip())
