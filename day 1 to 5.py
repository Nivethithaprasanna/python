# Basic Print
print("Hii")
print("Welcome")
print("Hello")
print("Gopika")


# Integer - int
a = 1
print(a)
print(type(a))

a = float(input("Enter a: "))
b = int(input("Enter b: "))
print(a + b)
print(a)


# Arithmetic Operators
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Add:", a + b)
print("Sub:", a - b)
print("Mul:", a * b)
print("Div:", a / b)
print("FD:", a // b)
print("Expo:", a ** b)
print("Modules:", a % b)


# Comparison Operators
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# Logical Operators
# and --> Both conditions should be true
a = int(input("Enter the value: "))

print(a == 10 and a < 20)
print(a != 10 and a < 20)


# or --> Either one condition should be true
b = int(input("Enter b: "))

print(b != 20 or b <= 20)


# not
c = int(input("Enter c: "))

print(not(c < 10))
print(not(c == 30))


# Assignment Operators
a = 5
b = 4

a += 3
a -= 2
a *= 4
a /= 2

print(a)
print(b)


# Bitwise Operators
a = 4
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(~b)


# If-Else
a = int(input("Enter AGE: "))

if a >= 18:
    print("Vote")
else:
    print("Cant vote")


# Last digit of the number
a = 123
b = a % 10
print(b)


# Remove the last digit
a = 123
b = a // 10
print(b)


# Even or Odd
a = int(input("Enter a: "))

if a % 2 != 0:
    print("Odd")
else:
    print("Even")


# Check Username and Password
u = str(input("Enter username: "))
p = int(input("Enter pass: "))

if u == "Livewire" and p == 123098:
    print("Login")
else:
    print("Unsuccessful")


# Check Divisible by 3 and 5
a = int(input("Enter a: "))

if a % 3 == 0 and a % 5 == 0:
    print("Login")
else:
    print("Unsuccessful")


# Positive / Negative / Zero
a = int(input("Enter a: "))

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")


# HackerRank - Weird
n = int(input("Enter a: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# Traffic Light
a = str(input("Enter the color: "))

if a == "red":
    print("Stop")
elif a == "yellow":
    print("Get ready")
elif a == "green":
    print("Go")
else:
    print("No color")


# String Operations
a = "Hii"
b = "Hello"

print(a * 3)
print(a + b)
print("Python" + a)


# Nested If-Else
f = str(input("Enter food: "))
p = int(input("Enter price: "))
s = str(input("Enter spice: "))

if f == "Biriyani":
    print("Woww")

    if p <= 150:
        print("Enjoy!!")

        if s == "Loww":
            print("Low")
        elif s == "Medium":
            print("Medium")
        else:
            print("Highh")

    else:
        print("Okk!")

else:
    print("Sadddd")


# FOR LOOP
# Increment
for i in range(1, 5, 1):
    print(i)


# Step value 2
for i in range(1, 5, 2):
    print(i)


# No step value
for i in range(1, 5):
    print(i)


# Only stopping value
for i in range(5):
    print(i)


# Tables
a = int(input("Enter number: "))

for i in range(1, 6):
    print(i, "x", a, "=", a * i)


# Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
