# NOTE: We will use the idea "packages" in this file "helpers_module_packages.py"
# *******************************************************************************

# Starting the block of Package Coding
# from colorama module, we need to use Fore, Back, Style classes or (init function):
# Below is our code with the function to practice using packages
# From the full package of "colorama" we will just import two components (classes): Fore and Back
# Fore and Back:
# - are two classes and that's why they start with Capital Letters
# - are used to add colours: Fore => foreground color and Back => background color
from colorama import Fore, Back
# Error message if the package is in not installed :
# ModuleNotFoundError: No module named 'colorama'

# Examples from the Colorama page:
# The link for this package: https://pypi.org/project/colorama/
"""
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print('back to normal now')
"""

def display(message="Here is my default message", is_raining=False):
    if is_raining:  
        if message: 
            print(Fore.RED + message)
        else:  
            print(Fore.BLUE+'Warning! Take your umbrella')    
    else:
        print(Back.GREEN + message)

def course_details(age):
    if age >= 18:
        print(Fore.GREEN+"Monday - Room#12 - 6:30 PM")
    else:
        print(Fore.YELLOW+"Tuesday - Room#22 - 7:30 PM")

