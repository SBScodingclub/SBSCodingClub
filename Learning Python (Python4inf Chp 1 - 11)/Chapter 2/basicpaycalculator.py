
"""
Created on Mon Apr 18 20:10:55 2016

@author: varun
"""

hours = raw_input ('How many hours did you work?\n')
rate = raw_input ('What is your pay rate?\n')
try
    hours = int (hours)
except
    print ('please enter a whole number')    
try
    rate = float (rate)
except 
    print ('please enter an hourly rate')

if hours > 40
    pay = (hours - 40) * rate*1.5) + (40 * rate)
else:
    pay = hours * rate
print pay