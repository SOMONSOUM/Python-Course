print("\nWelcome to Python from zero to one\n")
print("Instructor: SOUM Somon\nFrom: ITC\n")
print("\t\t\tFirst step")
print("==================================================")
name = "SOUM Somon"
greeting = "Hello"
# if you want to space you can add it too
print(greeting + " " + "​" + name)
print(2 * 4)
print(2 * 3 + 4 - 1 - 6 / 5)
# if you want to space you can add it too
print(greeting + ' ' + name + '\n ')
print("\t\t\tSecond step")
print("==================================================")
# greeting = "Welcome"
# name = input("Please input your name here: ")
# print(greeting + ' ' + name)
print("-You can split sring by using \\n ")
print("-You can comment multiple lines by using \nshortcut key is 'Ctrl+/'\n")
print("\t\t\tThird step")
print("==================================================")
# If I want to calculate the area of triangle where base =10 and height =5
# You can use formula of triangle area
base = 10
height = 5
area = (int)(1 / 2 * (base * height))  # You can casting the data type too in Python
print("The area of triangle is: ", area)
print("Operation in Python such as\n+(Addition)\n-(Subtraction)\n*(Multiple)\n/(Division)\n%(Modulo)")
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print("Basic calculation")

for i in range(1, (int)(a / b)):  # You can use casting
    print(i)
print("Another method")
for i in range(1, a // b):
    print(i)

print("Array of String")

string = "Hello Somon"
print(string)
print(string[0])
print(string[-1])  # count from the end of string
print(string[0:5])  # count string from index 0 to 5
print(string[:6])  # We don't specify the start string
print(string[0:])  # we don't specify the end string so it's going to count from index 0 to the end of string
print(string[0:5:6])
print(string[0:3:2])
