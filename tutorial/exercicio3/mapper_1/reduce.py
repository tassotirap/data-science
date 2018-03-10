#!/usr/bin/python

import sys

total = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisValue = data

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, total)

        total = 0

    oldKey = thisKey
    total += float(thisValue)

if oldKey != None:
    print "{0}\t{1}".format(oldKey, total)