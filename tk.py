import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox


#win = Tk()
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
#Snake game

'''
import turtle as t
import random as rd

t.bgcolor('purple')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)  
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
'''

#matchmaker

'''
import random
import time
from tkinter import Tk,Button,DISABLED

def show_symbol(x,y):
    global first
    global prevx,prevy
    buttons[x,y]['text']=button_symbols[x,y]
    buttons[x,y].update_idletasks()
      
    if first:
        prevx=x
        prevy=y 
        first=False
    elif prevx != x or prevy != y:
        if buttons[prevx,prevy]['text'] != buttons [x,y] ['text']:
            time.sleep(0.5)
            buttons[prevx,prevy]['text'] = ' '
            buttons[x,y]['text']=' '
        else:
            buttons[prevx,prevy]['command']= DISABLED
            buttons[x,y]['command']= DISABLED
        first= True     


win = Tk()
win.title('Matchmaker')
win.resizable(width=False,height=False)
first=True
prevx=0
prevy=0

buttons={}
button_symbols = {}
symbols =[u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
          u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
          u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
          u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbols)          

for x in range(6):
    for y in range(4):
        button= Button(command = lambda x=x , y=y: show_symbol(x,y),width=10, height=8)
        button.grid(column=x,row=y)
        buttons[x,y]=button
        button_symbols[x,y]=symbols.pop()

print(u'\u270B')
print(u'\u270C')
print(u'\u2705')

win.mainloop()
'''

#smart calculator 
'''
from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}

win = Tk()
win.geometry('500x300')
win.title('Smart Pugger')
win.configure(bg='red')

l1 = Label(win , text='I am a smart calculator',width=20 , padx=3)
l1.place(x=150,y=10)
l2 = Label(win , text='My name is Elon Mars' , padx=3)
l2.place(x=180,y=40)
l3 = Label(win , text='What can I help you' , padx=3)
l3.place(x=176,y=130)

textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=100,y=160)

b1 = Button(win , text='Just this' ,command=calculate)
b1.place(x=210,y=200)

list = Listbox(win,width=20,height=3)
list.place(x=150,y=230)

win.mainloop()
'''

# database
from tkinter import *
import backend

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    backend.delete(selected_row[0])

def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()):
        list.insert(END,row)

def add_command():
    backend.insert(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get())

    list.delete(0,END)
    list.insert(END,(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()))

win = Tk()

win.wm_title('MY ROUTINE DATABASE')

l1 = Label(win, text='Date')
l1.grid(row=0,column=0)
l2 = Label(win, text='Earnings')
l2.grid(row=0,column=2)
l3 = Label(win, text='Exercise')
l3.grid(row=1,column=0)
l4 = Label(win, text='Study')
l4.grid(row=1,column=2)
l5 = Label(win, text='Diet')
l5.grid(row=2,column=0)
l6 = Label(win, text='Python')
l6.grid(row=2,column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

earning_text = StringVar()
e2 = Entry(win, textvariable=earning_text)
e2.grid(row=0,column=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable=exercise_text)
e3.grid(row=1,column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=1,column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable=diet_text)
e5.grid(row=2,column=1)

python_text = StringVar()
e6 = Entry(win, textvariable=python_text)
e6.grid(row=2,column=3)

list = Listbox(win,height=8,width=35)
list.grid(row=3,column=0,rowspan=9,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(win,text='ADD',width=12,pady=5,command=add_command)
b1.grid(row=3,column=3)

b2 = Button(win,text='Search',width=12,pady=5,command=search_command)
b2.grid(row=4,column=3)

b3 = Button(win,text='Delete date',width=12,pady=5,command=delete_command)
b3.grid(row=5,column=3)

b4 = Button(win,text='View all',width=12,pady=5,command=view_command)
b4.grid(row=6,column=3)

b5 = Button(win,text='Close',width=12,pady=5,command = win.destroy)
b5.grid(row=7,column=3)

win.mainloop()

print(u'\u2705')
