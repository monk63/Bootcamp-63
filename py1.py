#x= 5
#print(x)

## Restrictions on variables
 
#x ="monkgee"

#print(x[2])

#x.replace('e', 'b')
#print(x)

#x ="monkgee"
#print(x[1:3])

#x=input("Enter the first value: ")
#y=input("Enter second value: ")
#x=int(x)
#y=int(y)
#z=x+y

#print(z)
"""
c=input("Enter temperature in celcius : ")
c=int(c)
f=(9/5)*c+32
print(int(f))
"""
#hour convertor
"""
m=input("Enter number of minutes: ")
s=input("Enter the number of seconds: ")
h=int(m)/60+int(s)/3600
print(h)
"""
#function
"""
def add(x,y):
    z=x+y
    return print(z)

a=5
b=10
c=add(a,b)
print(c)    
"""

#function user input
"""
def add(x,y):
    z=x+y
    return print(z)

a=input("Enter the first value: ")
b=input("Enter the second value: ")
add(int(a),int(b))
"""
#converting functions
"""
def temp(c):
    f=(9/5)*c+32
    return print(f)

c=input("Enter the temperature in celsuis: ")
c=int(c)
temp(c)

def leng(m, s):
    h=m/60 + s/3600
    return print(h)

m= input("Write the numbers of minutes: ")
m=int(m)

s=input("Write the nuimber of seconds: ")
s=int(s)

leng(m,s)
"""

#Modifying functions
'''
def div(a,b):
    if(b==0):
        return print("This is not possible")
    else:    
        c=a/b
        return print(c)

a=input("Enter the first value: ")
b=input("Enter the second value: ")

div(int(a),int(b))
'''
#Multiple conditions
'''
x= "benz"
y=input("Enter the word: ")

if (x==y):
    print("x and y are equal")
else:
    print("x is not equal to y")    
'''
#Nested conditons
'''
x=3
y=3
z=2

if (x==y):
    if(x!=z):
        print("x is equal to y")
else:
    print("Values do not match")
'''

#loops and user input
'''
x= [0,1,2,3,4,5,6,7,8,9,]

for i in x:
    x[i] = input("Enter your name: ")

print(x)    
'''

# Range function
'''
for x in range(2,10):
    print(x)
'''

#nested loops
'''
x=["benz","amg","bmw","audi","lambo"]

y=["london","paris","new york","lome","amsterdam"]

a=0
b=0
for i in x:
    for j in y:
        print(x[a],y[b])
        b+=1
    a+=1 
    b = 0
'''

# date and time
'''
import datetime

x =datetime.datetime.now()

print(x.strftime("%A"))
'''
#opening a file
'''
file=open("text.txt","r")
x=file.read()
print(x)
'''

#writing a file
'''
file=open("test.txt","a")
file.write("bike\n")
file.write("motor\n")
file.close()
'''
#json files
'''
import json

x={"name":"michael","car":"benz","age":2000,"job":"developer"}

y=json.dumps(x)

print(y)
'''

#Application 1 Dice problem
'''
import random
print("This is a dice stimulator")
x = "y"

while x == "y":
    number = random.randint(1,6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    x = input("Press y to roll again: ")
    
'''
#dictionary
'''
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on wrong keys: ")
        else:
            return("You have entered wrong input please enter just y or n: ")
    else:
        print("pugger your paw steps on wrong keys: ")

word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
'''

#hangman
'''
import random
def hangman():

    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word: " , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character ")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter your name ")
print("Welcome" , name )
print("-------------------")
print("try to guess the word in less than 10 attempts ")
hangman()
print()

'''

#tic tac toe AI based module
'''
board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied ')
            else:
                print('please type a number between 1 and 9 : ')

        except:
            print('Please type a number: ')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('computer placed an o on position' , move , ':')
                printBoard(board)
        else:
            print("you win!")
            break




    if isBoardFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n): ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
'''

#Numpy
'''
import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])

x = arr[arr%2==1]

print(x)
'''
#pandas
'''
import pandas as pd

p=['a','b','c','d','e']
q=[1,2,3,4,5]
r=(1:'a',2:'b',3:'c',4:'d',5:'e')  

a = pd.Series(data = p)
print(a)
'''

#dataframes
'''
import numpy as np
import pandas as pd

A=[1,2,3,4]
B=[5,6,7,8]
C=[9,0,1,2]
D=[3,4,5,6]

df=pd.DataFrame([A,B,C,D],['a','b','c','d'],['W','X','Y','Z'])
print(df) 

print(df>3)
print(df(df>3))
'''

