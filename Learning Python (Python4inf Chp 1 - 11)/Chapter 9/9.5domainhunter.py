# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:23:23 2016

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
        atpos = newadd.find('@')
        #print atpos ##Debug## Check the find command
        newaddsliced = newadd[atpos+1:]
        #print newaddsliced ##Debug## checking to see if flice is working
        if newaddsliced not in dict1:
            dict1[newaddsliced] = 1
        else:
            dict1[newaddsliced] = dict1[newaddsliced] + 1

print ('\n'), dict1  ##Debug## Is the dictonary fine?
