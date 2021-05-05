#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
for i in range(1,50):
    
        if i % 2 == 0:
            print (math.sqrt(i))


# In[6]:


# Python code to generate
# random numbers and
# append them to a list
import random

# Function to generate
# and append them
# start = starting range,
# end = ending range
# num = number of
# elements needs to be appended
def Rand(start, end, num):
	res = []

	for j in range(num):
		res.append(random.randint(start, end))

	return res

# Driver Code
num = 10
start = 10
end = 100
print(Rand(start, end, num))


# In[ ]:


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))


# In[ ]:




