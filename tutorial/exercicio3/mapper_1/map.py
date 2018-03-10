#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    # YOUR CODE HERE
    body = line[4]
    splitters = [' ','.',',','!','?',':',';','"','(',')','<','>','[',']','#','$','=','-','/']
    words = [body]
    for s in splitters:
        temp_words = []
        for w in words:
            temp_words.extend(w.split(s))
        words = temp_words

    for w in words:
        print "{0}\t{1}".format(w.lower(), 1)
        