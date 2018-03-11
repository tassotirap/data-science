#!/usr/bin/python

import sys
import re

regex = '([(\d\.)]+) (.+) (.+) \[(.*?)\] "(.*?)" (\d+) (.+)'

for line in sys.stdin:

    result = re.match(regex, line)

    if not result:
        continue

    print "{0}\t{1}".format(result.groups()[4], 1)