import graphics.rectangle
from graphics.circle import area, perimeter
import graphics.graphics3d.cuboid as cuboid
from graphics.graphics3d.sphere import *

while True:
    print("\nChoose a shape to calculate area and perimeter:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Cuboid")
    print("4. Sphere")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        print("Rectangle Area:", graphics.rectangle.area(length, breadth))
        print("Rectangle Perimeter:", graphics.rectangle.perimeter(length, breadth))

    elif choice == "2":
        radius = float(input("Enter the radius of the circle: "))
        print("Circle Area:", area(radius))
        print("Circle Perimeter:", perimeter(radius))

    elif choice == "3":
        length = float(input("Enter the length of the cuboid: "))
        breadth = float(input("Enter the breadth of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        print("Cuboid Area:", cuboid.area(length, breadth, height))
        print("Cuboid Perimeter:", cuboid.perimeter(length, breadth, height))

    elif choice == "4":
        radius = float(input("Enter the radius of the sphere: "))
        print("Sphere Area:", area(radius))
        print("Sphere Perimeter (Circumference):", perimeter(radius))

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

