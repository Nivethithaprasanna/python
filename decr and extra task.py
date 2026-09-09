'''# Decrement
for i in range(5, 0, -1):
    print(i)

for i in range(5, 0, -2):
    print(i)


# Increment and Decrement
for i in range(5, 0, -1):
    print(i)

for i in range(1, 5):
    print(i)


# Factorial
n = int(input("Enter the value: "))
f = 1

for i in range(1, n + 1):
    f *= i

print("Factorial:", f)


# Alphabets
for i in range(65, 70):
    print(chr(i))


# String
a = "Gowsik"

for i in a:
    print(i)


# Sum of values
n = int(input("Enter the value: "))
add = 0

for i in range(1, n + 1):
    add += i

print("Total:", add)


# Counting the numbers which are divisible by 3
count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count += 1
        print(i)

print("Total:", count)'''


# Small letter to capital
text = "joy"
result = ""

for ch in text:
    result = result + chr(ord(ch) - 32)

print(result)


'''# Count the vowel
text = str(input("Enter a: "))
count = 0

for i in text:
    if i in "AEIOUaeiou":
        count += 1

print(count)'''
