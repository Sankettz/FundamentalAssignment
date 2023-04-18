import math

def surface_area_and_volume_of_cylinder(radius, height):
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
    volume = math.pi * radius**2 * height
    return surface_area, volume

print(surface_area_and_volume_of_cylinder(9, 5))
