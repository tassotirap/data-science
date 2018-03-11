import sys


def reducer():
    totalEntry = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisEntry = data

        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, totalEntry)

            totalEntry = 0

        oldKey = thisKey
        totalEntry += float(thisEntry)

    if oldKey != None:
        print "{0}\t{1}".format(oldKey, totalEntry)

reducer()