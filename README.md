# Python Modules and Packages Quick Demonstration

## About This Repo:
Quick and Basic Demonstration About How to Use Modules and Packages in Python. For "Full-Stack Software Development (FSSD) Diploma" and "Computer Programming Diploma" Programs.

# Working with Modules:
Modules allow you to store reusable blocks of code, such as functions, in separate files. 
They're:
- simply python files (with .py extension)
- referenced by using the import statement. 

|***:computer: Code Reference***|
|:---:|
|***1- Code File: helpers_module.py***|
|***2- Code File: main_app1.py***|

# Working with Packages:
Packages: are modules published by other entities which you can incorporate into your projects. they are python file(s) written by other developers that we need to install first then we can import them later.
You can search for many packages using: Python Package Index => The link: https://pypi.org/

**Note: you can type "cls" to clear the terminal window:**

|***:computer: Code Reference***|
|:---:|
|***1- Code File: helpers_module_package.py***|
|***2- Code File: main_app2.py***|

## Installing Packages:
- To install any package we use a python tool named "pip",
- "pip" is a "command line" installer that we use to install any package:

So let's take this example by installing ["colorama package"](https://pypi.org/project/colorama/), which a simple feature to help us change the color of our text when we print it in the terminal, yes that's it!

### Very Important Note (locally with VScode - Not in Gitpod):
- Packages can be installed in two different ways (2 different modes):
  - >> globally (by default) => the installed package will be available and accessed by the current project
  or any other project you want to build later
  - >> in isolation mode => the installed package will be available and access by the current project ONLY

## Packages and Virtual Environments:
By Default, packages are installed "globally" if we just run the command: 
```
pip install package_name
```
Python have different behaviour by installing all the Packages globally!

The 2 major drawbacks of globally installed packages:
  1) This package will be available for every application we want to build even if we don't want to use it!
  2) The version management will be difficult: for example, we want to use version 2 for this project version 3 for other project and so on

**The Question:*** how can we install the package locally (in isolation mode) not globally?
**The Solution:** using "Virtual Environment"

## Virtual Environment (We will do it in our machines):
- It's more practical to make a "local" installation for our packages for every specific application
- We can do it by utilizing something called "Virtual Environment"
- Virtual Environment is:
  - really just a folder that will contain all the code of installed packages (dependencies) to run the application we are creating
  - Virtual Environment it's just a sub-folder inside our main root folder for our project


### Very Important Note:
With Python version 3.7 or later, we already have these two tools installed:
  > pip <= You don't need to install pip tool
  > virtualenv <= You don't need to install virtualenv (for Virtual Environment)

Developers with old versions of Python, they need to install the virtual env.
The Steps for installing a virtual environment (Just to get an idea DON'T USE IT):
  - Install Virtual Environment:
  - the syntax:=>> **pip install virtualenv**
Please remember that this step you don't need it as Python 3.x you have it already installed with pip

# The Official Steps to install/work with Packages:
## Step 1: Create the "virtual environment" (in other word, the folder to hold/save all our packages):
Virtual Environment is nothing but a folder to isolate all the required packages for this project/website from other projects that we need to create in the future.

- You will set up a virtual environment folder and activate it as explained later
- You will install the package(s) inside the venv.

To create a virtual environment, it has to be created inside the project root folder,
**online syntax (MAC)=>> python -m venv <Virtual_Env_folder_name>**
Use this syntax (PC-Windows):
**=>> py -m venv <Virtual_Env_folder_name> (OR:) py -3 -m venv <Virtual_Env_folder_name>**
By convension most Python developers will name it "venv" or sometimes "env"
Yes, we can name it anything: my-venv or modules-packages-venv or m-p-env, etc..

### Virtual Environment Commands: 
You can check these statements/commands from Vscode:
#### Linux
```
sudo apt-get install python3-venv   # If needed
python3 -m venv env
```

#### macOS
```
python3 -m venv env
```

#### Windows
```
python -m venv env
```

**Example:**
> py -m venv venv

Please notice that:
- the first "venv" will be the command name
- the second "venv" will be the name of the folder that we are creating,
- I will name it "my-venv" => py -m venv my-venv
- This command is to create a virtual environment named "my-venv"=>>  py -m venv my-venv
- type the command then press "Enter"


**NOTE:**
Please make sure to run the command for creating a venv inside your project folder
you can use File explorer in windows or mac to access your folder then you can run:
- Powershell (Windows) => Just type "powershell" inside the address bar of this folder
- CMD (Windows)
- Terminal (Mac)
- Or we can user the terminal window that comes with VS Code itself

## Step 2: Activate/Using the Virtual Environment 
When it's the time to use the virtual environment, we do need (have) to activate this virtual environment:
In Windows systems, two different locations:
  1) inside the command line prompt (cmd.exe) batch syntax =>> <venv_folder>\Scripts\Activate.bat
  2) inside the Windows Powershell (Or Your VS CODE Powershell):
    **Syntaxes:**
    - Syntax1: =>> <venv_folder>\Scripts\Activate.ps1
    - Syntax2: OR # the syntax =>> .\<venv_folder>\Scripts\activate
    - Syntax3: OR (for short) just type =>> <venv_folder>\Scripts\activate
  3) inside Bash shell "Git Bash": syntax =>> . ./<folder_name>/Scripts/activate

