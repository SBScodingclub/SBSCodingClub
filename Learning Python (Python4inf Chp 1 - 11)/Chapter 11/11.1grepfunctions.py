# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:09:29 2016

@author: varun
"""

import re
f = []
count = 0

regex = raw_input ('Please enter a regular expression:')

fhand = open ('mbox.txt')
#print fhand   ##DEBUG## is the file opening?



for line in fhand:
    line = line.rstrip()
    if re.findall(regex, line):
        f.append(re.findall(regex, line))
#        print line ##Debug## Is it finding everything
        count = count +1
#    print x
#    if len(x) > 0:
#        x = f
        
print ('there are') , count, ('lines countaining') , regex, (' in your search')
