#!/usr/bin/python

import sys

ids = []
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisId = data

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, ','.join(sorted(ids, key=int)))

        ids = []

    oldKey = thisKey
    ids.append(thisId)

if oldKey != None:
    print "{0}\t{1}".format(oldKey, ','.join(sorted(ids, key=int)))