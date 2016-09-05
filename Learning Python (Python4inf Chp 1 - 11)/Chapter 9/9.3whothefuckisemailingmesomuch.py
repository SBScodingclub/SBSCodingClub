# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:59:50 2016

@author: varun
"""

fname = raw_input ('Enter file name: ')

try:
    fhand = open (fname)
    
except:
    print ('file "'),(fname),('" could not be opened')
    exit ()
    
dict1 = dict ()

for line in fhand:
    if line.startswith ('From '):
        #print line  #  Debug check to see if correct line is found
        words = line.split()
        #print words #debus check split command
        newadd = words[1]
        if newadd not in dict1:
            dict1[newadd] = 1
        else:
            dict1[newadd] = dict1[newadd] + 1
print dict1
        
