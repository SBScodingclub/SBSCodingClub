# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:46:37 2016

@author: varun
"""

total = 0
count = 0
smallest = None
largest = None
   
    
        
        
while True:
    number = raw_input('Enter some numbers: ')
    try:
        number = int(number)
        
        if smallest is None or number < smallest:
            smallest = number
            
        if largest is None or number > largest:
            largest = number
            

        total = number + total
        
        count = count + 1
       
           
        
    except:
        
        if number == 'done':
               break 
        print 'try entering a whole number'
        
    
        
        
             
print 'total:', total, 'count:', count , 'average:', total/count, 'largest:', largest, 'smallest:' , smallest
