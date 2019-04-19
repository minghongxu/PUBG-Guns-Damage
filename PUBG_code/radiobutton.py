# coding=gbk
from tkinter import *

my_window = Tk()

img_h0 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\0-helmet.gif')
img_h1 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\1-helmet.gif')
img_h2 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\2-helmet.gif')
img_h3 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\3-helmet.gif')

h = {'零级头': 1.0, '一级头': 0.7, '二级头': 0.6, '三级头': 0.45}
helmet = 1
armour = 1
base_damage = 43

def func(x):
    helmet = h[x]
    print(helmet)
    return

'''
def zero_helmet():
    global helmet
    helmet = 1
def one_helmet():
    global helmet
    helmet = 0.7
def two_helmet():
    global helmet
    helmet = 0.6
def three_helmet():
    helmet = 0.45
'''
    
def zero_armour():
    armour = 1
def one_armour():
    armour = 0.7
def two_armour():
    armour = 0.6
def three_armour():
    armour = 0.45

def m416_dam():
    base_damage = 43
def ak47_dam():
    base_damage = 49
def ump9_dam():
    base_damage = 39
def mini14_dam():
    base_damage = 46
def sks_dam():
    base_damage = 53
def kar98k_dam():
    base_damage = 75


v1 = IntVar()
v1.set(1)
equip_helmet = [('零级头', img_h0, 1, 0), ('一级头', img_h1, 0.7, 1), 
             ('二级头', img_h2, 0.6, 2), ('三级头', img_h3, 0.45, 3)]

for level, img, red, i in equip_helmet:
    r1 = Radiobutton(my_window, variable = v1, value = red, compound = RIGHT, image = img, text = level, command = func(level)) #command
    r1.grid(row = i, column = 4)
    
print(helmet)
    
mainloop()

