print("Welcome to the rollercoaster")
# height = int(input("What's your height in cm?: "))

height = 120
if height >= 120:
    print("Get in!")
else:
    print("HELL NO!")

# number = int(input("Give me a number: "))
number = 12

if number % 2 == 0:
    print("It's even!")
else:
    print("It's odd")

price = 0
if height >= 120:
    print("Get in!")
    # age = int(input("What's your age?: "))
    age = 11

    if age <= 12:
        print("Child tickets are 5$.")
        price += 5
    elif age <= 18:
        print("Youth tickets are 7$.")
        price += 7
    else:
        print("Adult tickets are 12$.")
        price += 12
    want_a_picture = input("Do you want a picture? (yes/no): ")

    if want_a_picture == "yes":
        print("Pay 3$.")
        price += 3
    else:
        print("Don't pay 3$.")

    print(f"Enjoy the ride and pay ${price}")
else:
    print("HELL NO!")