#Matplot lib
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x= np.linspace(0,10,20)

y=x + x

z=x+y

plt.plot(x,y)
'''

#Plotter
'''
import numpy as np
import pandas as pd
import plotly.plotly as pl
import plotly.offline as po
import cufflinks as cf
po.init_notebook_mode(connected = True)
cf.go_offline()
def createdata(data):
    if(data == 1):
        x = np.random.rand(100,5)
        df1 = pd.DataFrame(x,columns=['A','B','C','D','E'])
    elif(data == 2):
        x = [0,0,0,0,0]
        r1= [0,0,0,0,0]
        r2= [0,0,0,0,0]
        r3= [0,0,0,0,0]
        r4= [0,0,0,0,0]
        print('Enter the values for columns')
        i=0
        for i in [0,1,2,3,4]:
            x[i] = input()
            i = i + 1
        print('Enter the values for first row')
        i=0
        for i in [0,1,2,3,4]:
            r1[i] = int(input())
            i = i + 1
        print('Enter the values for second row')
        i=0
        for i in [0,1,2,3,4]:
            r2[i] = int(input())
            i = i + 1
        print('Enter the values for third row')
        i=0
        for i in [0,1,2,3,4]:
            r3[i] = int(input())
            i = i + 1
        print('Enter the values for fourth row')
        i=0
        for i in [0,1,2,3,4]:
            r4[i] = int(input())
            i = i + 1
        df1 = pd.DataFrame([r1,r2,r3,r4] , columns = x)
    elif(data == 3):
        file = input('Enter the file name')
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
    else:
        print('DataFrame creation failed please enter in between 1 to 3 and try again')
    return df1
def plotter(plot):
    if(plot == 1):
        finalplot = df1.iplot(kind='scatter')
    elif(plot == 2):
        finalplot = df1.iplot(kind='scatter',mode='markers' ,symbol='x',colorscale='paired')
    elif(plot == 3):
        finalplot = df1.iplot(kind='bar')
    elif(plot == 4):
        finalplot = df1.iplot(kind='hist')
    elif(plot == 5):
        finalplot = df1.iplot(kind='box')
    elif(plot == 6):
        finalplot = df1.iplot(kind='surface')
    else:
        finalplot = print('Select only between 1 to 7')
    return finalplot
def plotter2(plot):
    col = input('Enter the number of columns you want to plot by selecting only 1 , 2 or 3')
    col = int(col)
    if(col==1):
        colm = input('Enter the column you want to plot by selecting any column from dataframe head')
        if(plot==1):
            finalplot = df1[colm].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[colm].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[colm].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[colm].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[colm].iplot(kind='box')
        elif(plot==6 or plot==7):
            finalplot = print('Bubble plot and surface plot require more than one column arguments')
        else:
            finalplot = print('Select only between 1 to 7')
    elif(col==2):
        print('Enter the columns you want to plot by selecting from dataframe head')
        x = input('First column')
        y = input('Second column')
        if(plot==1):
            finalplot = df1[[x,y]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y]].iplot(kind='surface')
        elif(plot==7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,size=size)
        else:
            finalplot = print('Select only between 1 to 7')
    elif(col==3):
        print('Enter the columns you want to plot')
        x=input('First column')
        y=input('Second column')
        z=input('Third column')
        if(plot==1):
            finalplot = df1[[x,y,z]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y,z]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y,z]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y,z]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y,z]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y,z]].iplot(kind='surface')
        elif(plot==7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,z=z,size=size )
        else:
            finalplot = print('Select only between 1 to 7')
    else:
        finalplot = print('Please enter only 1 , 2 or 3')
    return finalplot
def main(cat):
    if(cat == 1):
        print('Select the type of plot you need to plot by writing 1 to 6')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        plot = int(input())
        output = plotter(plot)
    elif(cat == 2):
        print('Select the type of plot you need to plot by writing 1 to 7')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('7.Bubble plot')
        plot = int(input())
        output = plotter2(plot)
    else:
        print('Please enter 1 or 2 and try again')        
print('Select the type of data you need to plot(By writing 1,2 or 3)')
print('1.Random data with 100 rows and 5 columns')
print('2.Customize dataframe with 5 columns and. 4 rows')
print('3.Upload csv/json/txt file')
data = int(input())
df1 = createdata(data)
print('Your DataFrame head is given below check the columns to plot using cufflinks')
df1.head()
print('What kind of plot you need , the complete data plot or columns plot')
cat = input('Press 1 for plotting all columns or press 2 for specifying columns to plot')
cat = int(cat)
main(cat)
'''