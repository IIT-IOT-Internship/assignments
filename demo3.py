import geometry

r = float(input("Enter radius of circle: "))
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

print("Area of Circle:", geometry.area_circle(r))
print("Area of Rectangle:", geometry.area_rectangle(l, w))