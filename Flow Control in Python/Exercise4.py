name = input("What is your name? ")
age = int(input("How old are you?"))

if age >= 18:
    print("You are old enough to vote")
else:
    print("You aren't old enough to vote yet, Please come back in: {0} years more ".format(18 - age))
