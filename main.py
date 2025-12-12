
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