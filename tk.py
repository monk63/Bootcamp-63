import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox


win = Tk()
#Intro
'''
def pr():
    print('Straigth to mars')
win.geometry("600x600")
b=Button(win,text='button',command=pr,padx=20,activeforeground='red')
b.place(x=100,y=200)

b2=Button(win,text='button2')
b2.place(x=300,y=200)
'''

'''
c=Canvas(win,height=400,width=450,bg="red")
coord=10,50,240,210
arc=c.create_arc(coord,start=0,extent=90,fill='pink')
line=c.create_line(10,10,200,200,fill='white')
c.pack()
'''

#geometry
'''
win.geometry("600x600")
c1=IntVar
c2=IntVar

cb=Checkbutton(win,text='Music',offvalue=0,onvalue=1,height=5,width=10,variable=c1)
cb.pack()

cb2=Checkbutton(win,text='Draw',offvalue=0,onvalue=1,height=5,width=10,variable=c2)
cb2.pack()

var = IntVar()
r1 = Radiobutton(win,text='option1',variable=var,value=1)
r1.pack()

r2 = Radiobutton(win,text='option2',variable=var,value=2)
r2.pack()

'''

#buttons
'''
l=Label(win,text="username")
l.pack()
e=Entry(win)
e.pack()
t=Text(win)
t.insert(INSERT,'hello')
t.pack()
'''

'''
def sum(labrl,x1,x2):
    n1= (x1.get())
    n2= (x2.get())
    sum=int (n1)+int(n2)
    label.config(text='sum is : %d' %sum)
    return

l1= Label(win,text="First NO")
l1.grid(row=1,column=0)

l2= Label(win,text="Second NO")
l2.grid(row=2,column=0)

label=Label(win)
label.grid(row=6,column=2)

x1=StringVar()
x2=StringVar()

e1=Entry(win,textvariable=x1)
e1.grid(row=1,column=2)
e2=Entry(win,textvariable=x2)
e2.grid(row=2,column=2)
sum = partial(sum,label,x1,x2)
button=Button(win,text='calculate',command=sum)
button.grid()
'''
#window widgets
'''
frame=Frame(win)
frame.pack()

frame2=Frame(win)
frame2.pack(side=BOTTOM)

rb=Button(frame,text='red',fg='red')
rb.pack(side=LEFT)

gb=Button(frame2,text='green',fg='green')
gb.pack(side=LEFT)
'''

#list works
'''
lb = Listbox(win) 
lb.insert(1,'cars')
lb.insert(2,'Benz')
lb.insert(3,'BMW')
lb.insert(4,'Fiat')
lb.pack()
'''
#top level

'''
win.title('Fast Lane')
top = Toplevel()
top.title('Draft')
'''

#message box
'''
def Mars():
    messagebox.showinfo('From Elon Musk','We are going to Mars')
b=Button(win,text='Mars Ticket',command=Mars)
b.pack()
'''

#Menu and menu buttons
'''
mb=Menubutton(win,text='Vehicle')
mb.grid()
mb.menu=Menu(mb)
mb['menu']=mb.menu

x1= IntVar()
x2= IntVar()

mb.menu.add_checkbutton(label='open',variable=x1)
mb.menu.add_checkbutton(label='open',variable=x2)

mb.pack()
'''

'''
def mars():
     file=Toplevel()
     button=Button(file,text='off to Mars')
     button.pack()

menubar = Menu(win)

filemenu = Menu(menubar)
filemenu.add_command(label='New Car',command=mars)
filemenu.add_command(label='New Spaceship',command=mars)
filemenu.add_separator()
filemenu.add_command(label='New Dock',command=mars)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=win.quit) 

menubar.add_cascade(label='Vehicle',menu=filemenu)

win.config(menu=menubar)
'''

#Scroll widgets

'''
s=Scale(win)
s.pack()

sb=Spinbox(win,from_=0,to=10)
sb.pack()
'''

'''
scrollbar=Scrollbar(win)
scrollbar.pacl(side=RIGHT,fill=Y)
list=Listbox (win,yscrollcommand=scrollbar.set)

for line in range(101):
    list.insert(END,'THis line no is'+str(line))

list.pack(side=LEFT,fill=BOTH)
'''

#Geometry methods
'''
b=0
for i in range(6):
    for j in range(6):
        b+=1
        Button(win,text=str(b),borderwidth=1).grid(row=i,column=j)
'''
'''
l1=Label(win,text='Maths')
l1.place(x=10,y=10)
e1=Entry(win,bd=5)
e1.place(x=60 , y=10 )

l2=Label(win,text='Science')
l2.place(x=10,y=60)
e2=Entry(win,bd=5)
e2.place(x=60 , y=60 )

b= Button(win,text ='submit')
b.place(x=100,y=100)
'''

#win.mainloop()

#Turtle
#kaleido spiral
'''
import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','blue','green','yellow','orange','grey','purple','pink'])

def circle(size,angle,forw):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(forw)
    circle(size+5,angle+1,forw+5)




t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(30,0,1)

ti.sleep(2)
t.hideturtle()
'''
#Modified kaleido spiral

'''
import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','blue','green','yellow','orange','grey','purple','pink'])

def circle(size,angle,forw,shape):
    t.pencolor(next(colors))
    next_shape=''
    if shape=='circle':
        t.circle(size)
        next_shape='square'
    elif shape == 'square':
        for i in range(4):
            t.forward(size*2)
            t.left(90)
        next_shape='circle'    
    t.right(angle)
    t.forward(forw)
    circle(size+5,angle+1,forw+1,next_shape)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(30,0,1,'circle')

ti.sleep(2)
t.hideturtle()
'''
