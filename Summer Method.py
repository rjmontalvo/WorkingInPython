#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Set a number in x and use summer() to calculate the sum of all the values that are multiples of 3 or 5 up to that number
##Give x a value to test in summer()
x= 975

##Define summer function
def summer(x):
    ##Find all the numbers up to but not including the given number
    y = range(x)
    ##Create an empty list to store the numbers
    numList = []
    ##For each number in the list that is divisible by 3 or 5 without a remainder, add to the list
    for num in y:
        if (num % 3 == 0) or (num % 5 == 0):
            numList.append(num)
    ##Find the sum of all the numbers in the list
    total = sum(numList)
    ##Print the total
    print(total)

##Call the function with the passed value
summer(x)

