#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

userInfo = None

for line in reader:

    thisType = line[1]

    if thisType == 'A':
        userInfo = line
    
    elif thisType == 'B':
        if userInfo and userInfo[0] == line[0]:
            new_line = []
            new_line.extend(userInfo)
            new_line.extend(line)
            writer.writerow(new_line)