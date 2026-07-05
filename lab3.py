fruits = ["apple", "banana", "cherry", "mango"]
print("Problem 1: Looping over a sequence")
for x in fruits:
    print(x)
print()


print("Problem 2: Countdown")
n = int(input("Enter a number: "))
while n >= 0:
    print(n)
    n -= 1
print()


print("Problem 3: Exponentiation")
base = 2
power = 5
result = 1
i = 0
while i < power:
    result = result * base
    i += 1
print(base, "^", power, "=", result)
print()


print("Problem 4: Sum of primes below 1000")
total = 0
for num in range(2, 1000):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        total += num
print("Sum of all primes below 1000:", total)
print()


print("Problem 5: Fibonacci numbers")
N = int(input("Enter N: "))
a, b = 0, 1
while a < N:
    print(a, end=" ")
    a, b = b, a + b
print()