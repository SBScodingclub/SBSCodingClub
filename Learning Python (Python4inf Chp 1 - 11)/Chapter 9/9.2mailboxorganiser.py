# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 18:42:43 2016

@author: varun
"""

fname = raw_input ('Enter file name: ')

try:
    fhand = open (fname)
    
except:
    print 'file name can not be openend: ' , fname
    exit()
    
dict1 = dict ()
    
for lines in fhand:
    if lines.startswith ('From '):
        #print lines    #Debug code: for line by line reading
        #lines = lines.lower()
        words = lines.split()
        #print words  #bug checl what words are being split out and used
        #for word in words:
            #print words[2]  #checking the correct word is selected
        newword = words[2]
            #print newword  #double check
        if newword not in dict1:
            dict1[newword] = 1
        else:
            dict1[newword] += 1
            #dict1 [word] = [word[3]]

print dict1