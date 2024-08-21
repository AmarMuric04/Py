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
# for key in programming_dictionary:
# ---- print(programming_dictionary[key])

# Nested dictionaries
capitals = {"Serbia": "Novi Pazar", "France": "Paris"}

# travel_log = {"Serbia": ["Novi Pazar", "Belgrade", "Novi Sad"]}

# print(travel_log["Serbia"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "Serbia": {
        "cities_visited": ["Novi Pazar", "Belgrade", "Novi Sad"],
        "total_visits": 10,
    },
    "UAE": {
        "cities_visited": ["Dubai"],
        "total_visits": 1,
    },
}

print(travel_log["UAE"]["cities_visited"][0])
