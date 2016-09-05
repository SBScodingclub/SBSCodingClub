# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:55:59 2016

@author: varun
"""

score = raw_input('enter your score:\n')

try:
    score = float (score)
    if score == 1:
        print ('A')
    elif score >= 0.9:
        print ('A')
    elif score >= 0.8:
        print ('B')
    elif score >=0.7:
        print ('C')
    elif score >=0.6:
        print ('D')
    elif score < 0.6:
        print ('F')
except:
    print ('obviously you failed fuckwith, but try entering a number')
        