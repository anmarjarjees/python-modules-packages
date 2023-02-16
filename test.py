# ********************************************************
# Part of my lecture in using Python with Google Excel API 
# ********************************************************

# Now We can import the entire gspread library so we can access any class or method within it:
import gspread

# importing just the Credentials class which part from the service_account function from Google auth library. 
# We don't need to import the entire library 
from google.oauth2.service_account import Credentials


# We will need to write some line of required settings (like a template) to access our spreadsheet data:

# First:
# We need to set our scope:
# the "SCOPE" lists the APIs that the program should access in order to run:
# the values of the "scope" variable will not change so it's known as a "constant" which a variable that shouldn't be changed
# In Python we write constant variable in capitals
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Second:
# Creating another constant varaible named "CREDS":
# We call the form_service_account_file method of the "Credentials class"
# Passing our JSON file "creds.json"
CREDS = Credentials.form_service_account_file('creds.json')

# Third:
# Creating anther constant varaible "SCOPED_CREDS"
# Using the "with_scopes" method of the "CREDS" object
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Fourth:
# Creating our GSPREAD_CLIENT using gspread.authorize method
# Passing our "SCOPED_CREDS"
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Fifth:
# Open an access to our sheet inside love_sandwiches file
# Passing the name that we gave to our spreadsheet which is "love_sandwiches"
SHEET = GSPREAD_CLIENT.open("love_sandwiches") 

# Sixth:
# Now can access the data in our sheet "sales"
# By using the method "worksheet()" of SHEET object
# this method will return the work sheet data
# passing the text value 'sales' which corresponds to the name of the worksheet
# saving the returned data into a variable named "sales"
sales = SHEET.worksheet('sales')

# Every Google Account has "IAM" configuration which is stands for "Identity and Access Management"
# IAM specifies what the user has access to

# Now we will write the normal Python:

# Creating a variable named "data" (Testing the API Settings):
# Using gspread method "get_all_values()" to pull all the values from our sales worksheet
data = sales.get_all_values()

print(data)

# to run a project: => python3 run.py OR python run.py