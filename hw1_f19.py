'''This is Homework One for CSC 280 - 005 Fall 2019.
This will be distributed through Github Classroom.
Please fill in your name, and make sure your
code is executable. Each answer should show up properly
when I run the code while grading.  There are sample
exercises in the code for the purpose of showing you
the format I'm looking for in your responses.
'''

# PROBLEM ONE: Create variables for each data type listed, and print as a demo.
print("")
print("------------------- Homework One: ------------------")
myname = "Joe Rogero"
print("My name is: ", myname)
print ("Problem one: ..... ..... ..... .....")

# Boolean
b = True
print(b, "is type", type(b))

b=True
10>3
if 10>3:
    print(b)

# List
L=[1,2,3,4,5]
print("here is my list", L)
# integer
a=2
print(a)
# float
a=2.3
print(a)
# string
thisvariable="This is cool"
print(thisvariable)


# PROBLEM TWO: Show the use of each of: +, -, *, **, /, //, % with numbers.
print("")
print ("Problem two: ..... ..... ..... .....")

a,b =5,9

print(a, '+', b, '=', a+b)  #This demonstrates +

b,c=1,2
print(b,'+',c,'=', b+c)

print(c,'',b,'=', c-b)

print(b,'*',c,'=', b*c)
import math
print(b,'**',c,'=', b**c)

print(c,'/',b,'=', c/b)

d,w=64,8

print(d,'//',w,'=', d//w)




print(((2/10)*(100)),'%')






# PROBLEM THREE: Use the range command and other skills to find the
#                sum of odd integers between 1003 and 30239 inclusive.
print("")
print ("Problem three: ..... ..... ..... .....")
print("Sum of odds between 1003 and 30239: ",sum(range(1003,30240,3)))

# Example: Sum of even integers between 8 and 20 inclusive:
print("Sum of evens between 8 and 20: ", sum(range(8,21,2)))



# PROBLEM FOUR: Create a list of 10 strings. Then, print out the third and
#               seventh items.
print("")
print ("Problem four: ..... ..... ..... .....")
List=[1,2,3,4,5,6,7,8,9,10]
print("Here is my list:",List)
print("The foruth item is:", List[3])
print("The seventh item is:", List[6])










#Example: Here, I create a list of 5 integers and print the 4th one.


