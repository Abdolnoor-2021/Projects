# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 08:46:21 2021

@author: Abdolnoor Khaleghi
"""

# Import Numpy package
import numpy as np

# Create the arrays

a = np.array([3,6,4,5])
b = np.array([5,9,1,6])

#3 Compute the size, mean, median, and sum of each array a and b

np.size(a)
print(np.size(a))
np.size(b)
print(np.size(b))
np.mean(a)
print(np.mean(a))
np.mean(b)
print(np.mean(b))
np.median(a)
print(np.median(a))
np.median(b)
print(np.median(b))
np.sum(a)
print(np.sum(a))
np.sum(b)
print(np.sum(b))

#4 Preform the operations

a+b
print(a+b)
a-b
print(a-b)
a*b
print(a*b)
a**b
print(a**b)
a%b
print(a%b)

# 5 Make two new arrays, a_odd and b_odd

a_odd = []
b_odd = []

for l in a[1::2]:
    a_odd.append(l)
print("a odd : ", a_odd)

for l in b[1::2]:
    b_odd.append(l)
print("b odd : ", b_odd)
print("\n")

a_odd = np.array(a[0:1:5])
b_odd = np.array(b[0:3:9])


# 6 Two ways to create an array containing all integer values between 1 and 10000
10000
1
range(1,10000)
array1 = list (range(1,10000))
print(array1)

2
range(10000)
array2 = range(10000)
print(array2)

# Guess the number

import random

number = random.randint(1,100)

chances = 0
  
print("Guess a number (between 1,100)")  
  
# While loop to count the number 
# of chances 
while chances < 6: 
      
    # Enter a number between 1 to 100  
    guess = int(input()) 
      
    # Compare the user entered number   
    # with the number to be guessed  
    if guess == number: 
          
        # if number entered by user   
        # is same as the generated   
        # number by randint function then   
        # break from loop using loop  
        # control statement "break" 
        print("Congratulation YOU WON!!!") 
        break
          
    # Check if the user entered   
    # number is smaller than   
    # the generated number  
    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 
  
    # The user entered number is   
    # greater than the generated  
    # number              
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
          
    # Increase the value of chance by 1 
    chances += 1
          
          
# Check whether the user   
# guessed the correct number  
if not chances < 6: 
    print("YOU LOSE!!! The number is", number)