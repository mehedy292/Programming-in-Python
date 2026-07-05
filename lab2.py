import math


a = 5
b = 10
print("Before swap: a =", a, " b =", b)
temp = a
a = b
b = temp
print("After swap: a =", a, " b =", b)
print()


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance between the points:", distance)
print()


num = 7
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
print()


ch = input("Enter a character: ")
ch = ch.lower()
if ch in "aeiou":
    print(ch, "is a vowel")
else:
    print(ch, "is not a vowel")
print()


marks = 78

if marks >= 80:
    grade = "A"
elif marks >= 75:
    grade = "A-"
elif marks >= 70:
    grade = "B+"
elif marks >= 65:
    grade = "B"
elif marks >= 60:
    grade = "B-"
elif marks >= 55:
    grade = "C+"
elif marks >= 50:
    grade = "C"
elif marks >= 45:
    grade = "D"
else:
    grade = "F"

print("Marks:", marks, " Grade:", grade)