'''#odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#eleigible or not

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

#
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")

#
mark = int(input("Enter your mark: "))

if mark >= 35:
    print("Passed")
else:
    print("Failed")
    
#
 num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
    
#
mark = int(input("Enter your mark: "))

if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C")
elif mark >= 60:
    print("Grade D")
elif mark >= 35:
    print("Grade E")
else:
    print("Fail")

#
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

#
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    print("Result =", a + b)
elif operator == "-":
    print("Result =", a - b)
elif operator == "*":
    print("Result =", a * b)
elif operator == "/":
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")


#
units = int(input("Enter units consumed: "))

if units <= 100:
    print("Category: Low Consumption")
elif units <= 200:
    print("Category: Medium Consumption")
elif units <= 500:
    print("Category: High Consumption")
else:
    print("Category: Very High Consumption")

    
#
 age = int(input("Enter your age: "))

if age >= 18:
    licence = input("Do you have a driving licence? (yes/no): ")

    if licence == "yes":
        print("Eligible to Drive")
    else:
        print("Not Eligible: Licence Required")
else:
    print("Not Eligible: Age must be 18 or above")


#
username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")

    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")


#Budget and Laptop Brand
    budget = float(input("Enter your budget: "))

if budget >= 50000:
    brand = input("Enter laptop brand: ")

    if brand.lower() == "dell":
        print("You can purchase a Dell laptop")
    else:
        print("Brand not available")
else:
    print("Budget is not sufficient")


#Exam Eligibility and Mark
    attendance = float(input("Enter attendance percentage: "))

if attendance >= 75:
    mark = int(input("Enter your mark: "))

    if mark >= 35:
        print("Eligible for Exam and Passed")
    else:
        print("Eligible for Exam but Failed")
else:
    print("Not Eligible for Exam due to low attendance")'''

#ATM WITHDRAWAL
correct_pin = 1234
balance = 10000

pin = int(input("Enter PIN: "))

if pin == correct_pin:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        print("Withdrawal Successful")
        print("Remaining Balance =", balance - amount)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")


#BOOKING TICKECT

age = int(input("Enter your age: "))

if age >= 18:
    print("Age eligible for booking")

    movie_type = input("Enter movie type (Regular/3D/IMAX): ")
    tickets = int(input("Enter number of tickets: "))

    if movie_type.lower() == "regular":
        price = 150
    elif movie_type.lower() == "3d":
        price = 250
    elif movie_type.lower() == "imax":
        price = 350
    else:
        price = 0
        print("Invalid movie type")

    if price > 0:
        total = price * tickets
        print("Ticket Price =", price)
        print("Number of Tickets =", tickets)
        print("Total Amount =", total)
        print("Booking Successful")

else:
    print("Not eligible for booking. You must be 18 or above.")



    


    




    






    




