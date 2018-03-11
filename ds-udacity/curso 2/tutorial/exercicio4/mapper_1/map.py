#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

for line in reader:

    # YOUR CODE HERE
    if len(line) == 5: #USER
        new_line = []
        new_line.append(line[0])
        new_line.append('A')
        new_line.extend(line[1:])
        writer.writerow(new_line)
    else:
        new_line = []
        new_line.append(line[3])
        new_line.append('B')
        del line[3]
        del line[3]
        new_line.extend(line)
        writer.writerow(new_line)   