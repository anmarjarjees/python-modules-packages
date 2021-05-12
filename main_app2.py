# We are importing this file because of the packages
from helpers_module_packages import *

print(Fore.RED + 'some red text')

print(Back.GREEN + 'and with a green background')

print(Back.BLACK)
print(Fore.WHITE)


display("Stay at home", True)  # Stay at home


course_deatails(10)  # Monday - Room#12 - 6:30 PM

my_list = [89, 78.67, 90, 78.54, 4, 3]
# Because my function doesn't print and I want to print the total
# So we put/placed our function call inside print() function
print(number_total(my_list))  # None

my_exams = [90, 87, 91, 92, 88, 85]
# avg (the mean):
avg = number_total(my_exams) / len(my_exams)
print("Average", avg)