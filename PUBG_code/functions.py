'''
Created on 2018723

@author: Minghong Xu
'''
import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def in_oval(x,y,x1,y1,x2,y2):
    c = (x2-x1)/2
    b = (y2-y1)/2
    a = math.sqrt(abs(c**2 - b**2))
    if y2 - y1 < x2 - x1:
        return distance(x1+c-a,y1+b,x,y) + distance(x1+c+a,y1+b,x,y) <= x2-x1
    else:
        return distance(x1+c,y1+b-a,x,y) + distance(x1+c,y1+b+a,x,y) <= y2-y1

def triangle_area(x1,y1,x2,y2,x3,y3):
    a = distance(x1,y1,x2,y2)
    b = distance(x2,y2,x3,y3)
    c = distance(x1,y1,x3,y3)
    s = (a+b+c)/2
    return round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
    
def in_triangle(x,y,x1,y1,x2,y2,x3,y3):
    a = triangle_area(x,y,x1,y1,x2,y2) + triangle_area(x,y,x2,y2,x3,y3) + triangle_area(x,y,x1,y1,x3,y3)
    return abs(round(a,2) - round(triangle_area(x1,y1,x2,y2,x3,y3),2)) < 5

def in_rectangle(x,y,x1,y1,x2,y2):
    return x1<x<x2 and y1<y<y2

def in_4polygon(x,y,x1,y1,x2,y2,x3,y3,x4,y4):
    return in_triangle(x,y,x1,y1,x2,y2,x3,y3) or in_triangle(x,y,x1,y1,x3,y3,x4,y4)
    
def in_5polygon(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    return in_4polygon(x,y,x1,y1,x2,y2,x3,y3,x4,y4) or in_triangle(x,y,x1,y1,x4,y4,x5,y5)
