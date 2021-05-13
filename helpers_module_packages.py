# NOTE: We will use the idea "packages" in this file "helpers_module_packages.py"
# ***********************************************************************************************
# Packages: are modules published by other entities which you can incorporate into your projects.
# ***********************************************************************************************
# Packages: python file(s) written by other developers that we need to install first then we can import them later
# You can search for many packages using: Python Package Index
# The link: https://pypi.org/

# Note: you can type "cls" to clear the terminal window:

# *********************
# Installing Packages:
# *********************
# To install any package we use a python tool named "pip",
# which is a "command line" installer that we use to install any package:
# So let's take this example by installing "colorama" package, which a simple feature
# to help us change the color of our text when we print it in the terminal, yes that's it!

# Very Important Note (locally with VScode - Not in Gitpod):
# Packages can be installed in two different ways (2 different modes):
# >> globally (by default) => the installed package will be available and accessed by the current project
# or any other project you want to build later
# >> in isolation mode => the installed package will be available and access by the current project ONLY

# **********************************
# Packages and Virtual Environments:
# By Default, packages are installed "globally" if we just run the command: pip install package_name
# Python have different behaviour by installing all the Packages globally!!!!

# The 2 major drawbacks of globally installed packages:
# 1) This package will be available for every application we want to build even if we don't want to use it!
# 2) The version management will be difficult:
# we want to use version 2 for this project version 3 for other project and so on

# The Question: how can we install the package locally (in isolation mode) not globally?
# The Solution: using "Virtual Environment"


# Virtual Environment (We will do it in our machines):
# It's more practical to make a "local" installation for our packages for that "specific application"
# We can do it by utilizing something called "Virtual Environment",
# which is really just a folder that will contain all the code of installed packages (dependencies)
# to run the application we are creating
# Virtual Environment it's just a sub-folder inside our main root folder for our project


# Very Important Note:
# With Python version 3.7 or later, we already have these tools installed:
# > pip <= You don't need to install pip tool
# > virtualenv <= You don't need to install virtualenv (for Virtual Environment)


# *****************************************************************************
# Developers with old versions of Python, they need to install the virtual env.
# The Steps for installing a virtual environment (Just to get an idea DON'T USE IT):
# Install Virtual Environment:
# Please remember that this step you don't need it as Python 3.x you have it already installed with pip
# the syntax =>> pip install virtualenv
# ******************************************************************************


# The Official Steps to install/work with Packages:
# *************************************************
# Step 1: Create the "virtual environment" (in other word, the folder to hold/save all our packages):
# -------------------------------------------------------------------------------------------------
# so Virtual Environment is nothing but a folder to isolate all the required packages for this project/website
# from other projects that we need to create in the future
# You will set up a virtual environment folder and activate it as explained later
# you will install the package(s) inside the venv
# To create a virtual environment, it has to be created inside the project root folder,
# online syntax (MAC)=>> python -m venv <Virtual_Env_folder_name>
# Use this syntax (PC-Windows):
# =>> py -m venv <Virtual_Env_folder_name> (OR:) py -3 -m venv <Virtual_Env_folder_name>
# By convension most Python developers will name it "venv" or sometimes "env"
# Yes we can name it anythong: my-venv or modules-packages-venv or m-p-env

# You can check these statements/commands from Vscode:
"""
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv env

# macOS
python3 -m venv env

# Windows
python -m venv env
"""

# Example: py -m venv venv
# Please notice that:
# the first "venv" will be the command name
# the second "venv" will be the name of the folder that we are creating,
# I will name it "my-venv" => py -m venv my-venv
# This command is to create a virtual environment named "my-venv"=>>  py -m venv my-venv
# type the command then press "Enter"


# NOTE: Please make sure to run the command for creating a venv inside your project folder
# you can use File explorer in windows or mac to access your folder then you can run:
# Powershell (Windows) => Just type "powershell" inside the address bar of this folder
# CMD (Windows)
# Terminal (Mac)
# Or we can user the terminal window that comes with VS Code itself


