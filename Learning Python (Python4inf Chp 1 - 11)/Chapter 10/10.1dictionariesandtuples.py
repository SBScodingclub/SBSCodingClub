# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:42:35 2016

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
#print '\n' , dict1
        
t = dict1.items()
l = list()

#print t  ##Debug##  Chcking listing porcess makes a tuple

for key, val in t:
    l.append( (val,key))
    
#print l ##Debug## #is itreversing the tuples

l.sort(reverse=True)

print ('\n'), l[0]   
    
    


