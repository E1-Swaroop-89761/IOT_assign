#3] Write a program to accept three integer numbers and find its average.

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))

def average():
    return (num1+num2+num3)/3

avg = average()

print(f"Average of {num1}, {num2}, {num3} is {avg}")