"""
# Let's talk about local, global and nonlocal variables

## Implicit scopes
* When a variable is defined outside a method, it's global. This means it's available everywhere
* When a variable is defined inside a function, it's local. It's available only within the method. You can have a
local variable with the same name of an existing global variable and both can have different values

## Global keyword
Use the `global` keyword to modify a global variable in a method.

## Nonlocal keyword
The `nonlocal` keyword is used to modify a variable in the outer scope. ex: nested functions
"""

# The global variables
unchanged_global = "I won't be changed"
changed_global = "I will be changed soon"
local_sibling_global = "I have a local sibling"


def chill_method():
    global changed_global
    local_sibling_global = "I have a global sibling"
    changed_global = "And I have changed"
    print(f"The value of unchanged_global inside chill_method : {unchanged_global}")
    print(f"The value of changed_global inside chill_method : {changed_global}")
    print(f"The value of local_sibling_global inside chill_method : {local_sibling_global}")


def chill_method_goes_deep():
    chill_changed_variable = "I will be changed soon"
    chill_unchanged_variable = "I have a sibling in inner class"

    def chill_method_again():
        nonlocal chill_changed_variable
        global changed_global
        chill_changed_variable = "I am changed in chill_method_again"
        chill_unchanged_variable = "I have a sibling in outer class"
        changed_global = "Changed again in inner class"
        print(f"The value of chill_changed_variable inside chill_method_again: {chill_changed_variable}")
        print(f"The value of chill_unchanged_variable inside chill_method_again : {chill_unchanged_variable}")

    chill_method_again()
    print(f"The value of chill_changed_variable outside chill_method_again: {chill_changed_variable}")
    print(f"The value of chill_unchanged_variable outside chill_method_again : {chill_unchanged_variable}")


print("---GLOBAL KEYWORD---\n")
chill_method()
print('-'*200)

print(f"The value of unchanged_global outside chill_method : {unchanged_global}")
print(f"The value of changed_global outside chill_method : {changed_global}")
print(f"The value of local_sibling_global outside chill_method : {local_sibling_global}")
print('-'*200)

print("---NONLOCAL KEYWORD---\n")
chill_method_goes_deep()
print('-'*200)

print(f"The value of unchanged_global outside chill_method : {unchanged_global}")
print(f"The value of changed_global outside chill_method : {changed_global}")
print(f"The value of local_sibling_global outside chill_method : {local_sibling_global}")
print('-'*200)
