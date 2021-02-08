# NOTE: We will use the idea packages in this file "helpers_module_packages.py"
# ***********************************************************************************************
# Packages: are modules published by other entities which you can incorporate into your projects.
# ***********************************************************************************************
# Packages: python file(s) written by other developers that we need to install
# You can search for many packages using: Python Package Index
# The link: https://pypi.org/

# *********************
# Installing Packages:
# *********************
# To install any package we use pip, which is a "command line" installer that we use to install any package:
# So let's take this example by installing "colorama" package, which a simple feature
# to help us change the color of our text when we print it in the terminal, yes that's it!

# We have two different ways to install packages:
# ************************************************
# First Way: Install an individual package (the basic standard official way)
# If you sure, that you only want to install one and only one package, you can install it individually:
# You don't want to put on Github or you don't want to share it with other developers:
# The syntax: pip install package_name
# pip install colorama

# Second Way: Install from a list of packages
# if you have a list of packages, we can set them up (list them) inside a text file
# This text file is frequently called/named "requirements.txt" <= (Strongly recommended)
# So requirements.txt contains the text "colorama" which is the module/package name, that's it
# and so on if you want to use other packages, you can just simply write the package name inside this text file
# so it's just a text file the contains the name(s) of our package(s)

# We will import the color functions in this file to be used inside our own function:
# The link for this package: https://pypi.org/project/colorama/

# **********************************
# Packages and Virtual Environments:
# By Default, packages are installed "globally" if we just run the command: pip install package_name
# Python have different behaviour by installing all the Packages globally!!!!
# The drawbacks of globally installed packages:
# This package will be available for every application we want to build even if we don't want to use it!
# The version management will be difficult: we want to use version 2 for this project version 3 for other project and so on

# Virtual Environment:
# It's more practical to make a local installation for our packages for that specific application
# We can do it by utilizing something called "Virtual Environment",
# which is really just a folder that will contain  all the code (main filpie, modules, packages, etc...)
# to run the application we are creating
# Virtual Environment it's just a sub-folder inside our main root folder for our project

# Very Important Note:
# We installed Python version 3.7 or later, we already have these tools installed:
# pip <= You don't need to install pip tool
# virtaulenv <= You don't need to install virtaulenv

# *****************************************************************************
# Developers with old versions of Python, they need to install the virtual env.
# The Steps for creating a virtual environment (Just to get an idea DON'T USE IT):
# Install Virtual Environment:
# Please remember that this step you don't need it as Python 3.x you have it already installed with pip
# the syntax =>> pip install virtualenv
# ******************************************************************************

# The Official Steps to install/work with Packages:
# *************************************************
# Step 1: Create the virtual environment (in other word, the folder to hold/save all our packages):
# so Virtual Environment is nothing but a folder to isolate all the required packages for this project/website
# from other projects that we need to create in the future
# You will set up a virtual environment folder and activate it as explained later
# you will install tje package(s) inside the venv
# Note: you can type "cls" to clear the terminal window:
# To create a virtual environment, it has to be created inside the project root folder,
# online syntax (MAC)=>> python -m venv <Virtual_Env_folder_name>
# Use this syntax (PC-Windows) =>> py -m venv <Virtual_Env_folder_name> (OR:) py -3 -m venv <Virtual_Env_folder_name>
# By convension most Python developers will name it "venv" or sometimes "env"

# =================================================================================================
# Example: py -m venv venv
# Please notice that:
# the first "venv" will be the command name
# the second "venv" will be the name of the folder that we are creating, so I will name it "my-venv"
# ==================================================================================================

# But I will name my venv to be "my-venv"
# Hint: You can use the command "pip list" to see the installed packages
# This command is to create a virtual environment named "my-venv"=>>  py -m venv my-venv
# type the command then press "Enter"

# NOTE: Please make sure to run the command for creating a venv inside your project folder
# you can use File explorer in windows or mac to access your folder then you can run:
# Powershell (Windows) => Just type "powershell" inside the address bar of this folder
# CMD (Windows)
# Terminal (Mac)
# Or we can user the terminal window that comes with VS Code

# Step 2: Using the Virtual Environment (Activate it)
# When it's the time to use the virtual environment, we need to activate this virtual environment:
# In Windows systems, two different locations:
# 1) inside the command line prompt (cmd.exe) batch syntax =>> <venv_folder>\Scripts\Activate.bat
# 2) inside the Windows Powershell (Or Your VS CODE Powershell):
# Syntaxes:
# Syntax1: =>> <venv_folder>\Scripts\Activate.ps1
# Syntax2: OR # the syntax =>> .\<venv_folder>\Scripts\activate
# Syntax3: OR just type: <venv_folder>\Scripts\activate
# 3) inside Bash shell "Git Bash": syntax =>> . ./<folder_name>/Scripts/activate
# This command (for point 2) is to activate our virtual environment named "my-venv"=>>  my-venv\scripts\activate
# By the way, we can exit/deactivate the venv with this syntax =>> deactivate

# *************************************************************************
# If you activate a venv for the first time in any Windows Computer,
# you might receive an error: cannot be loaded because running scripts is disabled on this system [Execution Policy].
# And this error or warning is because "Microsoft Execution Policies"
# Microsoft Windows Execution Policies:
# PowerShell's execution policy is a safety feature
# that controls the conditions under which PowerShell loads configuration files and runs scripts.
# This feature helps prevent the execution of malicious scripts.
# you can check this article (link):
# https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-executionpolicy?view=powershell-7

# The solution:
# *************
# syntax =>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# PowerShell:  you can type the command inside VS code Terminal Window or PowerShell:
# A command to change an execution policy can succeed but still not change the effective execution policy.
# ********************************************************************************************************

# now every time we open the folder it will activate the Virtual .Env for us
# and you can check the VS Code status bar to confirm that we are working inside our virtual environment
# for this project folder

# Step 3: Installing the required package(s) in a virtual environment:
# Install an individual package:
# the syntax =>> pip install colorama
# Note: you can use the command: pip list
# This command will show you all the installed packages for this current project
# Let's try using the second way in very basic way:
# A) Create a simple text file with the name "requirements.txt" (inside the project root folder)
# B) Just write the package name(s) exactly, save it
# C) the syntax =>> pip install -r requirements.txt


# Step 4: We will import the required modules and functions from this package:
# **************************************************************************************************

# Starting the block of Package Coding ******************************
# from colorama module, we need to use init function:
# Below is our code with the function to practice using packages
# From the full package of "colorama" we will just import two componets (classes): Fore and Back
# Fore and Back are two classes and that's why they start with Capital function Instructor()
from colorama import init, Fore, Back


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


def course_deatails(age):
    if age >= 18:
        print("Monday - Room#12 - 6:30 PM")
    else:
        print("Tuesday - Room#22 - 7:30 PM")


def number_total(number_list):
    total = 0
    for number in number_list:
        total += number  # the same as we wrote before: total=total+number
    return total    # at the end of this function: return the final total


display("Here is my text", True)