# Step 2: Activate/Using the Virtual Environment 
# -----------------------------------------------
# When it's the time to use the virtual environment, we do need (have) to activate this virtual environment:
# In Windows systems, two different locations:
# 1) inside the command line prompt (cmd.exe) batch syntax =>> <venv_folder>\Scripts\Activate.bat
# 2) inside the Windows Powershell (Or Your VS CODE Powershell):
# Syntaxes:
# Syntax1: =>> <venv_folder>\Scripts\Activate.ps1
# Syntax2: OR # the syntax =>> .\<venv_folder>\Scripts\activate
# Syntax3: OR (for short) just type =>> <venv_folder>\Scripts\activate
# 3) inside Bash shell "Git Bash": syntax =>> . ./<folder_name>/Scripts/activate
# This command (for point 2) is to activate our virtual environment named "my-venv"=>>  my-venv\scripts\activate
# By the way, we can exit/deactivate the venv with this syntax =>> deactivate


# NOTE:
# You can check the VS Code status bar to confirm that we are working inside our virtual environment
# for this project folder
# and also you can check the project path:
# (my-venv) PS D:\Your Full path\01.Python-Modules-Packages>

# *************************************************************************
# If you activate a venv for the very first time in any Windows Computer,
# you might receive an error: cannot be loaded because running scripts is disabled on this system [Execution Policy].
# And this error or warning is because "Microsoft Execution Policies"
# Microsoft Windows Execution Policies:
# PowerShell's execution policy is a safety feature
# that controls the conditions under which PowerShell loads configuration files and runs scripts.
# This feature helps prevent the execution of malicious scripts.
# you can check this article (link):
# https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-executionpolicy?view=powershell-7

# The solution (Only needed for the fist time):
# *********************************************
# syntax =>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# PowerShell:  you can type the command inside VS code Terminal Window or PowerShell:
# A command to change an execution policy can succeed but still not change the effective execution policy.
# *********************************************************************************************************


# Step 3: Installing the required package(s) in a virtual environment:
# --------------------------------------------------------------------
# Install an individual package:


# We have two different ways to install packages (in local Vscode or Gitpod):
# ***************************************************************************
# First Way (First Step): Install an individual package (the basic standard official way)
# If you sure, that you only want to install one and only one package, you can install it individually:
# You don't want to put on Github or you don't want to share it with other developers:
# The syntax: pip install package_name
# example installing the package "colorama" => pip install colorama


# Hint: You can use the command "pip list" or "pip freeze" to see the installed packages
# This command will show you all the installed packages for this current project

# Second Way (Used by others): Using the requirements.txt file
# Install from a list of packages
# if you have a list of packages, we can set them up (list them) inside a text file
# This text file is frequently called/named "requirements.txt" <= (Strongly recommended)
# So requirements.txt contains the text "colorama" which is the module/package name, that's it
# and so on if you want to use other packages, you can just simply write the package name inside this text file
# so it's just a text file the contains the name(s) of our package(s)

# Reasons:
# 1. Other people can understand and know the packages (dependencies) that we used in our app
# 2. Other people can use this file to install all the package(s) that are listed inside it
# NOTE: Yes, other users, they have the choice to create a virtual environment with any name

# Question: What is the command for installing the package(s) from the text file "requirements.txt"?
# Answer: pip install -r requirements.txt


# NOTE: to uninstall any package =>> pip uninstall colorama


# The text file "requirements.text":
# *********************************
# To move the name of all our installed packages to this file (Creating/Updating the file):
# >> pip freeze > requirements.txt
# This command has two actions:
# Action1: Create/Update a file with the name "requirements.txt"
# Action2: Write all the installed packages for my current app/project
 
# To install all the listed packages from this file:
# >> pip install -r requirements.txt

# Starting the block of Package Coding
# from colorama module, we need to use Fore, Back, Style classes or (init function):
# Below is our code with the function to practice using packages
# From the full package of "colorama" we will just import two componets (classes): Fore and Back
# Fore and Back are two classes and that's why they start with Capital Letters
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
    if is_raining:  # This condition will be True if is_raining has the value of "True" OR if it has any value
        # if variable => We are just asking if this variable has any value or if it's true Then do if block
        if message:  # This condition will be True if message has the value of "True" OR if it has any other value
            print(Fore.RED + message)
        else:  # this else will run if message variable has no value "empty string"
            print(Fore.BLUE+'Warning! Take your umbrella')
    # in this simple function, if you don't put else the following print message will always run
    # but with else, this message will be printed if the condition is false
    else:
        print(Back.GREEN + message)


# Let's create another function:
def course_deatails(age):
    if age >= 18:
        print(Fore.GREEN+"Monday - Room#12 - 6:30 PM")
    else:
        print(Fore.YELLOW+"Tuesday - Room#22 - 7:30 PM")


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


def number_avg(number_list):
    # finding the total by calling our other function number_total():
    total = number_total(number_list)
    return total/len(number_list)
