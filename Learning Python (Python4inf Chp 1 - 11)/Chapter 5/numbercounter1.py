# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:14:09 2016

@author: varun
"""
total = 0
count = 0

   
    
        
        
while True:
    number = raw_input('Enter a number: ')
    try:
        number = float(number)
        
        total = number + total
        
        count = count + 1
       
           
        
    except:
        
        if number == 'done':
               break 
        print 'try entering a whole number'
        
    
        
        
             
print 'total:', total, 'count:', count , 'average:', total/count

