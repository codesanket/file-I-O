#Write a Python program to read an entire text file.
s=open('demo.txt','r')
print(s.read())
s.close()
#.Write a Python program to read first n lines of a file.
s1=open('demo.txt','r')
print(s1.read())
lines=s1.readline()
print(lines)

#Write a Python program to append text to a file and display the text.
s1=open('demo.txt','a')
s1.write('i am learning python')
s1.close()

#Write a Python program to read last n lines of a file.
def lastline(f,n):
    with open(f) as file:
        print('last',n,'lines from file',f)
        for line in (file.readlines()[-n:]):
            print(line,end='')
name=input('enter file name:')
n=int(input('enter number:'))
try:
    lastline(name,n)
except:
    print('error')

#Write a Python program to read a file line by line and store it into a list.

f=open("demo.txt","r")
lines=f.readlines()
print(lines)

nline=[x.strip() for x in lines]
print(nline)

#Write a Python program to read a file line by line store it into a variable.
simplel=[]
with open("demo.txt","r") as f:
    for line in f:
        simplel.append(line.strip())
    print(simplel)

#Write a python program to find the longest words.
s='hello how are you?'
list=s.split()
long=''
length=0
for i in list:
    if len(i)>length:
        long=i
        length=len(long)
print(long,length)

#Write a Python program to count the number of lines in a text file.
file=open('demo.txt','r')
count=0
for line in file:
   simple=line.split(" ")
count=+len(simple)
print('no of words in text file:',count)

#Write a Python program to count the frequency of words in a file.
f=open('demo.txt','r')
w=input('enter any word:')

s=f.read()
list=s.split()
print(list)
count=0
for i in list:
    if(i==w):
        count=count+1
print("word comes ".format(w,count))

#Write a Python program to get the file size of a plain file.
import  os
file_stat=os.stat('C:\\Users\\91866\\Desktop\\python work\\datatype1\\datatype1\\datatype1\\demo.txt')
print("file size is:",file_stat)

#Write a Python program to write a list to a file.
list=['BMW','AUDI','ALTO','fariri']

with open("demo.txt",'w') as file:
    for item in list:
        file.write(item+"\n")
print('list write to file successfuly')

#Write a Python program to copy the contents of a file to another file

#Write a Python program to read a random line from a file.

import random
lines=open('demo.txt').read().splitlines()
x=random.choice(lines)
print(x)

#Write a Python program to assess if a file is closed or not
f=open('demo.txt','r')
print(f.close)
f.close()
print(f.closed)
