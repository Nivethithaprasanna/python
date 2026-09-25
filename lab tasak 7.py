def hello():
    print("Hello Python")

hello()

def name():
    print("Nive")

name()

def add(a, b):
    print(a + b)

add(10, 20)

def subtract(a, b):
    print(a - b)

subtract(20, 10)

def square(n):
    print(n * n)

square(5)


def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)


def largest(a, b):
    if a > b:
        print(a)
    else:
        print(b)

largest(25, 40)

def area(length, width):
    print(length * width)

area(10, 5)

def greet(name):
    print("Hello", name)

greet("Nive")

def add_three(a, b, c):
    print(a + b + c)

add_three(10, 20, 30)

#pre defined
print(len("Python"))



print(max([10, 20, 30, 40]))

print(min([15, 5, 25, 10]))


print(sum([10, 20, 30]))


print(sorted([40, 10, 30, 20]))

print(abs(-50))

print(type(100))

numbers = [10, 20, 30, 40, 50]

print(len(numbers))

#lambda func
cube = lambda n: n * n * n

print(cube(3))


add = lambda a, b: a + b

print(add(10, 20))


