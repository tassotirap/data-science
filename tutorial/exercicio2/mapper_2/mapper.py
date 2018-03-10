#!/usr/bin/python

import sys
import re

# regex = '([(\d\.)]+) (.+) (.+) \[(.*?)\] "(.*?)" (\d+) (.+)'

for line in sys.stdin:

    # result = re.match(regex, line)

    if not '10.99.99.186' in line:
        continue

    print "{0}\t{1}".format('10.99.99.186', 1)