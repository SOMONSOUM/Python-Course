# Write a program to check wether a number is odd or even
number = int(input("Please input a number to check: "))
if number % 2 == 0:
    print("The number {} is even number".format(number))
else:
    print("The number {} is odd number".format(number))
