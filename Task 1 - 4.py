#Task --- 1
'''
# Arithmetic Operators
a=10
b=5
print ("addition : ", a + b)
print ("subtraction : ", a - b)
print ("mutiplication : ", a * b)
print ("floor division : ", a // b)
print (" modulus :", a % b)
print (" power :", a ** b)

num =int (input("Enter a number :"))
last_digit = num % 10
print("last_digit : " , last_digit)


a = int(input("Enter first number :"))
b =int(input("Enter second number :"))
if a > b:
    print("Greater :", a)
    print("smaller :", b)
else:
        print("Greater :", a)
        print("samller :", b)



age = int(input("enter a age : "))
id =input(" do you have valid id ")
if age >=18 and id == "yes" :
    print("eligible to vote")
else :
    print("not eligible")

a= int(input("enter first number :"))
b = int(input("enter second number :"))
if a > 100 or b > 100:
    print("At leastb one number is greater than 100")
else:
        print("both nuymbers are 100 or less")
        
username = input("enter username: ")
password = input("enter password: ")
if username == "admin" and password == "1234" :
    print("login successful")
else:
    print("invalid username or password ")


students = ["namkkal" , "ooty" , "salem"]
name = input("enter name: ")
if name in students:
    print("name exists")
else:
    print("name not found")
    
fruits = ["Apple" , "banana", "mango", "orange"]
print("apple" in fruits)
print("mango" in fruits)
    
      
text = "python"
ch = input("enter a character: ")
if ch in text:
    print("character is present")
else:
    print("character is not present")

a =[1, 2, 3]
b =[1, 2, 3]
print(a == b)
print(a is b)

a =[1, 2, 3]
b = a
print(a is b)

a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)

a = 5
print (~a)

a = 6
b = 3
print("and =" , a & b)
print("or =" ,a | b)

#Even or Odd
num = int(input("enter a number : "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

#Positive, Negative or Zero
num = int(input("enter a number : "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

#Voting Eligibility
age = int(input("enter your age: "))
if age >=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


#Biggest of Two Numbers
a = int(input("enter first number: "))
b =int(input("enter second number: "))
if a > b:
    print("first numerb is bigger")
elif b > a:
        print("second number is bigger")
else:
    print("both are equal")


#Pass or Fail
mark = int(input("enter a mark :"))
if mark >50:
    print("pass")
else:
    print("fail")

#Divisible by 5
num =int(input("enter a number:"))
if num % 5== 0:
    print("divisible by 5")
else:
    print("not divisible by 5")

#Last Digit
num = int(input("enter a number :"))
last = num % 10
print("last digit is even")
if last % 2== 0:
    print("last digit is odd")

#Simple Login
username = input("enter username :")
password = input("enter password :")
if username == "admin" and password == "1234" :
    print("login succesfully")
else:
    print("Login falied")

'''

#Task -- 2
##IF–ELSE Tasks
#Check whether a number is Even or Odd
num = int(input("enter a number :"))
if num % 2==0:
    print("even")
else:
    print("odd")

#Check whether a person is Eligible or Not Eligible to Vote
a = int(input("enter a age: "))
if a >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote ")

#Check whether a number is Positive or Negative
age =int(input("enter a number"))
if age >= 18 :
    print("positive")
else:
    print("negative")

#Check whether a student has Passed or Failed based on a mark
a = int(input("enter a number"))
if a >= 50:
    print("passed")
else:
    print("falied")

#Check whether a given number is Divisible by 5 or Not.
a =int(input("enter a number"))
if a % 5==0:
    print("yes")
else:
    print("not")

##ELIF Tasks
# Display the grade based on the student's mark.
mark = int(input("enter a mark"))
if mark > 90:
    print("grade a")
elif mark > 80:
        print("grade b")
elif mark > 70:
    print("grade c")
         
else:
    print("grade ")

#Find the largest of three numbers.
num =int(input("enter a largest three number"))
if num ==  69:
     print("largest first number")
elif num == 55:
     print("second largest number ")
elif num == 50:
     print("third largest number")
else:
     print("lowest number") 

#Create a simple calculator using `+`, `-`, `*`, `/`.

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


     
#Display the day of the week based on a number (1–7).
day = int(input("enter a number (1-7):"))
if  day == 1:
    print("sunday")
elif day == 2:
    print("monday")
elif day == 3:
    print("tuesday")
elif day == 4:
    print("wednesday")
elif day == 5:
    print("thursday")
elif day == 6:
    print("friday")
elif day == 7:
    print("saturday")
else:
    print("no week")
                    
#Display the electricity bill category based on units consumed.
units =int(input("enter a units cousumed"))
if units <= 100:
    print("low useage")
elif units <= 200:
    print("medium useage")
elif units <= 300:
    print("high useage")
else:
    print("very high useage")

## NESTED IF–ELSE Tasks
#Check age and driving licence eligibility.

age = int(input("enter a age "))
if age>= 18:
    print("eligible to drive a bike")
elif age>= 20:
    print("eligible to drive a car")
else:
    print("not eligible")
    
#Check username and password for login.
username = input("enter username: ")
password = input("enter a password: ")
if username == "joy" and password == "12345":
    print("login successful")
else:
    print("worng username or password ")

# Check budget and laptop brand before purchasing.
budget = int(input("enter your budget: "))
brand = input("enter laptop brand: ")
if budget >= 50000 and brand == "hp":
    print("you bye a laptop")
