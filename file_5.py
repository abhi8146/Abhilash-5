'''
# ! -----> common functions for list

l1 = [6,7,8,9,0]
print(len(l1))

print(max(l1))
print(min(l1))

# l1 = [6,8,9,"p","u"]
# print(max(l1)) #---> error coz its a combination of int and string
# print(min(l1)) #---> error coz its a combination of int and string

# l1 = [6,7,8,9,0,8.89,-5,0.78]
# print(min(l1)) # -5

# l1 = [5,7,8,9,0,8.89,-5,0.78]
# index()---> to get index value of specific element
# print(l1.index(9))

# l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
# count()---> how many num of times an element is repeated
# print(l1.count(6))

# ! some functions which is specifically used for list

# To add element inside list
# ? insert(index_value,element)---> to add element at specific index position
# l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
# l1.insert(2,"car")
# print(l1)


# ? To delete element from list
# l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
# pop()---> last element will be delete
# l1.pop()
# print(l1)

# pop(index_value)---> used to delete element at specific index
# l1.pop(4) # 4 is index value
# print(l1)

# Remove(element)---> used to delete element directly
#,l1.remove(8.89)
# print(l1)

# clear()---> to complete delete all element in list
# l1.clear()
# print(l1)

# del--> to delete the list
# del l1 # or del(l1)
# print(l1)

# ? ---> join 2 list
l1 = [9,0,8]
l2 = ["p","o","t",34]
print(l1+l2)

# or
# extend()---> to combine 2 lists
l1.extend(l2)
print(l1)

# ? ------> copy()
l1=[6,7,8,9,3,]
l2=l1.copy()
#print(l2)
#print(l1)

print(id(l1))
print(id(l2))

# ! diff between shallow copy and deep copy
# * shallow copy
# import copy
# l1 = [8,9,0,[5,6],[3,2,1]]
# l2 = copy.copy(l1)
# l1.append(890)
# print(l1)
# print(l2)

# * deep copy ---> used to copy the list with nested list
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
# print(l1[-1][1])---> to index nested list

l2 = copy.deepcopy(l1)
l1[-1].append("aunty")
print(l1)
print(l2)

# ? sort ----> arrange element in list in ascending or descending order
l1 = [9,7,45,0,-6,5,12]
l1.sort() # to arrange in ascending order
print(l1)

l1.sort(reverse=True) # to sort in decending oeder
print(l1)

l1 = ['z','1','0','p',9]
l1.sort()
print(l1)#---> error


# ? list constructor
# * list()---> to conver other collrction datatype to list
l3 = ((8,9,0))
print(list(l3))

l4 = (8,9)
print(list(l4))

# ! ---> nested list

l1 = [8,9,[0,8,7],["p","0",'y'],[8,'t']]
print(l1[-2][1]) #---> 0

print(l1[1:4])
print(l1[1:-1])

# ? to delete "t" from l1
l1[-1].remove('t')
print(l1)

# ? combine these ["p","o",'y'],[8,'t'] list in l1 to ["p","o",'y',8,'t']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

# ! ----> Tuple
# * char of tuple


# 1.) Tuple have to be surrounded by ()
# 2.) The elements inside tuple are not changeble
# 3.) The elements inside tuple are indexed
# 4.) the element will execute in order
# 5.) It is heterogenous
# 6.) It allow duplicate elements

# Eg:
t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))

# ? indexing slicing are all same as list

l1 = (8)
print(type(l1)) # int

l1 = (8,)
print(type(l1)) # tuple

t1 = 8,9
print(type(t1))# tuple

t2 = 8,
print(type(t2))# tuple

# len(), min(),max(), index(), count()---> all same as list

# To add element inside tuple ---> cannot add
# cannot delete any element from tuple

# * join 2 tuples
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)

# To add all element inside list
sum()
l1 = (8,9,7,6)
print(sum(l1))


# * sort tuple
t1 = (8,9,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1,reverse=True)))

# * Iterate list and tuples

l1 = [9,8,0,6,5]
for i in l1:
    print(i)

# * Iterate based on index value

l1 = [9,8,0,6,5,8,56]
for i in range(0,len(l1)):
    print(l1[i])

# ! ----> string
 s1 = '0'
 print(type(s1))

s1 = "u"
print(type(s1))

s1 = "hello world"
# * To access string
print(s1)
# indexing and slicing---> same as list and tuple
# print(s1[0:5])


# -----> common functions

# len(), min(),max(),index(),count()
s1 ="hello world"
print(len(s1))
print(max(s1))
print(min(s1))
# ord()----> used to find the ASCII value of a character
s1 = 'u'
print(ord(s1))


# functions of string
s1 = "hello world"
# To convert all characters to upper case
#print(str.upper())

# ? to convert to lower case
s1 = "HFREDGiou"
print(s1.lower())

# strip()---> to eliminate the space in beginnig and end of string
s1 = "wher are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

# split()---> to split the words in string based on a character
s1 = "where are you?"
print(s1.split())
print(s1.split("r"))

# print(s1.count('e'))


# * Replace()
s1 = "where are you?"
print(s1.replace('r','&&'))

# Swapcase()----> to convert capital to small and small to capital at a time
s1 =- "Hey there"
print(s1.Swapcase())


# * title()---> to write the string in format of title
s1 = 'never giveUP'
print(s1.title())

# * Capitalize()---> 1st char of string will be converted to capital
s1 = 'never giveUP'
print(s1.capitalize())

# * join the strings
s1 = "hello"
s2 = "world"
print(s1+s2)

# * spliline()---> used to split the string based on lines
# print(s1.splitlines())

# * find()---> to find the index based on a character
s1 ="hello world"
print(s1.find('z'))
print(s1.index('z'))



# * join()--->
l1 = ["hey","there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
print(s1.endswith('1'))
print(s1.startswith('w'))
print(s1.split("r"))
s1= "67"
print(type(s1))
print(s1.isdigit())
# * print the string in reverse manner
s1 = "welcome to all"
print(s1[::-1])


# ! --->Eg:1
# wap to find the number of lower case letters
s1 = "HEY there you aRE"
count = 0
for i in s1:
    if i.islower():
        count+=1
print("The total num of lower case letters:",count)

# ! ----> Eg:2 r--->"$"
s1 = 'restarter'
print(s1.replace('r',"$"))
s1 = "IMAGIN"
print(s1.replace('I',"&"))

fst = s1[0]
bal = s1[1:]
txt = bal.replace  
str1 = "bbbbbyyybbbaaioo"
str2 = "%"

# ! -----> Eg:3
s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
# chacters = len(s1)
# print(chracters)


# words = s1.split(" ")
# print(len(words))


santenses = s1.split('.')
for i in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))
'''

space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)
