# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:25:32 2016

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
#print ('\n'), dict1  ##Debug## Is the dictonary fine?


### above from here is establishing a histogram of emails and numnber of times youve been emailed###

largest = None

for values in dict1:
    #print dict1[values] #is it finding the values?
    if dict1[values] > largest:
        largest = dict1[values]
        
###Above is for finding out who sent the most emails###

for key in dict1:
    #print key ##Debug## this checks its cycling the keys
    if dict1[key] == largest:
        print key, dict1[key]

###Above uses what was found in the previous loop and links it to a key###



    



