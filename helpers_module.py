# Modules:
# *****************************************************
# Here is my module (python file created/written by us)
# *****************************************************

# creating a module on our own project
# Modules: are files with functions and other reusable blocks of code,
# which allows you to break complex projects into smaller, more manageable chunks.


# functions are useful for reuse and readability
# we want to take a list of our functions and use them in our application
# Or in other different applications
# we can do it by utilizing Modules
# and how can we import them into a separate projects is through the use of Packages

# ***********************************************************
# Creating a module (Think about the module is like a server)
# so this file is our module "helpers_module".py"
# this file can contain x number of functions/classes/etc...
# ***********************************************************

# Example:
# Below is our normal function named "display" to practice using modules
# this function accepts two parameters (expecting to receive two input/values):
# 1) message: should be a "string" by default but it can be any data type!!!!
# 2) is_raining: boolean either True (Yes) or False (No)

# NOTE:
# is_raining has a default value of "False" in case if we called this function without passing any argument
# which means if the user forgets to pass a value to it, its value will be "False"
# also message has a default value of "Here is my default message"

def display(message="Here is my default message", is_raining=False):
    # This condition will be True if is_raining has the value of "True" OR if it has any value
    if is_raining:
        # if variable => We are just asking if this variable has any value or if it's true Then do if block
        if message:  # This condition will be True if message has the value of "True" OR if it has any other value
            print(message)
        else:  # this else will run if message variable has no value "empty string"
            print('Warning! Take your umbrella')
    # in this simple function, if you don't put else the following print message will always run
    # but with else, this message will be printed if the condition is false
    else:
        print(message)


# Let's create another function:
def course_details(age):
    if age >= 18:
        print("Monday - Room#12 - 6:30 PM")
    else:
        print("Tuesday - Room#22 - 7:30 PM")


# Let's create another function:
# this function accepts a list (array) of numbers and returning the total value:
# we want to run this function against an array (list) of numbers
# we put a parameter named "number_list" to act as a place holder for the real list
# You can thing about number_list as a "Local Variable" that ONLY belongs to our function
def number_total(number_list):
    # using for loop with initial of total
    # number_list => a list that contains numeric values
    # declare a new variable with name "total"
    # has to have an initial value of 0
    total = 0
    # we need to use a loop to go through all the elements in this array "number_list"
    # in JS: for(var i=0; i<=number_list.length; i++) { our code goes here }
    for number in number_list:
        # In JS: total += number_list[i]
        # assume number_list = [45.6, 12.78, 10.89, 23.42]
        # adding 45.6 to my container "total"
        # total=total+number # total = 0 + 45.6
        # Or the short way:
        total += number  # the same as we wrote before: total=total+number
    return total    # at the end of this function: return the final total


# Another function to find/return the average (mean) of a list (array) of numbers:
def number_avg(number_list):
    # finding the total by calling our other function number_total():
    total = number_total(number_list)
    return total/len(number_list)

# our last function to find/return True if even number and False if odd:
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
# we can access variables also:
course = "Python"

# ********************************************************************************
# Just to review:
# Notes about comment in Python:
# Python only has one official way of doing comments and that is using #.
# using """ is not considered to be full official comment!

"""
Some people using this simple for writing multiple-lines of comments
But it's just a string in Py!!!
Py will read this string 

Django Framework Developers, using this way of comments also
"""
# In JS, we have // for one line comment, and we /* */ for multiple-lines comment

# Check this line below about comments!!!!!
my_text = """
you might think that this is a multiple-lines comment
but it's a text value (string) 
line 1
line 2
line 3
line 4
"""
print(my_text)

# Modules can have classes
# Notice there is no code block for this class, it's empty => using "pass"
class Member():
    pass

# using "pass" with functions:
def calculate_tax(price):
    pass
