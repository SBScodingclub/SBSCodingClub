# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:44:56 2016

@author: varun
"""
count = 0
numb = 0
total = 0

#file reader

try:
    filen = raw_input ('enter file name:')
    fhand = open(filen)
    print  fhand
        
except: 
        
    print 'please enter a valid file name'
    
    
        
 # file opener line by line
        
for line in fhand:
    line = line.rstrip()
    if line.startswith ('X-DSPAM-Confidence:') :
        print line
        count = count + 1
        print count
        pos = line.find(':')
        numb = line[pos+1:]
        print numb
        numb = float(numb)
        total = numb + total

print 'total: ', total , 'average spam confidence: ', total/count , 'count: ', count



