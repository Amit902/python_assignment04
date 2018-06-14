# Q.1- Write a program to create a tuple with different data types and do the following operations. 

t = [1,2,3,4,5,6]
print(t)
print(len(t))
print(max(t))
print(min(t))
print("\n")


t = ["amit", "lalit" ,"nisha", "aachal"]
print(t)
print(len(t))
print(max(t))
print(min(t))
print("\n")


# Q.2-Find largest and smallest elements of a tuples. 

t = [0,1,2,5,4,6,3,7,8,9,10,12,14,15,13,16]
print(t)
print("\n")
print("the  smallest element is",min(t))
print("\n")



# Q.3- Write a program to find the product of all elements of a tuple. 

t = [1,2,3,4,5,6]
p = t[0]*t[1]*t[3]*t[4]*t[5]
print("the product of all the element is",p)
print("\n")	 
  
  
#Q.4- Create two set using user defined values. 

#Calculate difference between two sets.
#Print the result of intersection of two sets.

l1 = [0,0,0,0,0,0]
l1[0] = int(input("Enter a number: "))
l1[1] = int(input("Enter another number: "))
l1[2] = int(input("Enter another number: "))
l1[3] = int(input("Enter another number: "))
l1[4] = int(input("Enter another number: "))
l1[5] = int(input("Enter another number: "))
print("\n")

 
l2 = [0,0,0,0,0,0]
l2[0] = int(input("Enter a number: "))
l2[1] = int(input("Enter another number: "))
l2[2] = int(input("Enter another number: "))
l2[3] = int(input("Enter another number: "))
l2[4] = int(input("Enter another number: "))
l2[5] = int(input("Enter another number: "))
print("\n")

s1 = set(l1)
s2 = set(l2) 
print(s1)
print(s2)
print(s1-s2)
print(s1&s2)
print("\n")

# Q.5- Create a dictionary to store name and marks of 10 students by user input.

d = {}
name = input("enter name: ")
marks = int(input("ente marks: "))
d[name] = marks
 
name = input("enter name: ")
marks = int(input("ente marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter  marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter  marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter  marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter  marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter  marks: "))
d[name] = marks

name = input("enter name: ")
marks = int(input("enter  marks: "))
d[name] = marks

print(d)
print("\n")

 
#Q.6-Sort the dictionary created in previous question according to marks.

d = {}
name =""
marks =""
l = []
for x in range(3):
	name= input("enter the name of student: ")
	marks = int(input("enter  the student marks: "))
	l.append(marks)
	d[name] = marks
print(d)
l.sort()
print(l)
print("\n")
	 


#Q.7- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.

l = ["M","I","S","S","I","S","S","I","P","P","I"]
a = l.count('M')
b = l.count('I')
c = l.count('S')
e = l.count('P')
d = {}
d["m"] = a
d["i"] = b
d["s"] = c
d["p"] = e
print(d)