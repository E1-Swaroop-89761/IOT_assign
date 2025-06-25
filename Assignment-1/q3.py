#4] Write a Python function to find the maximum of three numbers.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 > num2:
    if num1 > num3:
        print("Num1 is greatest...")
    else:
        print("Num3 is greatest...")
else:
    if num2 > num3:
        print("Num2 is greatest...")
    else:
        print("Num3 is greatest...")