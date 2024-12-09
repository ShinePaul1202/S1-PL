import graphics.rectangle
import graphics.circle
import graphics.graphics3d.cuboid
import graphics.graphics3d.sphere

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
radius_circle = float(input("Enter the radius of the circle: "))

length_cuboid = float(input("Enter the length of the cuboid: "))
breadth_cuboid = float(input("Enter the breadth of the cuboid: "))
height_cuboid = float(input("Enter the height of the cuboid: "))
radius_sphere = float(input("Enter the radius of the sphere: "))

print("Rectangle Area:", graphics.rectangle.area(length, breadth))
print("Circle Area:", graphics.circle.area(radius_circle))
print("Cuboid Area:", graphics.graphics3d.cuboid.area(length_cuboid, breadth_cuboid, height_cuboid))
print("Sphere Area:", graphics.graphics3d.sphere.area(radius_sphere))
