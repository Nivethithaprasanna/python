'''s=(10,20,30,40,50)
print(s)

numbers = {10, 20, 30, 40, 50}
numbers.add(60)
print(numbers)


numbers={10,20,30,40,50}
numbers.remove(10)
print(numbers)

s={10,20,30,40,50}
print(len(s))

numbers={10,20,30,40,50}
if 30 in numbers:
    print("30 exists")
else:
    print("30 does not")

numbers={10,20,30,40,50}
for number in numbers:
    print(number)

    
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)

numbers = {10, 20, 30, 40, 50}
print(sum(numbers))

#set
#union
a={10,20,30}
b={30,40,50}
print(a.union(b))

#intersection
a={10,20,30}
b={30,40,50}
print(a.intersection(b))

#diff
a={10,20,30}
b={30,40,50}
print(a.difference(b))

#symmetric
a={10,20,30}
b={30,40,50}
print(a.(b))

a = {10, 20}
b = {10, 20, 30, 40}

print(a.issubset(b))

a = {10, 20, 30}
b = {40, 50, 60}

print(a.isdisjoint(b))

#duplicates

numbers=[10,20,30,40,40,50]
result= set(numbers)
print(result)

group1 = {"Arun", "Bala", "Chitra"}
group2 = {"Chitra", "Deepa", "Arun"}
common = group1.intersection(group2)
print(common)

#Dictionary

student={
    "name":"nive",
    "age":25,
    "city":"salem"
    }
print(student["name"])


student = {
    "name": "Arun",
    "age": 20,
    "city": "Madurai"
}
student["course"] = "Python"
print(student)

student = {
    "name": "Arun",
    "age": 20,
    "city": "Madurai"
}
student["age"] = 21
print(student)


student = {
    "name": "Arun",
    "age": 20,
    "city": "Madurai"
}

del student["city"]
print(student)
'''


student = {
    "name": "Arun",
    "age": 20,
    "city": "Madurai"
}
print(len(student))

student = {
    "name": "Arun",
    "age": 20,
    "city": "Madurai"
}

print(student.keysstudent ={
    "name": "Arun",
    "age": 20,
    "city": "Madurai"
}
print(student.values())
