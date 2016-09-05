# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:22:05 2016

@author: varun
"""

morewords = [] # empty list

fhand = open ('romeo.txt')
for words in fhand:   #read each line
    s = words.split()    #split the words and assign to s
    #print s   debugging check that words are going to s
    for x in s:  # searching through s for assigned variable
        if x not in morewords: #if x isnt in the list more words then continue
            morewords.append(x)  # add it to the list
            #print x   #debug are we getting recognisation of x
            #print morewords # debug, is it storing in more words
morewords.sort()  #sort in more words
print morewords
    