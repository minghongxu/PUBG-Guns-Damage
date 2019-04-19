'''
Created on 2018724

@author: Minghong Xu
'''
from functions import *

def shoot(canvas,x,y,helmet=1,armour=1):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    if in_oval(x,y,0.4*width, 0.025*height, 0.6*width, 0.150*height):
        return (101*helmet,'red')
    elif in_rectangle(x,y,0.460*width,0.145*height,0.540*width,0.165*height):
        return (76, 'red')
    #body
    elif in_triangle(x,y,0.3*width,0.165*height,0.5*width,0.165*height,0.3*width,0.215*height) or in_triangle(x,y,0.5*width,0.165*height,0.7*width,0.165*height,0.7*width,0.215*height):
        return (45*armour, 'blue')
    elif in_5polygon(x,y,0.3*width,0.215*height,0.5*width,0.165*height,0.7*width,0.215*height,0.7*width,0.28*height,0.3*width,0.28*height):
        return (47*armour, 'blue')
    elif in_rectangle(x,y, 0.3*width,0.28*height ,0.7*width,0.38*height):
        return (43*armour, 'blue')
    elif in_rectangle(x,y, 0.3*width,0.33*height ,0.7*width,0.43*height):
        return (41*armour, 'blue')
    elif in_rectangle(x,y, 0.3*width,0.38*height ,0.7*width,0.48*height):
        return (43*armour, 'blue')
    #leg
    elif in_5polygon(x,y,0.3*width,0.48*height,0.5*width,0.48*height,0.5*width,0.530*height,0.447*width,0.640*height,0.27*width,0.67*height):
        return (23, 'green')
    elif in_5polygon(x,y,0.7*width,0.48*height,0.5*width,0.48*height,0.5*width,0.530*height,0.553*width,0.640*height,0.73*width,0.67*height):
        return (23, 'green')
    elif in_4polygon(x,y,0.447*width,0.640*height,0.27*width,0.67*height,0.24*width,0.860*height,0.34*width,0.860*height):
        return (19, 'green')
    elif in_4polygon(x,y,0.553*width,0.640*height,0.73*width,0.67*height,0.66*width,0.860*height,0.76*width,0.860*height):
        return (19, 'green')
    elif in_rectangle(x,y,0.24*width,0.860*height,0.34*width,0.880*height) or in_oval(x,y,0.22*width,0.860*height,0.26*width,0.880*height):
        return (12, 'green')
    elif in_rectangle(x,y,0.66*width,0.860*height,0.76*width,0.880*height) or in_oval(x,y,0.74*width,0.860*height,0.78*width,0.880*height):
        return (12, 'green')
    #arm
    elif in_4polygon(x,y,0.3*width,0.165*height,0.18*width,0.285*height,0.2*width,0.335*height,0.3*width,0.265*height):
        return (23, 'green')
    elif in_4polygon(x,y,0.06*width,0.405*height,0.18*width,0.285*height,0.2*width,0.335*height,0.1*width,0.405*height):
        return (19, 'green')
    elif in_5polygon(x,y,0.06*width,0.405*height,0.1*width,0.405*height,0.088*width,0.438*height,0.06*width,0.445*height,0.03*width,0.425*height):
        return (12, 'green')
    elif in_4polygon(x,y,0.7*width,0.165*height,0.82*width,0.285*height,0.8*width,0.335*height,0.7*width,0.265*height):
        return (23, 'green')
    elif in_4polygon(x,y,0.94*width,0.405*height,0.82*width,0.285*height,0.8*width,0.335*height,0.9*width,0.405*height):
        return (19, 'green')
    elif in_5polygon(x,y,0.94*width,0.405*height,0.9*width,0.405*height,0.912*width,0.438*height,0.94*width,0.445*height,0.97*width,0.425*height):
        return (12, 'green')
    else:
        return (0,'yellow')