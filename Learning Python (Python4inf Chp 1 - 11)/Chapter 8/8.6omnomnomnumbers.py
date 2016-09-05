# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:05:04 2016

@author: varun
"""
numbers = []

while True:
    
    singlenumber = raw_input ( 'Enter some numbers and when your done write done: ')
    
    try:
        
        float (singlenumber)
        numbers.append (singlenumber)
        #print numbers debug tells you if the list is being appended
        
        
    except:
        
        if singlenumber == ('done'):
            print min (numbers)
            print max (numbers)
            break
        else:
            print ('try entering a number cunt' )