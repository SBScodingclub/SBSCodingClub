# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:44:56 2016

@author: varun
"""
count = 0
numb = 0
total = 0

#file reader



while True:
    
    filen = raw_input ('enter file name:')
    count = 0
    
    try:
        fhand = open (filen)
        print  fhand
        for line in fhand:
            count = count + 1
        print 'there were' , count , 'lines in the document'        
        
   
   

    except:
           
        if filen == 'nanabooboo.txt' :
            print (' NA NA BOO BOO TO YOU TOO, youve been punked' )
            exit()       
        
        else:
            print ('File cannot be opened:', fname)
            
        
      


else:        
        
    print 'please enter a valid file name'
   
        
