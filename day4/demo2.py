# Lambda conversion functions
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda feet: feet * 12
inches_to_cm = lambda inches: inches * 2.54


# Higher-order function
def distance_converter(distance, conversion_type, conversion_function):
    result = conversion_function(distance)
    print(f"{conversion_type} = {result}")

km = float(input("Enter distance in kilometers:"))
m = float(input("Enter distance in meters:"))
cm = float(input("Enter distance in centimeters:"))
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches:"))

print("\nDistance Conversions:")
distance_converter(km,"Kilometers to Meters", km_to_m)
distance_converter(m,"Meters to Centimeters", m_to_cm)
distance_converter(cm,"Centimeters to Millimeters", cm_to_mm)
distance_converter(feet,"Feet to Inches", feet_to_inches)
distance_converter(inches,"Inches to Centimeters", inches_to_cm)
