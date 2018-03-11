#!/usr/bin/python

import sys

totalOfSales = 0.0
numOfSales = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisSale = data

    totalOfSales += float(thisKey)
    numOfSales += float(thisSale)

print "{0}\t{1}".format(totalOfSales, numOfSales)