from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circ_area, perimeter as circ_perimeter
from graphics.graphics3d.cuboid import area as cuboid_area, perimeter as cuboid_perimeter
from graphics.graphics3d.sphere import area as sphere_area, perimeter as sphere_perimeter

def main():
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
            print("Rectangle Area:", rect_area(length, breadth))
            print("Rectangle Perimeter:", rect_perimeter(length, breadth))

        elif choice == "2":
            radius = float(input("Enter the radius of the circle: "))
            print("Circle Area:", circ_area(radius))
            print("Circle Perimeter:", circ_perimeter(radius))

        elif choice == "3":
            length = float(input("Enter the length of the cuboid: "))
            breadth = float(input("Enter the breadth of the cuboid: "))
            height = float(input("Enter the height of the cuboid: "))
            print("Cuboid Area:", cuboid_area(length, breadth, height))
            print("Cuboid Perimeter:", cuboid_perimeter(length, breadth, height))

        elif choice == "4":
            radius = float(input("Enter the radius of the sphere: "))
            print("Sphere Area:", sphere_area(radius))
            print("Sphere Perimeter (Circumference):", sphere_perimeter(radius))

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
