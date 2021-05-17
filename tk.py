import tkinter
from tkinter import *
from functools import partial


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

frame=Frame(win)
frame.pack()

frame2=Frame(win)
frame2.pack()

rb=Button(frame,)


win.mainloop()

