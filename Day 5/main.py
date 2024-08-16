import random

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

student_scores = [
    51,
    137,
    38,
    71,
    56,
    15,
    27,
    12,
    114,
    82,
    94,
    144,
    67,
    40,
    58,
    123,
    94,
    92,
    139,
    71,
    21,
    62,
    51,
    132,
    105,
    149,
    66,
    39,
    54,
    58,
    104,
    2,
    119,
    77,
    75,
    129,
    53,
    49,
    53,
    22,
    31,
    131,
    88,
    142,
    6,
    125,
    30,
    45,
    99,
    85,
]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)
print(total_exam_score)

exam_max_score = max(student_scores)

max = student_scores[0]
for score in student_scores:
    if max < score:
        max = score

print(max)
print(exam_max_score)

sum = 0
for num in range(101):
    sum += num

print(sum)
