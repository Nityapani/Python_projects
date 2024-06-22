a="Nityaprakqshpanigrahi"
print(a[-8:])
#############
# Exercise Cats Everywhere

# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
catt = Cat('cat1', 5)
cattt = Cat('Cat2', 7)
catttt = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(catt.age, cattt.age, catttt.age)} years old.')
a=0
a=a+1
'''
In below example, we can see that when the ‘add_number’ function is called, it returns the sum of ‘a’ and ‘b’, 
which is stored in the result variable. Then using the print statement, the result is printed on the console.
'''
def add_numbers(a, b):
    return a + b
result = add_numbers(7, 9)
print(result)

print('hello  '+str(5))
# Write a Python program to calculate the length of a string.
def length(str1):
    count=0
    for i in str1:
        count+=1
    return count
print(length('w3resource.com'))

# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
def string(str1):
    if len(str1)<2:
        return '\'\''
    else:
        return str1[:2]+str1[-2:]
print(string('u'))
print(string('Nityaprakash'))
print(string('py'))
# Write a Python program to sum all the items in a list.
def sum_list(list1):
    addition=0
    for i in list1:
        addition+=i
    return addition
print(sum_list([1,2,3,4,5]))
#Write a Python program to get the largest number from a list.

def max_value(values):
    max=values[0]
    for i in values:
        if i>max:
            max=i
    return max
print(max_value([8,1,2,3,4,6,8]))
print(max_value([8,1,2,3,4,6,9]))
print(max_value([5,1,2,3,15,6,8]))
# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

def match_words(words):
    ctr=0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            ctr += 1
    return ctr
print(match_words(['abc', 'xyz', 'aba', '1221',"ctc",'bb']))

# Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4={}
for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)
# Write a Python program to iterate over dictionaries using for loops.
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for i,j in d.items():
    print(i,"corrensponds to", j)

# Write a  Python program to sum all the items in a dictionary.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result=sum(my_dict.values())
print(result)
#Write a python program to get all the even numbers from a list using list comprehension.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list=[x for x in numbers if x % 2 == 0]
print(new_list)
#lambda function
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2,numbers)
filtered_numbers = filter(lambda x: x % 2 == 0,numbers)
print("Squared numbers:", list(squared_numbers))
print("Filtered numbers:", list(filtered_numbers))
#for loop example
for i in "My name is Nityaprakash":
    print(i)
print(i)

#write a python program to remove duplicates from the list.
dupicate_list=[1,1,2,3,4,5,5,6,6,7,7,8,8,8]
unique_list=[]
for i in dupicate_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
#Work with dictionary
user={'name':'Nitya',
      'age':30,
}
for item in user.items():
    print(item)
for k,v in user.items():
    print(k,v)
for item in user.values():
    print(item)
for item in user.keys():
    print(item)
#Range:
for i in range(10,0,-1):
    print(list(range(10)))
for i,char in enumerate ("Hello"):
    print(i,char)
for i,char in enumerate(list(range(100))):
    if char==50:
        print(f'The index of 50 is : {i}')
# while loop
i=0
while i <20:
    print(i)
    i=i+1
#String slicing
my_name="Nityaprakash panigrahi"
exp=my_name[-9:]+" "+my_name[:12]
print(exp)
#get the duplicate values from a dictionary
dict={'name':'bangalore','age':30,'location':'bangalore','good_name':30}
list=[]
for i in dict.values():
    list.append(i)
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
    else:
        print(i)
#image processing
picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for image in picture:
    # print(image)
    for pixel in image:
        if pixel==1:
            print("*",end='')
        else:
            print(' ',end='')
    print('')
#Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1 and 56 (both included).
for i in range (1,57):
    if i%5==0 and i%7==0:
        print(i)
# Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(1):
    for j in range(i):
        print("* ",end="")
    print("")
for i in range(5,0,-1):
    for j in range(i):
        print("* ",end="")
    print("")

#Print the minimum value of a list
list=[0,-5,12,-9,25,-8,26]
min_value=list[0]
for num in list[i:]:
    if min_value > num :
       min_value = num
print(f'The minimum value of the list is {min_value}')
#Sort any given list.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2):
        print('i = ' + str(i))
        for j in range(0, n-i-1):
            print('j = ' + str(j))
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
my_list = [26, 25, 12, 20,-5, -8, 0]

# Sort the list
bubble_sort(my_list)

# Print the sorted list
print("Sorted list:", my_list)

# n=5
# for i in range(n):
#     print('i = '+str(i))
#     for j in range(0, n - i - 1):
#         print('j = '+str(j)
print(round(4.56))
# a=input()
# b=input()
a=10
b=12
if a>b:
    print("a is bigger")
elif a<b:
    print("b is bigger")
else:
    print("both are equal")
#Continue and break:-
n=10
i=1
while True:
    print("Nitya")
    if i%9 !=0:
        print("Inside if")
        i+=1
        continue
    print("Something")
    print("Something else")
    break
print("Done!")
#For loop
l=[]
for i in range (10):
    print(i+1,end=" ")
    l.append(i**2)
print('\n', l, sep='')
#While else loop example
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("Loop is finished")
    
#For Else loop:
s={"apple",4.9,"cherry"}
i=1
for x in s:
    print(x)
    i+=1
    print(i)
    if i ==3:
        break
    else:
        pass
else:
    print("Loop terminates with success")
print("outside loop")
#For Loop Dictionary:
Dict={"a":10,"b":20,20:25}
for items in Dict:
    print(items,Dict[items])
