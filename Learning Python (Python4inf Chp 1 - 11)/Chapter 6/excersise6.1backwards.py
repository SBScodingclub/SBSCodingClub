# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:51:00 2016

@author: varun
"""

fruit = 'banana'
index = -1
while index < len(fruit) and index > (len(fruit) +1) * -1:
    letter = fruit[index]
    print letter
    index = index - 1
