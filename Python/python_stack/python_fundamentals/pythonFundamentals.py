######
# Find and Replace
######
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find("day")
# print words.replace("day", "month", 1)

######
# Min and Max
######

#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

#x = [2,54,-2,7,12,98]
#print "The maximum number is", max(x)
#print "The minimum number is", min(x)

######
#First and Last
######

#Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0]
# print x[len(x)-1]
# y = [x[0],x[len(x)-1]]
# print y

######
#New List
######

#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

# x = [19,2,54,-2,7,12,98,32,10,-3,6]
# x= sorted(x)
# halfLength = (len(x))/2
# halfList = []
# while halfLength>=0:
#     halfList.append(x[0])
#     del x[0]
#     halfLength-=1
# x.insert(0,halfList)
# print x

####################
#Assignment: Multiples, Sum, Average
####################

#This assignment has several parts. All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!

######
#Multiples
######

#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
# for i in range(1,1001,2):
#     print i

#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

# for i in range(5,1000001,5):
#     print i

######
#Sum List
######

#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
# sum = 0
# for i in a:
#     sum+=i
# print sum

#######
#Average List
#######

# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

# avg = 0
# for i in a:
#     avg+=i
# avg = avg/len(a)
# print avg

#####################
#Assignment: Filter by Type
#####################

# sI = 45
# mI = 100
# bI = 455
# eI = 0
# spI = -23
# sS = "Rubber baby buggy bumpers"
# mS = "Experience is simply the name we give our mistakes"
# bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
# eS = ""
# aL = [1,7,4,21]
# mL = [3,5,7,34,3,2,113,65,8,89]
# lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# eL = []
# spL = ['name','address','phone number','social security number']

# randList = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]

# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

######
#Integer
######

#If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

######
#String
######

#If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

######
#List
######

#If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

# for i in randList:
#     if type(i)==int:
#         if i>=100:
#             print i, "That's a big number"
#         elif i<100:
#             print i, "That's a small number"
#     elif type(i)==str:
#         if len(i)>=50:
#             print i, "Long sentence"
#         else:
#             print i, "Short sentence"
#     elif type(i)==list:
#         if len(i)>=10:
#             print i, "Big list!"
#         else: print i, "Short list."
# print "That's all folks!"

####################
#Assignment: Type List
####################

#Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

#Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

#Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# l1 = ['magical unicorns',19,'hello',98.98,'world']
# l2 = [2,3,1,7,4,12]
# l3 = ['magical','unicorns']

# def analyzer(lst):
#     sum = 0
#     string = ""
#     checker = []

#     for i in lst:
#         if type(i)==int:
#             sum += i
#             checker.append("integer")
#         elif type(i)==float:
#             sum+=i
#             checker.append("integer")
#         else:
#             string+=(i+" ")
#             checker.append("string")
#     if "integer" in checker and "string" in checker:
#         print "The list you entered is of mixed type"
#     elif "integer" in checker:
#         print "The list you entered is of integer type"
#     else: 
#         print "The list you entered is of string type" 
#     print "String:", string
#     print "Sum:", sum
#     print checker


# analyzer(l1)
# analyzer(l2)
# analyzer(l3)

###################
#Assignment: Compare Lists
###################

#Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

#Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

# def comparer(lst1, lst2):
#     if len(lst1)!=len(lst2):
#         print "The lists are not the same"
#         return
#     counter = 0
#     for i in lst1:
#         if i != lst2[counter]:
#             print "The lists are not the same"
#             return
#         else:
#             counter+=1
#     print "The lists are the same"

# comparer(list_one, list_two)

#######################
#Assignment: Find Characters
#######################
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.


# input
# word_list = ['hello','world','my','name','is','Anna']


# def container(lst, char):
#     new_list=[]
#     for i in lst:
#         if char in i:
#             new_list.append(i)
#     print new_list

# container(word_list, "a")

###################
#Assignment: Checkerboard
###################
# Write a program that prints a 'checkerboard' pattern to the console.

# Your program should require no input and produce console output that looks like so:

# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. In our case we will alternate stars and spaces. The goal is to repeat a process several times. This should make you think of looping.

# def checkboard(width, height):
#     line = "* "
#     oddLine = " *"
#     for i in range(0,height):
#         if i%2==0:
#             print line*width
#         else:
#             print oddLine*width

