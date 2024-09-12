h=10
print(h)
w=5
print(w)
r=3
print(r)
pi=3.14
print(pi)
#area of circle
print(2*pi*r)
#area of triangle 
print((h*w)/2)
#area of rectangle 
print(h*w)

def area_of_circle(radius_value):
    pi=3.14 
    area=2*pi*radius_value
    print(area)
    area= round(area,2)
    print(f"***{area}")
    return area

def area_of_triangle(h_value,w_value):
    area=h_value*w_value
    print(area)
    return area
    
def area_of_rectangle(he_value,we_value): 
    area=he_value*we_value
    print(area)
    return area






print(f"area of circle {area_of_circle(10)}") 
print(f"area of triangle {area_of_triangle(10,15)}")
print(f"area of rectangle {area_of_rectangle(5,10)}")
