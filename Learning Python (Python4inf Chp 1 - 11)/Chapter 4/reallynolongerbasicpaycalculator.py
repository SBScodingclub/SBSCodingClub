
"""
Created on Mon Apr 18 20:10:55 2016

@author: varun
"""

def computepay ():

    hours = raw_input ('How many hours did you work?\n')
    rate = raw_input ('What is your pay rate?\n')
    
    try:
        hours = float (hours)
        rate = float (rate)
    
        
    
        if hours > 40:
            pay = ((hours - 40) * rate*1.5 ) + (40 * rate)
        else:
            pay = hours * rate
            
        print pay
    
    
    except: 
        print ('you did not enter a integer please enter a number')
        computepay ()

computepay ()

