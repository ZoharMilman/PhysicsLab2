# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:55:06 2022

@author: zorik
"""

#%%
"Hello World"

print("Hello World!")
#%%

#%%

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Hello")
strings.append("World")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#%%


#%%

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10 
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
    
#%%


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s your balance is %.2f"

print(format_string % data)

#%%

x = [1,2,3]
y = x
print(x == y) # Prints out True
print(x is y) # Prints out False


#%%

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if (number % 2 == 0): 
        print(number)
    if (number == 237):
        break

#%%
import re

# Your code goes here
find_members = []
functions = dir(re)
for func in functions :
    if "find" in func:
        find_members.append(func)

print(sorted(find_members))

#%%

import numpy as np 

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg

np_weights_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg

np_weights_pounds = np_weights_kg * 2.2

# Print out np_weight_lbs

print(np_weights_pounds)

#%%
