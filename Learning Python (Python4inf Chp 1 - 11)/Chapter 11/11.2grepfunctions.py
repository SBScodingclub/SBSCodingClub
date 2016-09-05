# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 12:13:04 2016

@author: varun
"""

import re
f = []
total = 0
count = 0

#regex = raw_input ('Please enter a regular expression:')
regex = ('^New Revision*.+ ([0-9]+)')

fname = raw_input ('Please enter a file name:')

try:
    fhand = open (fname)

except:
    print ('file "'),(fname),('" could not be opened')
    exit ()



for line in fhand:
    #print line ##DEBUG## is it running though th lines
    line = line.rstrip()
    if re.findall(regex, line):
        count = count + 1
#        f.append (re.findall(regex, line))
        x = re.findall(regex, line)
#        print x ##Debug## Is it splitting correctly
        y = x[0]
        y = float(y)
#        print y ##DEBUG## floating point conversion check
        total = total + y
#        print line ##Debug## Is it finding everything


#print total ##DEBUG## total check       
        
print ('New revision score:'), total/count


