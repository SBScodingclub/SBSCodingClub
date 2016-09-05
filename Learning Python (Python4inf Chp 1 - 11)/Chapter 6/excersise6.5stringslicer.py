# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:23:08 2016

@author: varun
"""

str = 'X-DSPAM-Confidence: 0.8475'
pos = str.find(':')
num = str[pos+1:]
num = float(num)
print num
print type(num)