#Find the minimum value of a list:
my_list = [26, 25, 12, 20,-5, -8, 0]
m=my_list[0]
c=0
idx=0
for i in my_list:
    if i<m:
        m=i
        idx=c
    c+=1
print(m,idx)

#Functions
def printSuccess():
    print("I am done")
    print("send me another task")
printSuccess()
#Need to print character with the count
s = 'aaabbbbcca'
#output = a3b4c2a1
s = 'aaabbbbcca'
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1
result += s[-1] + str(count)
print(result)
#Write a python program to remove duplicats from a list.
list=[1,1,2,2,3,3,4,4,5,5,6,7,7]
l=[]
for i in list:
    if i not in l:
        l.append(i)
print(l)
#Get the unique values from a dictionary.
dict={'name':"nitya",'age':30,'city':"Bangalore",'officeLocation':"Bangalore",'place':"Bangalore",'my_age':30}
list1=[]
list2=[]
list3=[]
for items in dict.values():
    list1.append(items)
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print(i)
#sum the values of a list
my_list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in my_list:
    sum+=i
print(sum)
############################
#Functions with return
def pow(a,b):
    c=a**b
    return c
#Functions with print
print(pow(3,2))
##############
def pow(a,b):
    c=a**b
    print(c)
pow(3,2)
#Create a function which can take any number of integers and give of addition of those.
def addition(*args):
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    return sum
print(addition(1,2,3,4,8,10,-8))
#print the variable names and it's values.
def printVariableNameAndItsValues(**args):
    for i in  args:
        print("The variable name is : " +str(i)+" and the value is : "+str(args[i]))
        print("The variable name is : ",i, " and the value is : " ,args[i])

printVariableNameAndItsValues(a=25,b=35,c="Nitya",d="Python")
#Write a function to swap values.
def swapValues(l,idx1,idx2):
    temp =l[idx1]
    l[idx1]=l[idx2]
    l[idx2]=temp
    return l
print(swapValues([1,2,3,4,5],2,3))
#Find minimum value with index.
def findMin(list):
    m=list[0]
    idx=0
    c=0
    for x in list:
        if x<m :
            m=x
            idx=c
        else:
            pass
        c+=1
    return m,idx
print(findMin([1,2,3,4,5,-8]))
#list sorting
def sortList(L):
    c=0
    for x in L:
      m,idx = findMin(L)
      L= swapValues(L,c,idx)
      c+=1
    return L
print(findMin([-4,-3,-2,-5,-1]))
#Multiline string.
a="""
Hi my name is Nitya and i am a data scientist.
Do you have any assignment for me i will do that
please let me know
"""
# print(a)
def stri(a):
    c=0
    for i in a:
        if i =="n":
            print(i,c)
        c += 1
stri("""Hi my name is Nitya and i am a data scientist.
Do you have any assignment for me i will do that
please let me know""")
#print using split function.
a="game,and,no"
l=a.split(",")
print(l)
#Get a perticular substring out of the string using string slicing techniques
s = "Happy Birthday"
s2 = "Birthday"
a=s.index(s2)
a+=4
print(a)
print(s[a:])
#Print the square till 10 numbers in list
list_square=[x**2 for x in range (10)]
print(list_square)
#set
s={x**2 for x in range(2,20,2)}
print(s)
#############
#Print a string with how many times each letter occurs in the string
s='eeeeeeerrbvgfbhgffdfsdghjghgf55'
# Expected output is e7r2
c = 1
idx = 0
finalStr = ''
if all(char == s[0] for char in s):
    finalStr=s[0]+str(len(s))
    print(finalStr)
else:
    for i in s:
        if i == s[idx + 1]:
            c += 1
            idx += 1
        else:
            finalStr += i + str(c)
            c = 1
            idx += 1
        if idx == len(s) - 1:
            break
    c = 0
    dx = len(s) - 2
    for x in range(len(s) - 1, 0, -1):
        # print(s[x])
        if s[x] == s[dx]:
            dx -= 1
            c += 1
            finalStr += s[x] + str(c + 1)
        else:
            break
    print(finalStr)


'''Solve below assignment:
Suppose you are a teacher you have ids of many students with marks in each subject and different students have taken
different Tests.You need to Average marks of each student with the Id.'''
# def getDtaFromUser():
#     D={}
#     while True:
#         studentId=input("Enter student ID: ")
#         marksList=input("Enter marks in comma separated values: ")
#         moreStudents=input('Enter "no" to quit the insertion: ')
#         if studentId in D:
#             print(studentId, "is already inserted")
#         else:
#             D[studentId]=marksList.split(',')
#         if moreStudents.lower()=="no":
#             return D
#
# print(getDtaFromUser())
# for items in getDtaFromUser().values():
#     print(items)
# D={'22': ['22','23','24','25'], '20': ['20','21','22','23','25']}
# averageMarks={}
# for x in D:
#     L=D[x]
#     s=0
#     for marks in L:
#         s+=int(marks)
#     averageMarks[x]=s/len(L)
#
# for x in averageMarks:
#     print("The average mark of" ,x, "is :",averageMarks[x])

a="123456"
k=""
for i in a:
    i=int(i)
    if i==0:
        print("n")
    elif i==1:
        print("i")
    elif i==2:
        print("t")
    elif i==3:
        print("y")
    elif i==4:
        print("a")
    elif i==5:
        print("p")
    elif i==6:
        print("r")
    elif i==7:
        print("k")
    elif i==8:
        print("s")
    else:
        print("h")
