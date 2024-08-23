import random

import maths


def my_function():
    for i in range(1, 21):  # 1, 20 -> 1, 21
        if i == 20:
            print("you got it")


my_function()

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = random.randint(0, 5)  # 1, 6 -> 0, 5
print(dice_num)

year = int(input("What's your year of birth?: "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:  # > -> >=
    print("You are a Gen Z.")

try:
    age = int(input("How old are you?: "))
except ValueError:
    print("Invalid input. Try again!")
    age = int(input("How old are you?: "))

if age > 18:
    print(f"You can drive at age {age}.")  # identation and added f in front of string

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 4, 5, 8, 13])
