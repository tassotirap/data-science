#!/usr/bin/python

import sys

totalAccess = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisAccess = data

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, totalAccess)

        totalAccess = 0

    oldKey = thisKey
    totalAccess += int(thisAccess)

if oldKey != None:
    print "{0}\t{1}".format(oldKey, totalAccess)