else:
    print("you can not bye laptop")

#Check whether a student is eligible for an exam based on attendance, and then check the mark.
    
attendance = int(input("enter attendance :"))
if attendance >= 75:
    mark = int(input("enter mark :"))
if mark >= 50:
    print("eligible and passed")
else:
    print("eligible but falied")


#Check ATM withdrawal
pin= 1234
balance = 30000
enter_pin =int(input("enter pin: "))
if enter_pin == pin:
    amount = int(input("enter withdrawal amount: "))
    if amount >= balance:
        print("withdrawal successful")
else:
    print("worng pin ")

                 
pin= 1234
balance = 30000
enter_pin =int(input("enter pin: "))
if enter_pin == pin:
    amount = int(input("enter withdrawal amount: "))
    if amount >= balance:
        print("withdrawal successful")
        print("remaining balance:")
else:
    print("worng pin ")

    
### Challenge Task
#Create a Movie Ticket Booking Program
num = int(input("Enter number of tickets: "))
if num <= 120:
    print("Available")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Allowed")
        movie = input("Enter movie name: ")
        if movie == "spiderman":
            print("Spiderman")
        else:
            print("Movie not available")
    else:
        print("Not allowed")
else:
    print("Movie not available")




#Task --- 3

#Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


#Print all even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)


#Print all odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)


#Multiplication table of 5
for i in range(1, 11):
    print(5, "x", i, "=", 5 * i)


#Sum of numbers from 1 to 10
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum =", sum)


#Print each character in "PYTHON"
text = "PYTHON"
for i in text:
    print(i)


#Count vowels in "programming"
text = "programming"
count = 0
for i in text:
    if i in "aeiou":
        count = count + 1
print("Vowels =", count)


#Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)


#Factorial of 5
fact = 1
for i in range(1, 6):
    fact = fact * i
print("Factorial =", fact)


#Pattern
for i in range(1, 6):
    print("*" * i)


#Count vowels in your name
name = input("Enter your name: ")
count = 0
for i in name.lower():
    if i in "aeiou":
        count = count + 1
print("Vowels =", count)i = 1


#while loop
while i <= 10:
    print(i)
    i = i + 1


#Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i = i - 1


#Print all even numbers from 1 to 20
i = 2
while i <= 20:
    print(i)
    i = i + 2


#Sum of numbers from 1 to 10
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i = i + 1
print("Sum =", sum)


#Multiplication table of 7
i = 1
while i <= 10:
    print(7, "x", i, "=", 7 * i)
    i = i + 1


#Factorial of 5
i = 1
fact = 1
while i <= 5:
    fact = fact * i
    i = i + 1
print("Factorial =", fact)


#Count the digits in a number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Number of digits =", count)


#Reverse a number
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)


#Task -- 4


#STRING
#lower and upper
a="sakthivel"
print(a.upper())
b="RAINA"
print(b.lower())

#swapcase
a="SakthiVeL"
print(a.swapcase())
b="CRICKET"
print(b.swapcase())

#capitalize
a="sakthivel"
print(a.capitalize())

#startwith
a="Sakthivel"
print(a.startswith('S')) 
print(a.startswith('s'))

#endswith
b="SAKTHIVEL"
print(b.endswith('RA'))
print(b.endswith('rc'))

#replace
c="python"
print(c.replace('py','ja'))

#strip
a="     sakthi     "
print(a.strip())

#split
a="we play cricket"
print(a.split())


#format
a="sakthivel"
b="20"
c="namakkal"
print(f"my name is {a}")
print(f"iam{b}years old")
print(f"i live in{c}")

#center
c="python"
print(c.center(20))

#ljust
a="java"
print(a.ljust(20))

#rjust
b="cricket"
print(b.rjust(20))

#zfill
c="hii"
print(c.zfill(6))

#isdigit
a="sakthivel1234"
print(a.isdigit())

#isalpha
b="python"
print(b.isalpha())

#isascii
c="sakthivellll111234"
print(c.isascii())

#combainedtask
#remove extra spaces
a=input("enter username:")
print(a.strip())

#capitalize
a=input("enter name:")
print(a.sumithra())

#ascii
a=input("Enter filename ")
print(a.isascii())
print(a.isalpha())
print(a.isdigit())

#check contains only digits
a=input("Enter number")
print(a.isdigit())

#add zeros using zfill
a=input("Enter number")
print(a.zfill(15))

#convert it into uppercase
a=input("Enter name")
print(a.upper())

#replace the space with
text=input("Enter value:")
print(text.replace("  ","-"))

#split it into a words
a=input("Enter a value:")
print(a.split())

#print each word separately
b=input("Enter value:")
print(b.split())

#for else tasks
for i in range(1,6):
    print(i)
else:
    print("loop completed")
#print even numbers
for i in range(1,11):
  if i%2==0:
    print(i)
else:
    print("not okay")

#print each word in python
for char in "python":
   print(char)
else:
    print("loop completed")

#search for 5
for i in(1,2,3,4,5,6):
  if i==5:
    print("5 found")
    break
else:
    print("break")

#search for 10
for i in(2,4,6,8):
  if i==10:
    print(i)
    break
else:
    print("loop completed")

# search for the letter
for i in("apple"):
    if i=="a":
        print(i)
        break
else:
    print("loop completed")

