# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:12:09 2016

@author: varun
"""

fname = raw_input ('Please enter a file name:')

try:
    fhand = open (fname)

except:
    print ('file "'),(fname),('" could not be opened')
    exit ()

dict1 = dict()
newwords = dict()

for line in fhand:
    if line.startswith ('From '):
        #print line  #  Debug check to see if correct line is found
        words = line.split()
        #print words #debus check split command
        #day = words[4]
        hours = words[5]
        atpos = hours.find(':')
        hourssliced = hours[:atpos]
        #print day, hourssliced  ##Debug## checking to see if thhe hunt worked
        if hourssliced not in dict1:
            dict1[hourssliced] = 1
        else:
            dict1[hourssliced] = dict1[hourssliced] + 1


print dict1


l = list()

for key, val in dict1.items():
    l.append( (key,val))

l.sort()

print l


#print newwords

    
