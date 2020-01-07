#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def getMeanValue(valueList):
    """
    Calculate the mean (average) value from a list of values.
    Input: list of integers/floats
    Output: mean value
    """
    valueTotal = 0.0
 
    for value in valueList:
        valueTotal += value
    numberValues = len(valueList)
    
    return (valueTotal/numberValues)

