#1.Write a Python function to find the maximum of three numbers.
a=int(input('enter any number:'))
b=int(input('enter any number:'))
c=int(input('enter any number:'))

def max_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else :
        return c
result=max_number(a,b,c)
print('greater number is:',result)

# Write a Python function to sum all the numbers in a list.
#given list is
s=[8, 2, 3, 0, 7]
def add(s):
    return sum(s)
print(add(s))

#Write a Python function to multiply all the numbers in a list.
d=[8, 2, 3, -1, 7]
def mul(d):
    total=1
    for i in d:
        total*=i
    return  total
print(mul(d))

# Write a Python function to reverse a string.
def rev_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = reversed_string + char
    return reversed_string
given_string="1234abcd"
final=rev_string(given_string)
print('given_string',given_string)
print('rev_string',rev_string(given_string))

#Write a Python function to check whether a number falls within a given range.
def simple(start,end,key):
    a=set()
    for i in range(start,end+1):
        a.add(i)
        print('set a is',a)
        if key in a:
            print('key is present a',key)
    else:
             print('print key is not present a',key)
a=int(input('enter start point:'))
b=int(input('enter end point:'))
c=int(input('enter key of key: '))
simple(a,b,c)

#Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count_upperlower(string):
        upper = 0
        lower = 0
        for char in string:
            if char.isupper():
                upper+=1
            elif char.islower():
                lower+=1
        print('upper case count  and lower case count: ',upper,lower)
count1=input("enter the any string")
count_upperlower(count1)

#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#givin list is:
a= [1, 2, 3, 3, 3, 3, 4, 5]
def comm_sorted(a):
    comm_list=set(a)
    return comm_list
print(comm_sorted(a))

#Write a Python function that checks whether a passed string is a palindrome or not.
s=input()
def palindrome(s):
    rev=''
    for char in s:
        rev=char+rev
    if s==rev:
        print('string is palindrome')
    else:
        print('string is not palindrome')
palindrome(s)

#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
a='green-red-yellow-black-white'
def comm_sorted(a):
    s=a.split('-')
    s.sort()
    print(s)
comm_sorted(a)

#Write a Python program to detect the number of local variables declared in a function.
x=50
print(x)
def my_function():
    print('this is inside the function')
my_function()

#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
add=lambda x,y:x+15

mul=lambda x,y:x*y

a=int(input('enter any number :'))
print('addition afer 15 additing is :',add(a,a))

b=int(input('enter any number'))
c=int(input('enter any number'))
print('multiplection is :',mul(a,b))

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number
def num(n):
     y=lambda x:x*n
     return y
result=num(5)
print(result(10))
print(result(5))

#Write a Python program to sort a list of tuples using Lambda.
a=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sdata=sorted(a,key=lambda x:(x[1]))
print('sorted by element')
print(sdata)

#Write a Python program to sort a list of dictionaries using Lambda.
a=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
def mydata(a):
    return a ['make']
newlist=sorted(a,key=mydata)
print(newlist)

#Write a Python program to filter a list of integers using Lambda.
s=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def data1(s):
     return s
evennumber=list(filter(lambda x: x%2==0,s))
print('even number is',evennumber)
oddnumber=list(filter(lambda x: x%2!=0,s))
print('odd number is:',oddnumber)
data1(evennumber)
data1(oddnumber)

#.Write a Python program to square and cube every number in a given list of integers using Lambda.
z=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def scdata(z):
     return z
square=list(map(lambda x: x**2, z))
print('squareroot is:',square)

cube=list(map(lambda x: x**3, z))
print('cube is:',cube)

scdata(square)
scdata(cube)

#Write a Python program to find if a given string starts with a given character using Lambda.
string="hello my name is sanket"
def data(string):
     return string
c=input('enter your character')
a=lambda x:True if x.startswith(c) else False
print(a(string))
data(string)

#Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
s=[-1, 2, -3, 5, 7, 8, 9, -10]
arrange=sorted(s,key=lambda  x: x>=0)
print('original sorted list:',arrange)

#Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
f=[1, 2, 3, 5, 7, 8, 9, 10]
def eveodd(f):
     even=len(list(filter(lambda  x:x%2==0,f)))
     print('total even number:',even)

     odd=len(list(filter(lambda x:x%2!=0,f)))
     print('total odd number:',odd)
eveodd(f)

#Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
l=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
def mul(l):
    div=(list(filter(lambda x:x%19==0,l)))
    print('number is divisible by 19',div)

    divv=(list(filter(lambda x:x%13==0,l)))
    print('number is divisible by 13',divv)
mul(l)

#Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.









