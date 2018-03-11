#!/usr/bin/python

import sys

totals = 0.0
count = 0.0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisId = data

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, (totals / count))

        totals = 0.0
        count = 0.0

    oldKey = thisKey
    totals += float(thisId)
    count += 1

if oldKey != None:
    print "{0}\t{1}".format(oldKey, (totals / count))