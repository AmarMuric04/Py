print("Hello"[0])

print("123" + "345")  # 123345
# print("123" - "345")

# Integer - Whole number!!!
print(123 + 345)  # 468

print(123_456_789)

# Float - Not a whole number!
print(3.14159)

# Boolean - True or False
print(True)
print(False)

# len(12345) # Error
len("12345")
print(len("12345"))

print(type("1234"))  # Check Type

print(type("123"))
print(type(123))
print(type(123.45))
print(type(True))

print(int(123) + int(456))

# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(2**5)

# print(4 - 2 * 3) # PEMDAS
print(3 * (3 + 3) / 3 - 3)

height = 1.85
weight = 96

bmi = weight / height**2

print(int(bmi))
print(round(bmi))
print(round(bmi, 4))

score = 0

# User scores a point!
# score = score +1 NO!
score += 1  # YES!
print(score)

print(f"Your score is {score}")
