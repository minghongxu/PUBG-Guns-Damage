'''
Created on 2018724

@author: Minghong Xu
'''
import time
from threading import Timer

class bullet:
    def __init__(self,x,y,color,canvas):
        self.x = x
        self.y = y
        self.color = color
        self.o = 0
        self.canvas = canvas
        
    def deletedot(self):
        self.canvas.delete(self.o)
        
    def draw(self):
        t1 = time.time()
        self.o = self.canvas.create_oval(self.x-4,self.y-4,self.x+4,self.y+4, fill = self.color)
        Timer(3, self.deletedot).start()

        

        
def draw_bullets(canvas,dots):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    for x,y,color in dots:
        b = bullet(x*width, y*height, color, canvas)
        b.draw()
