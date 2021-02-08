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

# First Way: import module as namespace:
# **************************************
# using import python file name (no extension)
# below we are importing "helpers" which the file that contains our function(s)
from helpers_module import display
from helpers_module import *
import helpers_module
# so the import keyword will import all the functions inside helpers.py file
# this file has 3 functions inside it
# we need/have to write the file name then . then the function signature for every function we call
helpers_module.display('Not a warning')

# Second Way: import all (all the functions/code) into the current namespace (file) using the wildcard *:
# **********************************************
# using this way we don't need to specify the namespace "helpers" before our functions when we call them
# we can call any function by writing the function name and it's arguments
# so after importing everything, this will make everything in this module "helpers" become globally available
# or in more technical, it will imported into the current namespace (file) which is "modules-pure"
# so below we can just simply say/write display instead of "helpers.display()"
# Very Important Note: In this way if we don't use/call all the functions and the variables we will receive a warning (Problem)!
display('Not a warning')

# Third Way: import specific item(s) (specific functions) into current namespace
# *******************************************************
# below we are importing just this specific function "display" from our helpers.py file
# You can specify a list of functions using ,
# example of importing only tow functions: from helpers import display, course_deatails
# this might be a good choice!
display('Not a warning')

# ******************************************************************************************************
# Now we can call all our functions
# calling my function dispaly() without passing anything (value), so python will use the default values:
# message="Here is my default message"
# is_raining=False
display()  # Here is my default message

print("**************************************")
display("Stay at home", True)  # Stay at home
display("Don't go for walking today", True)  # Don't go for walking today
display("Take a bus", True)  # Take a bus
# You should stay at home and study python
display("You should stay at home and study python", False)
# Still you will have to stay at home
display("Still you will have to stay at home")
# Yes we can have this code!!! display(True,"Any text")

# below I am passing two string values instead of passing string and boolean
display("Stay inside", "raining")  # Stay inside
# Notice that based on our function signature we need to specify our empty string
# otherwise Python will assign the value of True to the function parameter "message"

# Because we are passing one value, so python will take it and just assigned it to first parameter message
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