# checkboard(10,10)

########################
#Optional Assignment: Multiplication Table
########################

#Create a program that prints a multiplication table in your console.



#Your table should look like the following example:

# x   1  2  3  4  5  6  7  8   9  10  11  12
# 1   1  2  3  4  5  6  7  8   9  10  11  12
# 2   2  4  6  8 10 12 14 16  18  20  22  24
# 3   3  6  9 12 15 18 21 24  27  30  33  36
# 4   4  8 12 16 20 24 28 32  36  40  44  48
# 5   5 10 15 20 25 30 35 40  45  50  55  60
# 6   6 12 18 24 30 36 42 48  54  60  66  72
# 7   7 14 21 28 35 42 49 56  63  70  77  84
# 8   8 16 24 32 40 48 56 64  72  80  88  96
# 9   9 18 27 36 45 54 63 72  81  90  99 108
# 10 10 20 30 40 50 60 70 80  90 100 110 120
# 11 11 22 33 44 55 66 77 88  99 110 121 132
# 12 12 24 36 48 60 72 84 96 108 120 132 144

# def timesTables(val1, val2):
#     #set an initial count less than times tables parameters. This function builds an array line by line and then stringifies it to return the string multiplication table
#     count = 1
#     lineStarter = 1
#     firstLine = ["x "]
#     #build the initial line
#     while lineStarter<=val1:
#         firstLine.append(lineStarter) 
#         firstLine[lineStarter]=str(firstLine[lineStarter])+ " "
#         lineStarter+=1
#     print "".join(firstLine)
#     #this builds each subsequent line, reseting the variables each time. Then it does the same as the first line constructor
#     while count<=val2:
#         lineStarter=1
#         line=[str(count)+" "]
#         while lineStarter<=val1:
#             line.append(lineStarter*count)
#             line[lineStarter]= str(line[lineStarter])+ " "
#             lineStarter+=1
#         print "".join(line)  
#         count+=1  
        
        

# timesTables(12,12)

##################
#Assignment: Fun with Functions
##################
# Create a series of functions based on the below descriptions.

############
#Odd/Even:
############
#Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

# Your program output should look like below:

# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number

# def oddEven():
#     for i in range (1,20,2):
#         print "Number is a "+str(i)+". This is an odd number."
#         print "Number is a "+str(i+1)+". This is an even number."
# oddEven()

#################
#Assignment: Scores and Grades
#################
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# The result should be like this:

# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# ...
# End of the program. Bye!
# import random
# def scoreGrade():
#     print "Scores and Grades"
#     for i in range(0,10):
#         rdm = random.randint(60,100)
#         if rdm<70:
#             grade = "D"
#         elif rdm<80:
#             grade = "C"
#         elif rdm<90:
#             grade = "B"
#         else:
#             grade="A"
#         print "Score: "+str(rdm)+"; your grade is a "+grade
#     print "End of program, Bye!"

# scoreGrade()

####################
#Assignment: Making and Reading from Dictionaries
####################Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

# Write a function that will print something like the following as it executes:
# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

# myDict = {
#     "Name":"Warren",
#     "Age": 33,
#     "Country": "USA",
#     "Language": "Espanyol"
# }

# def aboutMe(lst):
#     print "My name is "+lst["Name"]
#     print "My age is "+ str(lst["Age"])
#     print "My country of birth is "+lst["Country"]
#     print "My favorite language is "+ lst["Language"]

# aboutMe(myDict)

########################
#Assignment: Dictionary in, tuples out
########################Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

# function input
# my_dict = {
#   "Speros": "(555) 555-5555",
#   "Michael": "(999) 999-9999",
#   "Jay": "(777) 777-7777"
# }
# # #function output
# # [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

# def tuple(lst):
#     tupList=[]
#     for i in lst:
#         val = lst[i]
#         tupList.append((i,val))
#     print tupList

# tuple(my_dict)

##########################
# Assignment: Making Dictionaries
##########################

# Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. Here are two example lists:

# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# # Hacker Challenge:
# # If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

# def comList(lst1, lst2):
#     if len(lst2)>len(lst1):
#         temp = lst2
#         lst2 = lst1
#         lst1 = temp
#     personAnimal = zip(lst1,lst2)
#     personAnimalDict = dict(personAnimal)
#     print personAnimalDict

# comList(name, favorite_animal)


