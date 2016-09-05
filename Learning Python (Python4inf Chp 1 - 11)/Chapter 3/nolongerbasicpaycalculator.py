
"""
Created on Mon Apr 18 20:10:55 2016

@author: varun


"""





def computehours ():

    hours = hours

    try:
           
        hours = float (hours)
        
    
         
    except: 
        
        print ('you did not enter a integer please enter a number\n')
        
        computehours()

def computerate ():
    
   
    rate = rate     
    try:
        
        rate = float (rate)
        
        
    except: 
        print ('you did not enter a integer please enter a number\n')
        
        computerate()



hours = raw_input ('How many hours did you work?\n')

rate = raw_input ('What is your pay rate?\n')

computehours()



computerate()   
       
if hours > 40:
    pay = ((hours - 40) * rate*1.5 ) + (40 * rate)
        
else:
    pay = hours * rate
            
print pay




