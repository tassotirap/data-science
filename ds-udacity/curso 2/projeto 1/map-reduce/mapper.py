import sys

def mapper():
    for line in sys.stdin:
        # your code here

        if line.startswith(','): #skip header
            continue

        data = line.split(',')
        print "{0}\t{1}".format(data[1], data[6])

mapper()