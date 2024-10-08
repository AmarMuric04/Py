print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
elif size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
else:
    print("Unrecognised input.")

if extra_cheese == "Y":
    bill += 1

print(f"Final price of your pizza is ${bill}")

# With logic operators


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "L":
    bill = 25
elif size == "M":
    bill = 20
elif size == "S":
    bill = 15
else:
    print("Unrecognised input.")

if size == "L" and pepperoni == "Y" or size == "M" and pepperoni == "Y":
    bill += 3
if not size == "L" and not size == "M" and pepperoni == "Y":
    bill += 2

if extra_cheese == "Y":
    bill += 1

print(f"Final price of your pizza is ${bill}")
