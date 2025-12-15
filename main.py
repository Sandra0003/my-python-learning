from math import *

from orca.debug import eventDebugLevel

print("*")
print("**")
print("***")
print("***")
print("**")
print("*")


print("   /|")
print("  / |")
print(" /  |")
print("/   |")

char_name = "sam"
print(char_name)
isMale = False
print(isMale)

print("\n Sandra \n and\n savio  \n are \n  siblings")

name = "savio"
print(name.upper().isupper())
print(len(name))
print(name[2])
array= [1,2,3,4,5]
print(array[3])

def area(a, b):
    areaofshape = 0.5 * a * b
    print(areaofshape)

area(3,4)
area(4,2)


def largest(a,b,c):
    if a > b :
        print("a is greater than b")
    if a > c:
        print("a is greater than c")
    else:
        print("a is less than c")
largest(2,1,2)

bb =9
cc =8
print(bb + cc)


def iseven(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

iseven(9)

str =" i love python"
print(str.find("python"))
print(str.replace("python","html"))
print(str * 6)

g = 9
print("g is" , g)
print(int(g))

# input("enter your name")

fruits = ["apple","orange","banana"]
x,y ,m= fruits
print(x,y,m)


phrase = "sara is bob"
print(phrase.index("b"))
print(phrase.replace("bob","sab"))

for letter in phrase:
    print(letter)

print(3 * 3)
print(3 * 3 + 3)
print(10 / 3)
print(abs(-10))
print(abs(10))
print(pow(2,2))
print(max(2,6))
print(min(2,6))
print(round(2.8))
print(sqrt(25))
print(floor(8.9))

x =(input("enter your name"))
b = int(input("enter your age"))
print("hai , " + x + " age" , b)

# basic calculater
def calculater(num1, num2, opr):
    if opr == "+":
        return  num1 + num2
    elif opr == "-":
        return num1 -num2
    elif opr == "*":
        return num1 * num2
    else:
        return "enter any opr"

while True:
    num1 = int(input("Enter number one:"))
    num2 = int(input("enter  number two: "))
    opr = input("enter operation :")
    result = calculater(num1, num2, opr)
    print(result)
    cont = input("Do you want to continue?(y/n)")
    if cont == "n":
        break




