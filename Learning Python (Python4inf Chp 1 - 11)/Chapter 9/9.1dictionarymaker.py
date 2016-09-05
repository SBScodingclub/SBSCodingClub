# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:02:41 2016

@author: varun
"""
dict1 = dict ()
#count = 0
fhand = open ('words.txt')
#print fhand #check handle and opening
for lines in fhand:
    lines.strip()
    nwords = lines.split( )
    for words in nwords:
        #count = count+1
        dict1 [words] = words
    
    #print nwords  #check lines are printing


print dict1

print len(dict1)

