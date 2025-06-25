#1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

len = float(input("Enter lenth of the rectangle: "))
bre = float(input("Enter breadth of the rectangle: "))

def area():
    area = len * bre
    print(f"Area of rectangle = {area}")

def per():
    perimeter = 2*(len+bre)
    print(f"Perimeter of the rectangle = {perimeter}")


per()
area()