# coding=gbk
'''
Created on 20180717

author: Minghong Xu
'''
from tkinter import *
from body import draw_person
from shoot import *
from bullet import *
from threading import Timer


FONT = ('Times New Roman', 16)
total_damage = 0
damage = 0
helmet = 1
armour = 1
bullet_ratio = 1
dots = []


my_window = Tk()    # Create the graphics window
my_window.title('PUBG 伤害计算   v1.0')




#radiobutton
#equip
img_h0 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\0-helmet.gif')
img_h1 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\1-helmet.gif')
img_h2 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\2-helmet.gif')
img_h3 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\3-helmet.gif')
img_a0 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\0-armour.gif')
img_a1 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\1-armour.gif')
img_a2 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\2-armour.gif')
img_a3 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\3-armour.gif')
# weapon
img_m416 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\m416.gif')
img_ak47 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\ak47.gif')
img_ump9 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\ump9.gif')
img_mini14 = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\mini14.gif')
img_sks = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\sks.gif')
img_kar98k = PhotoImage(file = r'C:\Users\Minghong Xu\Desktop\material\98k.gif')
# funcs
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
    global helmet
    helmet = 0.45
def zero_armour():
    global armour
    armour = 1
def one_armour():
    global armour
    armour = 0.7
def two_armour():
    global armour
    armour = 0.6
def three_armour():
    global armour
    armour = 0.45
def m416_dam():
    global bullet_ratio
    bullet_ratio = 1
def ak47_dam():
    global bullet_ratio
    bullet_ratio = 1.1395
def ump9_dam():
    global bullet_ratio
    bullet_ratio = 0.907
def mini14_dam():
    global bullet_ratio
    bullet_ratio = 1.0697
def sks_dam():
    global bullet_ratio
    bullet_ratio = 1.2326
def kar98k_dam():
    global bullet_ratio
    bullet_ratio = 1.7442





#canvas
my_canvas = Canvas(master=my_window, width=400, height=700)  
my_canvas.grid(column = 0, rowspan = 8, columnspan = 2,sticky = N + S + W + E)

#damage label
damage_text = StringVar()
damage_text.set('伤害: 0')
damage_label = Label(master = my_window, textvariable = damage_text, font = FONT)
damage_label.grid(row = 0, column = 2, sticky = S)
total_damage_text = StringVar()
total_damage_text.set('总伤害: 0')
total_damage_label = Label(master = my_window, textvariable = total_damage_text, font = FONT)
total_damage_label.grid(row = 0, column = 2)

#credit label/small labels
credit_text = '数据来源：小黑盒          作者：徐铭鸿'
credit_label = Label(master = my_window, text = credit_text, font = FONT)
credit_label.grid(row = 6)
helmet_label = Label(master = my_window, text = '头盔:', font = ('Times New Roman', 26), fg = 'orange')
helmet_label.grid(row = 0, column = 4, sticky = S)
armour_label = Label(master = my_window, text = '护甲:', font = ('Times New Roman', 26), fg = 'orange')
armour_label.grid(row = 0, column = 5, sticky = S)
weapon_label = Label(master = my_window, text = '武器:', font = ('Times New Roman', 26), fg = 'orange')
weapon_label.grid(row = 0, column = 6, sticky = S)

#reset button
def damage_reset():
    global total_damage
    my_canvas.delete(ALL)
    draw_person(my_canvas)
    total_damage = 0
    total_damage_text.set('总伤害: ' + str(total_damage))
    damage = 0
    damage_text.set('伤害: ' + str(damage))
    
reset_button = Button(master = my_window, text = '重置', font = FONT, command = damage_reset)
reset_button.grid(row = 6, column = 2,padx = 20, pady = 20, sticky = S + E)


#equipment button
v1 = IntVar()
v1.set(1)
equip_helmet = [('零级头', img_h0, zero_helmet, 1, 1), ('一级头', img_h1, one_helmet, 0.7, 2), 
             ('二级头', img_h2, two_helmet, 0.6, 3), ('三级头', img_h3, three_helmet, 0.45, 4)]
v2 = IntVar()
v2.set(0)
equip_armour = [('零级甲', img_a0, zero_armour, 0, 1), ('一级甲', img_a1, one_armour, 1, 2), 
             ('二级甲', img_a2, two_armour, 2, 3), ('三级甲', img_a3, three_armour, 3, 4)]
v3 = IntVar()
v3.set(10)
equip_weapon = [('M416', img_m416, m416_dam, 10, 1), ('AK47', img_ak47, ak47_dam, 11, 2), 
             ('UMP9', img_ump9, ump9_dam, 12, 3), ('Mini 14', img_mini14, mini14_dam, 13, 4),
             ('SKS', img_sks, sks_dam, 14, 5), ('Kar98k', img_kar98k, kar98k_dam, 15, 6)]
for level, img, func, red, i in equip_helmet:
    r1 = Radiobutton(my_window, variable = v1, value = red, compound = RIGHT, image = img, text = level, command = func) #command
    r1.grid(row = i, column = 4)
for level, img, func, red, i in equip_armour:
    r2 = Radiobutton(my_window, variable = v2, value = red, compound = RIGHT, image = img, text = level, command = func) #command
    r2.grid(row = i, column = 5)
for kind, img, func, dam, i in equip_weapon:
    r3 = Radiobutton(my_window, variable = v3, value = dam, compound = RIGHT, image = img, text = kind, command = func)
    r3.grid(row = i, column = 6)

my_window.rowconfigure(0, weight = 1)
my_window.columnconfigure(0, weight = 1)
my_window.columnconfigure(1, weight = 1)
my_window.columnconfigure(2, weight = 1)


def canvas_resized(event: Event):
    my_canvas.delete(ALL)
    draw_person(my_canvas)
    draw_bullets(my_canvas,dots)

def shoot_point(event: Event):
    global total_damage
    global dots
    damage = int(shoot(my_canvas, event.x, event.y, helmet, armour)[0]*bullet_ratio)
    color = shoot(my_canvas, event.x, event.y, helmet, armour)[1]
    total_damage += damage
    total_damage_text.set('总伤害: ' + str(total_damage))
    damage_text.set('伤害: ' + str(damage))
    width = my_canvas.winfo_width()
    height = my_canvas.winfo_height()
    dots.append((event.x/width, event.y/height, color))
    #Timer(3, dots.remove((event.x/width, event.y/height, color))).start()
    b = bullet(event.x, event.y, color, my_canvas)
    b.draw()
    
my_canvas.bind('<Configure>', canvas_resized)
my_canvas.bind('<Button-1>', shoot_point)
mainloop()