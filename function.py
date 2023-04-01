# functions in python
# collection of codes which performs a specific tasks
# helps to organize the code better and break the function into sections
# only runs when it is asked to


# key word in python --- def  (function define as def)
# name after the key word --- ex: sayhi


def say_hi():  # () is the parameter
    # can pass data (parameter)
    print("Hello user")


# return data as a result

say_hi()

""" arguments """


# information pass to function as an argument
# specified after the function name
# inside paranthesis
# as many arguments, seperate them with comma
# pass the first name to the same last name

def first_name(fname):
    print(fname + " Fernando")


first_name("Emil")
first_name("Tobias")
first_name("Linus")
# args


# function is more organisable than a variable
_my_var = "John"
print(_my_var)


# number of arguments
def num_arg(firstname, sname):
    print("my name is " + firstname + " " + sname)


num_arg("Imasha", "Sandi")  # output data

# number of args == number of output(data)

"""Arbitrary Arguments, *args"""


# if you don't know the number of arguments
# put a * before parameter name
def my_func(*kids):
    print("the youngest kid in my family is " + kids[0])


my_func("Emil", "Tobias", "Linus")

"""keyword args"""


# Keyword Arguments are often shortened to kwargs

def children(child3, child2, child1):
    print("The youngest of the family is " + child3)


children(child1="Emil", child2="Tobias", child3="Linus")  # reformat the args using keywords of the arguments
