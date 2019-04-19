'''
Created on 2018724

@author: Minghong Xu
'''

from tkinter import *

def draw_person(canvas):
    my_canvas = canvas
    width = my_canvas.winfo_width()
    height = my_canvas.winfo_height()
    #draw the head
    #my_canvas.create_arc(200, 50, 300, 150, start = 0, extent = 180, style = ARC)
    #my_canvas.create_arc(200, 75, 300, 175, start = 0, extent = -180, style = ARC)
    my_canvas.create_rectangle(0.460*width,0.145*height,0.540*width,0.165*height)
    my_canvas.create_oval(0.4*width, 0.025*height, 0.6*width, 0.150*height, fill = 'white')
    
    #draw the body
    my_canvas.create_rectangle(0.3*width,0.165*height,0.7*width,0.480*height, fill = 'white')
    my_canvas.create_polygon(0.3*width,0.165*height,0.06*width,0.405*height,0.1*width,0.405*height,0.3*width,0.265*height, fill = 'white',outline='black')
    my_canvas.create_polygon(0.7*width,0.165*height,0.94*width,0.405*height,0.9*width,0.405*height,0.7*width,0.265*height, fill = 'white',outline='black')
    
    #draw hands
    my_canvas.create_line(0.94*width,0.405*height,0.97*width,0.425*height,0.94*width,0.445*height,0.912*width,0.435*height,0.926*width,0.425*height,0.94*width,0.435*height)
    my_canvas.create_line(0.9*width,0.405*height,0.9*width,0.435*height)
    my_canvas.create_arc(0.9*width,0.432*height,0.912*width,0.438*height,start = 180, extent = 180,style='arc')
    my_canvas.create_line(0.06*width,0.405*height,0.03*width,0.425*height,0.06*width,0.445*height,0.088*width,0.435*height,0.074*width,0.425*height,0.06*width,0.435*height)
    my_canvas.create_line(0.1*width,0.405*height,0.1*width,0.435*height)
    my_canvas.create_arc(0.1*width,0.432*height,0.088*width,0.438*height,start = 180, extent = 180,style='arc')
    
    #draw the legs
    my_canvas.create_line(0.3*width,0.480*height,0.24*width,0.860*height)
    my_canvas.create_line(0.5*width,0.530*height,0.34*width,0.860*height)
    my_canvas.create_line(0.7*width,0.480*height,0.76*width,0.860*height)
    my_canvas.create_line(0.5*width,0.530*height,0.66*width,0.860*height)
    
    #draw the feet
    my_canvas.create_rectangle(0.24*width,0.860*height,0.34*width,0.880*height,outline='black',fill='black')
    my_canvas.create_arc(0.22*width,0.860*height,0.26*width,0.880*height, start = 90, extent = 180,outline='black',fill='black')
    my_canvas.create_rectangle(0.66*width,0.860*height,0.76*width,0.880*height,outline='black',fill='black')
    my_canvas.create_arc(0.74*width,0.860*height,0.78*width,0.880*height, start = 90, extent = -180,outline='black',fill='black')        
