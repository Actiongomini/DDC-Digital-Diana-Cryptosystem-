import tkinter
import random
import string
import os
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *

wheel = {
    1:'h',
    2:'d',
    3:'a',
    4:'e',
    5:'r',
    6:'k',
    7:'f',
    8:'o',
    9:'q',
    10:'j',
    11:'i',
    12:'v',
    13:'p',
    14:'n',
    15:'y',
    16:'b',
    17:'u',
    18:'g',
    19:'x',
    20:'c',
    21:'w',
    22:'s',
    23:'z',
    24:'m',
    25:'t',
    26:'l'}
rwheel = {
    'h':1,
    'd':2,
    'a':3,
    'e':4,
    'r':5,
    'k':6,
    'f':7,
    'o':8,
    'q':9,
    'j':10,
    'i':11,
    'v':12,
    'p':13,
    'n':14,
    'y':15,
    'b':16,
    'u':17,
    'g':18,
    'x':19,
    'c':20,
    'w':21,
    's':22,
    'z':23,
    'm':24,
    't':25,
    'l':26}

lton = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26}
ltonA = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'}


#window requisites
mom = tkinter.Tk()
mom.overrideredirect(1)
mom.withdraw()


#functions
def messagewindow():
    win = Tk()
    win.title(text)
    message = "What do you want to use"
    
    screen_width = win.winfo_screenwidth() #get screen measurements
    screen_height = win.winfo_screenheight()
    window_width = 150  # Adjust when needed
    window_height = 150

    x_position = (screen_width - window_width) // 2 #find centre window
    y_position = (screen_height - window_height) // 2

    win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}") #move window
    
    Label(win, text=message).pack()
    Button(win, text='Encoder', command=useencoder).pack()
    Button(win, text='Decoder', command=usedecoder).pack()
    Button(win, text='Generate OTP', command=generateotp).pack()
    Button(win, text='Quit', command=bye).pack()
def bye():
    quit()
def decode(attempt):
    first=int(lton[key[attempt]])
    firstk=int(lton[message[attempt]])
    firsta=first-firstk
    if firsta<=0:
        firsta=firsta+26
    firstd=str(wheel[firsta])
    print(firstd,end="")
    
def encode(attempt):
    outer=int(lton[key[attempt]])
    inner=int(rwheel[message[attempt]])
    firsta=outer-inner
    if firsta<=0:
        firsta=firsta+26
    firstd=str(ltonA[firsta])
    print(firstd,end="")

def useencoder():
    global key
    global message
    key = simpledialog.askstring(text,'please give the key')
    message = simpledialog.askstring(text,'please enter the message you would like to encode')
    dialogbox = messagebox.showinfo(text,'Output in console')
    print('the encoded message is: ',end="")

    attemptstotal=len(key)
    attemptsdone=0

    while attemptsdone<attemptstotal:
        encode(attemptsdone)
        attemptsdone=attemptsdone+1
    
def usedecoder():
    global key
    global message
    key = simpledialog.askstring(text,'please give the key')
    message = simpledialog.askstring(text,'please enter the coded message')
    dialogbox = messagebox.showinfo(text,'Output in console')
    print('the decoded message is: ',end="")

    attemptstotal=len(key)
    attemptsdone=0

    while attemptsdone<attemptstotal:
        decode(attemptsdone)
        attemptsdone=attemptsdone+1

def randomgenfile():
    randomletter = str(random.choice(string.ascii_lowercase),)
    with open(file_path, "a") as file:
        file.write(randomletter)

def randomgennofile():
    randomletter = str(random.choice(string.ascii_lowercase),)
    print(randomletter,end="")
        
def generateotp():
    number = simpledialog.askinteger(text,'how many characters would you like')
    userinput =messagebox.askyesno(text,'Would you like to save this to a file?')
    if userinput==True:
        if os.path.exists(file_path):
            open(file_path, "w").close()
        x = range(number)
        for n in x:
            randomgenfile()
            print(n,'/',number)
        print('DONE')
    else:
        x = range(number)
        for n in x:
            randomgennofile()
    
#file_path config
file_path = "one_time_pad.txt"

#version+name
text=('Digital Diana wheel')
version=str('test v1')


#debug
print('runnning',text,version)


#code start
mom.update
dialogbox = messagebox.showinfo(text,'Welcome to the Diana cryptosystem decoder')
messagewindow()
mom.mainloop()

#test otp is whtvi
#test code is vdtva
#should result in 'hello'
#saif better not leak this
