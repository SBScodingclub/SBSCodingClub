# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:27:41 2016

@author: varun
"""

def counter () :
    count = 0
    for letter in word:
        if letter == character :
            count = count + 1
    print count    


word = raw_input ("please enter a word:")
character = raw_input ("please enter a letter to count:")

counter ()
