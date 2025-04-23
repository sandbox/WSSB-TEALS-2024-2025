class Color:
    """Color class"""
    
a = Color()
a.r = 170
a.g = 219
a.b = 18

b = Color()
b.r = 191
b.g = 10
b.b = 255

c = Color()
c.r = 19
c.g = 112
c.b = 11

def add_colors(c1, c2):
    color = Color()
    color.r = min(c1.r + c2.r, 255)
    color.g = min(c1.g + c2.g, 255)
    color.b = min(c1.b + c2.b, 255)

    return color

ab = add_colors(a, b)
bc = add_colors(b, c)

print("My new color ab is", ab.r, ab.g, ab.b)
print("My new color bc is", bc.r, bc.g, bc.b)
