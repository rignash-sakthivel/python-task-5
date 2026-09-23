'''#Create a set of 5 numbers and print it.

a = {1,2,3,4,20}
print(a)

#Add 60 to a set.
a.add(60)
print(a)

#Remove 20 from a set.
a.remove(20)
print(a)

#Find the length of a set.
print(len(a))

#Check whether 30 exists in a set.
if a == 30:
    print("30 in the set")
else:
    print("30 not in the list")
    
#Print all elements using a for loop.

for i in a:
    print(i)

#Create a set containing duplicate values and observe the output.
b = {1,2,3,4,55,4,3,6}
print(b)

#Find the maximum value in a set.
print(max(a))

#Find the minimum value in a set.
print(min(a))

#Find the sum of all elements in a set.
c = 0
for i in a:
    c += i
    print(c)


#Find the union of two sets.

a1 = {1,2,3,4,5}
a2 = {4,5,6,7,8}

print(a1.union(a2))

#Find the intersection of two sets.
print(a1.intersection(a2))

#Find the difference between two sets.
print(a1.difference(a2))

#Find the symmetric difference.
print(a1.symmetric_difference(a2))

#Check whether one set is a subset of another.
print(a1.issubset(a2))

#Check whether two sets are disjoint.
print(a1.isdisjoint(a2))

#Convert a list into a set to remove duplicates.
lists = [1,2,3,45,67,89]
sets = set(lists)
print(sets)

#Find common elements between two student groups.
elements1 = {'abc','def','ghi','jkl','mno'}
elements2 = {'jkl','mno','pqr','stu','vwx'}
print(elements1.intersection(elements2))

#Create a dictionary containing name, age and city.
a = {"Name":"Sakthivel","Age":"22","City":"Namakkal"}
print(a)

#Print the value of "name".
print(a.get("Name"))

#Add a new key "course".
a.update({"Course":"AI&ML"})
print(a)

#Change the value of "age".
a.update({"Age":"22" , "Age":"23"})
print(a)

#Delete the "city" key.
a.pop("City", None)
print(a)

#Find the number of items in a dictionary.
print(len(a))

#Check whether "name" exists.

if "Name" in a:
    print("True")
else:
    print("False")


#Print all keys.
print(a.keys())

#Print all values.
print(a.values())

#Print both keys and values using a for loop
for key,value in a.items():
    print(key, value)'''

#Create a dictionary containing 5 students and their marks.
students = {"sakthivel":300,"prabha":300,"sri":350,"dheepa":400,"karan":250}
print(students)

#Find the student with the highest mark.
students_mark = max(students, key=students.get)
print(students_mark)

#Find the student with the lowest mark.
students_mark = min(students, key=students.get)
print(students_mark)

#Calculate the total of all marks.

total = 0
for i in students.values():
    total += i
print(total)

#Calculate the average mark.

avg = total/len(students)
print(avg)

#Count how many students scored above 50.
count = 0
for h in students.values():
    if i > 50:
        count += 1
print(count)

#Search for a student by name.

name = input("Enter the name : ")
if name in students:
    print("Marks : ",students[name])
else:
    print("student not found")

#Update a student's mark.

new_mark = int(input("Enter new mark: "))
students[name] = new_mark
print(students)












