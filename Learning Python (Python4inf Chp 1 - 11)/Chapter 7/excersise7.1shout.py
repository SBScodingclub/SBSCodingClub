# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:45:10 2016

@author: varun
"""

try:
    filen = raw_input ('enter file name:')
    fhand = open(filen)
    print  fhand
        
except: 
        
    print 'please enter a valid file name'
    
for line in fhand:
    line = line.upper()
    print line
    