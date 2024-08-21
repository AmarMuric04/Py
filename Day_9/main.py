programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

# print(programming_dictionary["Bug"])

programming_dictionary["Hash"] = "Array with indecies created out of given keys."
# print(programming_dictionary["Hash"])

empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "a bug..."
# print(programming_dictionary)

# Looping
for key in programming_dictionary:
    print(programming_dictionary[key])

# Nested dictionaries
