# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:29:21 2016

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
            words.append(letters)
print words

    
    
#for letters in words:
#    if letters not in letterbox:
#        letterbox[letters] = 1
#    else:
#        letterbox[letters] = letterbox[letters] + 1
#
##print lines
#print letterbox
