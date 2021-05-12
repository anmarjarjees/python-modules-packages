# Modules allow you to store reusable blocks of code, such as functions, in separate files.
# They're referenced by using the import statement.

# *************************************************************************
# here is the file where we need to import the module into it:
# If the module is the server so think about this file to act as the client
# *************************************************************************

# We have 3 different ways:
# There is no performance difference in these ways (all the same) and no logical difference
# It's just different method of accessing our module, or how are we going to call it
# it's a matter of personal preference


# First Way: from the module importing specific function(s)
# ********************************************************
# Example: from module_name import function_name
# below we are importing ONLY display from the "helpers_module" which is the file that contains our function(s)

# Way1: import module as namespace:
# below we are importing just this specific function "display" from our helpers_module.py file
from helpers_module import display
# You can specify a list of functions using ,
from helpers_module import display, number_total, number_avg
# Instead of listing all your functions as comma seprated values!
# It's better to import them all using * as explained in the second way:

# Second Way: import all (all the functions/code) into the current namespace (file) using the wildcard *:
# *******************************************************************************************************
# Way2: import module as namespace:
from helpers_module import *


# Third way: using just the import
# ****************************************
# the import keyword will import all the functions inside helpers_module.py file
# this file has 4 functions inside it
# we need/have to write the file name (specify the namespace)
# then . then the function signature for every function we call
# Way 3:
# using import python file name (no extension)
import helpers_module

# Besides calling our own custom module file(s)
# We can still use/call Python built-in modules
# Example below, we calling the module named "statistics":
# This module "statistics" provides functions for calculating mathematical statistics of numeric (Real-valued) data.
import statistics
# Or using this syntax:
from statistics import mean

# NOTE:
# In the first or second way we DON'T need to specify the namespace "helpers_module"
# before our functions when we call them
# we can call any function by writing the function name and it's arguments only
# These two ways: will make everything in this module "helpers_module" become globally available
# In the third way, we do need to specify:
# >> the "namespace" (module/python file name)
# >> then dot notation
# >> then function/varaible/class name
# Example: helpers_module.display()

# Now we can call all our functions:
# calling our function display() without passing any argument
# By default we will have:
# message="Here is my default message"
# is_raining=False
# ******************************************************************************************************
# calling my function dispaly() without passing anything (value), so python will use the default values:
# message="Here is my default message"
# is_raining=False

# ONLY for the third way:
# we need/have to write the file name then . then the function signature for every function we call
helpers_module.display()  # Here is my default message
# Very Important Note: In this way if we don't use/call all the functions and the variables
# we will receive a warning (Problem)!


helpers_module.display("It's fine")

# Note to remember :-)
# passing True => it's raining
# the default value is false => not raining
display("take your umbrella", True)


print(helpers_module.my_text)
print(my_text)

my_list = [89, 78.67, 90, 78.54, 4, 3]
# print("the total is: ", number)
helpers_module.number_avg


print("**************************************")
display("Stay at home", True)  # Stay at home
display("Don't go for walking today", True)  # Don't go for walking today
display("Take a bus", True)  # Take a bus

# You should stay at home and study python (Yes even if it's not raining)
display("You should stay at home and study python", False)

# Still you will have to stay at home
display("Still you will have to stay at home")
# Yes we can have this code!!! display(True,"Any text")

# below I am passing two string values instead of passing string and boolean
display("Stay inside", "raining")  # Stay inside
# Notice that based on our function signature we need to specify our empty string
# otherwise Python will assign the value of True to the function parameter "message"

# Because we are passing one value,
# so python will take it and just assigned it to first parameter "message"
display(True)  # message = True AND is_raining = False => output: True
# the same is here also:
display(False)  # output: Warning! Take your umbrella

# To make sure that these boolean values: True or False
# can go (assigned) to the second function parameter which is is_raining
# we do need to pass something to to the first first parameter in our function:
# Below we are passing just an empty string to the function parameter message and True to is_raining
# message will be "" empty string, nothing in between ""
# is_raining will be "True"
display("", True)  # Warning! Take your umbrella
# below is the same
# Notice that in the example (line) below we are passing the value of "False"
# to our function parameter named "is_raining"
# However, is_raining has the default value of "False"
# so Whether we put False of we don't as a second value, the result is the same
# Although we are passing an empty string, Python will assign this empty string to the parameter message!!!
# nothing just an empty line because we are passing empty string
display("", False)

display(None, False)  # None in Python is like Null in JavaScript # None

display(123456789)  # yes I am passing here numbers instead of string => 123456789
# have fun again by passing two numbers:
display(100, 200)  # 100
print("**************************************")

course_deatails(20)  # Monday - Room#12 - 6:30 PM

my_list = [89, 78.67, 90, 78.54, 4, 3]
# Because my function doesn't print and I want to print the total
# So we put/placed our function call inside print() function
print(number_total(my_list))  # None


# Notice that below we also need to use/call this variable "my_text"
# if we don't call it, we will receive this problem:
# Unused import my_text from wildcard importpylint(unused-wildcard-import)
print(my_text)

my_exams = [90, 87, 91, 92, 88, 85]
# avg (the mean):
avg = number_total(my_exams) / len(my_exams)
print("Average", avg)

# Or just calling our average function!!
print("Average", number_avg(my_exams))


# Or just calling the mean() function from the statistics module (build-in module):
print("Average", statistics.mean(my_exams))
# OR:
print("Average", mean(my_exams))
