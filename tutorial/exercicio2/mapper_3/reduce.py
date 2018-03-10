#!/usr/bin/python

import sys

totalValues = 0
oldKey = None

mostPopularValue = 0
mostPopularKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisValue = data

    if oldKey and oldKey != thisKey:
        if totalValues > mostPopularValue:
            mostPopularValue = totalValues
            mostPopularKey = oldKey

        totalValues = 0

    oldKey = thisKey
    totalValues += int(thisValue)

print "{0}\t{1}".format(mostPopularKey, mostPopularValue)