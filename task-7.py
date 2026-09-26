# User-Defined Functions
#Create a function to print "Hello Python".
'''
def hello():
    print("Hello Python")
hello()

# Create a function to print your name.
def name():
    print("Sakthivel M")
name()

#Create a function to add two numbers.
def add(a,b):
    print("adding : ",a+b)
add(56,89)

#Create a function to subtract two numbers.
def sub(c,d):
    print("subraction : ",c-d)
sub(89,67)

#Create a function to find the square of a number.
def square(e):
    h = e * e
    print(h)
square(4)

#Create a function to check whether a number is even or odd.
def check(evenodd):
    if evenodd % 2 == 0:
        print("even")
    else :
        print("odd")
check(4)
    
#Create a function to find the largest of two numbers.
def large(one,two):
    if one >  two:
        print("A is grater then B")
    else:
        print("B is grater then A")
large(34,67)

#Create a function to calculate the area of a rectangle.
def area(lenght,width):
    areas = lenght*width
    print("Area = ",areas)
area(34,78)

#Create a function to greet a person using their name.
def greet(name):
    print(f"Hello {name} Good Moring!")
greet("SakthivelMurugesan")

#Create a function to find the sum of three numbers.
def sum(no1,no2,no3,):
    print("Sum of three numbers : ",no1+no2+no3)
sum(34,56,78)


#Pre-Defined Functions
#Find the length of "Python"

def lenght(lenghts):
    print(len(lenghts))
lenght("python")

#Find the largest number in [10, 20, 30, 40].

def largest(a,b,c,d):
    print(max(a,b,c,d))
largest(10, 20, 30, 40)

# Find the smallest number in [15, 5, 25, 10].

def smallest(e,g,h):
    print(min(e,g,h))
smallest(10, 20, 30)

#Sort [40, 10, 30, 20].
def sortlist(i,j,k,l):
    numbers = [i,j,k,l]
    numbers.sort()
    print(numbers)
sortlist(40, 10, 30, 20)


#Find the absolute value of -50.

def absolute(value):
    print(abs(value))
absolute(-59)

#Find the type of 100.

def types(numbers):
    print(type(numbers))
types(100)

#Convert "25" into an integer.

def convert(integer):
    text = int(integer)
    print(text)
    print(type(text))
convert("25")


#Convert 100 into a string.
def convert2(integer):
    text2 = str(integer)
    print(text2)
    print(type(text2))
convert2(100)

#Find the length of a list.
def lenght(no1,no2,no3,no4):
    numbers = [no1,no2,no3,no4]
    print(len(numbers))
lenght(2,4,5,6)


#Lambda

# Create a lambda function to find the square of a number.

n = lambda x : x*x
print(n(4))

#Create a lambda function to find the cube.

cube = lambda y : y*y*y
print(cube(4))

#Create a lambda function to add two numbers.
add = lambda a,b : a+b
print(add(23,67))

#Create a lambda function to multiply two numbers.

multi = lambda e,d : e*d
print(multi(80,80))

# Create a lambda function to check whether a number is even.

check = lambda one : "odd" if one % 2 == 0 else "even"
print(check(45))


#Create a lambda function to subtract two numbers.
sub = lambda f,g : f-g
print(sub(89,45))

#Create a lambda function to find double of a number.

double = lambda x: x * 2
print(double(5))
print(double(12))

#Create a lambda function to find half of a number.
half = lambda no : no /2
print(half(50))

#Create a lambda function to find the length of a word.
lenghts = lambda nos : len(nos)
print(lenghts("sakthivel"))

#Create a lambda function to find the largest of two numbers.
large = lambda v,w : v if v > w else w
print(large(23,56))



# map()

# Double every number in [1, 2, 3, 4, 5].
a = [1, 2, 3, 4, 5]
double = list(map(lambda x : x * 2,a))
print(double)

#Find the square of [1, 2, 3, 4, 5].
b = [1, 2, 3, 4, 5]
square = list(map(lambda y : y * y , b))
print(square)

#Add 10 to every number in [5, 10, 15, 20].
c = [5, 10, 15, 20]
add = list(map(lambda z : z + 10,c))
print(add)

#Multiply every number by 5.
multi = list(map(lambda e : e * 10,c))
print(multi)

#Convert ["python", "java", "aws"] to uppercase.
t = ["python", "java", "aws"]
uppercase = list(map(lambda rt : rt.upper(),t))
print(uppercase)

#Find the length of each word in ["cat", "apple", "python"].
f =["cat", "apple", "python"]
lenght = list(map(lambda ty : len(ty),f ))
print(lenght)

#Find the cube of [1, 2, 3, 4]
k = [1, 2, 3, 4]
cube = list(map(lambda gh : gh * gh * gh ,k))
print(cube)


#Subtract 5 from every number.
sub = list(map(lambda gh : gh - 5 ,k))
print(sub)

#Double the marks [40, 50, 60, 70].
n = [40, 50, 60, 70]
double = list(map(lambda bf : bf * 2,n))
print(double)

# Convert every name to uppercase.
o =  ["sakthivel", "murugesan", "selvambal"]
uppercases = list(map(lambda tu : tu.upper(),o))
print(uppercases)
'''
#filter()

#Find even numbers from [1, 2, 3, 4, 5, 6].
r = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda rt : rt % 2 == 0,r ))
print(even)

#Find odd numbers.
odd = list(filter(lambda tr : tr % 2 == 1,r ))
print(odd)

#Find numbers greater than 10.
l = [71, 2, 13, 24, 15, 16]
find = list(filter(lambda fd : fd > 10 ,l))
print(find)

#Find numbers less than 20.
finds = list(filter(lambda uv : uv < 20,l))
print(finds)

#Find numbers divisible by 5.
finds0 = list(filter(lambda po : po % 5 == 0 ,l))
print(finds0)

#Find positive numbers.
ll = [71, 2, 13, -24, -15, 16]
find00 = list(filter(lambda fd : fd > 0 ,ll))
print(find00)

#Find negative numbers.
find000 = list(filter(lambda df : df < 0 ,ll))
print(find000)

#Find marks greater than 50.
find2 = list(filter(lambda df : df > 50 ,ll))
print(find2)

#Find names starting with "A".
ff =["cat", "apple", "python"]
lenght = list(filter(lambda ty : ty.startswith ("a"),ff ))
print(lenght)

#Find words with more than 5 characters.
lenghts = list(filter(lambda jh :len(jh) > 5,ff))
print(lenghts)








