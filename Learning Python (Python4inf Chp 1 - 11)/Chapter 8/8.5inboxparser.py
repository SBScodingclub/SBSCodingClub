# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:34:38 2016

@author: varun
"""
count = 0
data = raw_input ('enter file name:')
fhand = open (data)
#print fhand #check opening commands

for line in fhand:
    if line.startswith ('From '):
        #print line #check the search for from works
        words = line.split()
        #print words #checking split command
        print words[1]
        count = count + 1
print count