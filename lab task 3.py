# ================= FOR LOOP =================

'''# 1. Print 1 to 10
for i in range(1, 11):
    print(i)'''

# 2. Even numbers 1 to 20
for i in range(2, 21, 2):
    print(i)

'''# 3. Odd numbers 1 to 20
for i in range(1, 21, 2):
    print(i)

# 4. Multiplication table of 5
for i in range(1, 11):
    print(5 * i)

# 5. Sum 1 to 10
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

# 6. Each character in PYTHON
a = "PYTHON"
for i in a:
    print(i)

# 7. Count vowels in programming
a = "programming"
count = 0
for i in a:
    if i in "aeiou":
        count = count + 1
print(count)

# 8. Print 10 to 1
for i in range(10, 0, -1):
    print(i)

# 9. Factorial of 5
fact = 1
for i in range(1, 6):
    fact = fact * i
print(fact)

# 10. Pattern
for i in range(1, 6):
    print("*" * i)

# 11. Count vowels in name
name = input("Enter your name: ")
count = 0
for i in name:
    if i.lower() in "aeiou":
        count = count + 1
print("Vowels:", count)


# ================= WHILE LOOP =================

# 1. Print 1 to 10
i = 1
while i <= 10:
    print(i)
    i = i + 1

# 2. Print 10 to 1
i = 10
while i >= 1:
    print(i)
    i = i - 1

# 3. Even numbers 1 to 20
i = 2
while i <= 20:
    print(i)
    i = i + 2

# 4. Sum 1 to 10
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)

# 5. Multiplication table of 7
i = 1
while i <= 10:
    print(7 * i)
    i = i + 1

# 6. Factorial of 5
i = 1
fact = 1
while i <= 5:
    fact = fact * i
    i = i + 1
print(fact)

# 7. Count digits
n = int(input("Enter number: "))
count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Digits:", count)

# 8. Reverse a number
n = int(input("Enter number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse:", reverse)'''
