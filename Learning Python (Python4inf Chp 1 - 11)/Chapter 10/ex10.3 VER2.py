# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:09:24 2016

@author: varun
"""

import string
letterbox = dict()
words = []

fname = raw_input ('Please enter a file name:')

try:
    fhand = open (fname)

except:
    print ('file "'),(fname),('" could not be opened')
    exit ()
    
for line in fhand:
    #print line ##Debug## to see the original lines 
    line = line.translate(None, string.punctuation)
    line = line.translate(None, string.digits)
#    print line  ##DEBUG## #punctuation removal check
    line = line.lower()
    line = line.split()
    
    for words in line:
        for letters in words:
            for letters in words:
                if letters not in letterbox:
                    letterbox[letters] = 1
                else:
                    letterbox[letters] = letterbox[letters] + 1

#print letterbox ##Is the dict working##

t = letterbox.items()
l = list()

#print t  ##Debug##  Chcking listing porcess makes a tuple

for key, val in t:
    l.append( (val,key))
    
#print l ##Debug## #is itreversing the tuples

l.sort(reverse=True)

print ('\n'), l   