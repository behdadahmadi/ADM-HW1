# Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys
import textwrap

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
# def extractDigits(num):
#     number = int(num)
#     while number > 9:
#         number = sum([int(i) for i in str(number)])
#     return int(number)
def extractDigits(num):
    number = str(num)
    while len(str(number)) > 1:
        number = sum([int(i) for i in str(number)])
    return number

def superDigit(n, k):
#    if len(n) == 1:
#         return extractDigits(n*k)
   digit = extractDigits(n) 
   digit = extractDigits(digit*k)
   return digit
#    return extractDigits(n*k)
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    liked = []
    people = 5
    for i in range(n):
        people = math.floor(people/2)
        liked.append(people)
        people = people * 3
        
        
            
    return sum(liked)   
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    #X1+V1t == X2 + V2t
    #=> X1 - X2 == V2t - V1t
    #=> X1 - X2 == t(V2-V1)
    # Write your code here
    # for i in range(1,10001):
    #     if (x1 + (i*v1)) == (x2 + (i*v2)):
    #         return "YES"
    #     else:
    #         return "NO"
    # if v1 == v2:
    #     return "NO"
        
    #for i in range(1,10001):
        #if (x1-x2) == i*(v2-v1) and (x2 - x1) > 0 and (v2 - v1) < 0:
    if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0:    
        return "YES"
    else:
        return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles_counter = Counter(candles)
    return candles_counter[max(candles_counter)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


n_shoes = int(input())

shoes = map(int,input().split())
shoes = Counter(shoes)
#shoes = [s for s in shoes]
n_cutomer = int(input())

total_earned = 0
for _ in range(n_cutomer):
    customer = input().split()
    size = int(customer[0])
    price = int(customer[1])
    if shoes[size]:
        total_earned = total_earned + price
        shoes[size] =  shoes[size] -1
print(total_earned)
        
#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
_date = input()
mm = int(_date.split(" ")[0])
dd = int(_date.split(" ")[1])
yy = int(_date.split(" ")[2])
days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(days[calendar.weekday(yy,mm,dd)])

#Text Wrap


def wrap(string, max_width):
    # p_num = 0
    # if len(string)%max_width!=0:
    #     p_num = p_num + len(string)//max_width
    # else:
    #     p_num = len(string)/max_width
    
    return textwrap.fill(string,max_width)

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    res = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]
    res = [i for i in res if i[0] + i[1] + i[2] !=n]
    print(res)
   
#String Split and Join
def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a
    # write your code here

#Find a string
def count_substring(string, sub_string):
    sub_length = len(sub_string)
    window_count = 0
    for i in range(len(string)):
        window = string[i:i+sub_length]
        if window == sub_string:
            window_count = window_count + 1
    return window_count

#Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

#What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first,last))
    # Write your code here


#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score = student_marks[query_name]
    
    print('%.2f'%(sum(score)/len(score)))

#Nested Lists
if __name__ == '__main__':
    grades = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append(score)
        students.append([name,score])
    second_min = list(sorted(set(grades)))[1]
    target_names = []
    for s in students:
        if s[1] == second_min:
            target_names.append(s[0])
    target_names.sort()
    for n in target_names:
        print(n)

#Iterables and Iterators
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
N = input()
alphabet = input()
K = input()

x = alphabet.replace(" ","")
comb = itertools.combinations(x,int(K))
y = [' '.join(i) for i in comb]
r = 0
for i in y:
    if "a" in i:
        r = r+1


print(r/len(y))

#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Print Function
if __name__ == '__main__':
    n = int(input())
    print(''.join(str(x) for x in range(1,n+1)))

#Write a function
def is_leap(year):
    leap = False
    d4 = False
    d100 = False
    d400 = False
    
    if year%4==0:
        d4 = True
    if year%100:
        d100 = True
    if year%400:
        d400 = True
        
    
    if d4:
        if d100 and d400:
            leap = True
        if d100 and not d400:
            leap = False
        if not d100 and not d400:
            leap = True
    
    # Write your logic here
    
    return leap


#Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print str(a +b)
    print str(a-b)
    print str(a*b)
    

#Python If-Else

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 !=0:
        print "Weird"
    else:
        if n >= 2 and n <= 5:
            print "Not Weird"
        elif n>=6 and n<=20:
            print "Weird"
        else:
            print "Not Weird"
        

#Say "Hello, World!" With Python
if __name__ == '__main__':
    print "Hello, World!"

