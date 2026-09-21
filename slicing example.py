#Print the first 3 characters of a string using slicing.

a = "pythonprogramming"
print(a[0:3])

#Print the last 3 characters of a string.

print(a[-3:])

#Print the string in reverse.
print(a[::-1])

#Print every second character of a string.

print(a[0:17:2])

#Print characters from index 2 to 6.
print(a[2:6])


#Print the string without its first and last character.
print(a[1:-1])

#Extract the middle characters of a string.
extracts = a[(len(a)) //2]
print(extracts)

#Reverse a string and check whether it is a palindrome.

if a == a[::-1]:
    print("is palindrome")
else:
        print("it not palindrome")

#Print characters at odd indexes.

print(a[1:17:2])

#Print characters at even indexes.

print(a[0:17:2])

#lists

#Print the first 3 elements of a list.

b = ["apple","orange","bannana","graphs","mango","junk","cooldrinks","tea"]

print(b[0:3])

#Print the last 3 elements of a list.
print(b[-3:])

#Print a list in reverse order.
print(b[::-1])

#Print every second element of a list.
print(b[0:10:2])

#Print elements from index 2 to 5.
print(b[2:5])

#Print the list without its first and last element.
print(b[1:-1])

#Extract the middle elements of a list.
extract = b[len(b) // 2]
print(extract)

# Print elements at even indexes.
print(a[0:10:2])

#Print elements at odd indexes.
print(a[1:10:2])

#Create a new list containing the last 5 elements using slicing.
new = [1,2,3,4,5,6,7,8,9,0]
print(new[-5:])


#Tuples

#Print the first 3 elements of a Tuples.

c = (1,2,3,4,5,6,7,8,9,0) 

print(c[0:3])

#Print the last 3 elements of a list.
print(c[-3:])

#Print a list in reverse order.
print(c[::-1])

#Print every second element of a list.
print(c[0:10:2])

#Print elements from index 2 to 5.
print(c[2:5])

#Print the list without its first and last element.
print(c[1:-1])

#Extract the middle elements of a list.
extract_c = c[len(c) // 2]
print(extract_c)

# Print elements at even indexes.
print(c[0:10:2])

#Print elements at odd indexes.
print(c[1:10:2])


'''text = "PythonProgramming"

Print:

First 6 characters

Last 5 characters

Reverse

Every second character

'''

text = "PythonProgramming"
print(text[0:6])
print(text[-5:])
print(text[::-1])
print(text[0:17:2])


'''
numbers = [10, 20, 30, 40, 50, 60, 70]

Print:

First 3 elements

Last 3 elements

Reverse

Elements from index 2 to 5'''


numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[0:3])
print(numbers[-3:])
print(numbers[::-1])
print(numbers[2:5])

'''t = ("Python", "Java", "C", "AWS", "CCNA")

Print:

First 2 elements

Last 2 elements

Reverse

Elements from index 1 to 3'''

t = ("Python", "Java", "C", "AWS", "CCNA")
print(t[0:2])
print(t[-2:])
print(t[::-1])
print(t[1:3])