This command (for point 2) is to activate our virtual environment named "my-venv"=>>  my-venv\scripts\activate
By the way, **we can exit/deactivate the venv with this syntax =>> deactivate**

**NOTE:**
- You can check the VS Code status bar to confirm that we are working inside our virtual environment
- for this project folder, you can also check the project path:
  - **(my-venv) PS D:\Your Full path\01.Python-Modules-Packages>**


### Microsoft Windows Execution Policies
If you activate a venv for the very first time in any Windows Computer, you might receive an error: 
  - cannot be loaded because running scripts is disabled on this system [Execution Policy].

This error or warning is because "Microsoft Execution Policies". Microsoft Windows Execution Policies:
- PowerShell's execution policy is a safety feature that controls the conditions under which PowerShell loads configuration files and runs scripts. 
- This feature helps prevent the execution of malicious scripts.
- You can check this article (link): [Get-ExecutionPolicy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-executionpolicy?view=powershell-7)

#### The solution (Only needed for the first time):
- syntax =>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  - PowerShell:  you can type the command inside VS code Terminal Window or PowerShell:
- A command to change an execution policy can succeed but still not change the effective execution policy.

## Step 3: Installing the required package(s) in a virtual environment for your Application:
 We have two different ways to install packages (in local Vscode or Gitpod):
### First Way (First Step): Install an individual package (the basic standard official way)
- If you are sure, that you only want to install one and only one package, you can install it individually:
- You don't want to put on Github or you don't want to share it with other developers:
> The syntax: pip install package_name
- example installing the package "colorama" => **pip install colorama**

**Hint:** You can use the command **"pip list"** or **"pip freeze"** to see the installed packages.
This command will show you all the installed packages for this current project

### Second Way (Used by others): Using the requirements.txt file
Install from a list of packages
- if you have a list of packages, we can set them up (list them) inside a text file
- This text file is frequently called/named "requirements.txt" <= (Strongly recommended)
- So requirements.txt contains the text "colorama" which is the module/package name, that's it and so on if you want to use other packages, you can just simply write the package name inside this text file, so it's just a text file the contains the name(s) of our package(s)

**Reasons for requirements.txt:**
  1. Other programmers can understand and know the packages (dependencies) that we used in our app
  2. Other programmers can use this file to install all the package(s) that are listed inside it

**NOTE:** 
Yes, other users, they have the choice to create a virtual environment with any name

**Question:**
What is the command for installing the package(s) from the text file "requirements.txt"?
Answer: pip install -r requirements.txt

**NOTE:** to uninstall any package =>> pip uninstall colorama

### The text file "requirements.text":
To move the name of all our installed packages to this file (Creating/Updating the file):
  > pip freeze > requirements.txt

This command has two actions:
- Action1: Create/Update a file with the name "requirements.txt"
- Action2: Write all the installed packages for my current app/project
 
To install all the listed packages from this file:
  > pip install -r requirements.txt

**Code Samples:**
1- **Code File: helpers_module_packages.py**
2- **Code File: main_app2.py**


## Resources, References, and Credits:
- [Microsoft Learn Resources](https://learn.microsoft.com/?WT.mc_id=python-c9-niner)
- [Python 3.11.2 documentation](https://docs.python.org/3/index.html)
- MS VSCode - Python in Visual Studio Code
  - You can read more by visiting ["Python in Visual Studio Code"](https://code.visualstudio.com/docs/languages/python)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- W3Schools
- Please refer to my class materials and the pdf files for more details and explanations

#### NOTE: You can open any link in a new tab using either of the following ways:
- Hold down the CTRL Key in windows or the COMMAND key on Mac then click it
- Right-click the link and choose to open the link in a new tab or new window from the context menu
