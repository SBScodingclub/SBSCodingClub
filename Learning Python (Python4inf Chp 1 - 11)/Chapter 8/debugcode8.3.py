# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:17:17 2016

@author: varun
"""


fhand = open( 'mboxshorter.txt' )
count = 0
for line in fhand:
    words = line.split()
    #print 'Debug:' , words
    if len(words) == 0 : continue
    if words[0] != ('From' or 'from' or 0) : continue 
    print words [2]