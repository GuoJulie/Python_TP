# !/usr/bin/python
# -*- coding: utf-8 -*-
import math
import re
from tkinter import *


cal_state = False

def showText0():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '0')
    if tmp.get() is not '':
        tmp.insert(END, '0')


def showText1():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '1')
    if tmp.get() is not '':
        tmp.insert(END, '1')

def showText2():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '2')
    if tmp.get() is not '':
        tmp.insert(END, '2')

def showText3():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '3')
    if tmp.get() is not '':
        tmp.insert(END, '3')

def showText4():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '4')
    if tmp.get() is not '':
        tmp.insert(END, '4')

def showText5():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '5')
    if tmp.get() is not '':
        tmp.insert(END, '5')

def showText6():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '6')
    if tmp.get() is not '':
        tmp.insert(END, '6')

def showText7():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '7')
    if tmp.get() is not '':
        tmp.insert(END, '7')

def showText8():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '8')
    if tmp.get() is not '':
        tmp.insert(END, '8')

def showText9():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '9')
    if tmp.get() is not '':
        tmp.insert(END, '9')

def showTextP():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '.')
    if tmp.get() is not '':
        tmp.insert(END, '.')

def showTextPG():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, '(')
    if tmp.get() is not '':
        tmp.insert(END, '(')

def showTextPD():
    global entry, cal_state, tmp
    if cal_state is True:
        entry.delete(0, END)
    cal_state = False
    entry.insert(END, ')')
    if tmp.get() is not '':
        tmp.insert(END, ')')

def Addition():
    global entry, cal_state, tmp
    entry.insert(END, '+')
    cal_state = False
    if tmp.get() is not '':
        tmp.insert(END, '+')

def Soustraction():
    global entry, cal_state, tmp
    entry.insert(END, '-')
    cal_state = False
    if tmp.get() is not '':
        tmp.insert(END, '-')

def Multiplication():
    global entry, cal_state, tmp
    entry.insert(END, '*')
    cal_state = False
    if tmp.get() is not '':
        tmp.insert(END, '*')

def Division():
    global entry, cal_state, tmp
    entry.insert(END, '/')
    cal_state = False
    if tmp.get() is not '':
        tmp.insert(END, '/')

def Puissance():
    global entry, cal_state, tmp
    entry.insert(END, '^')
    cal_state = False
    if tmp.get() is not '':
        tmp.insert(END, '^')

def Sin():
    global entry, cal_state, tmp
    txt = entry.get()
    entry.delete(0, END)
    entry.insert(END, 'sin(' + txt + ')')
    tmp.insert(END, 'math.sin(math.radians(' + txt + '))')
    cal_state = False

def Cos():
    global entry, cal_state, tmp
    txt = entry.get()
    entry.delete(0, END)
    entry.insert(END, 'cos(' + txt + ')')
    tmp.insert(END, 'math.cos(math.radians(' + txt + '))')
    cal_state = False

def Tan():
    global entry, cal_state, tmp
    txt = entry.get()
    entry.delete(0, END)
    entry.insert(END, 'tan(' + txt + ')')
    tmp.insert(END, 'math.tan(math.radians(' + txt + '))')
    cal_state = False

def effaceDernierChiffre():
    global entry, cal_state, tmp
    entry.delete(len(entry.get())-1, END)
    tmp.delete(len(tmp.get()) - 1, END)
    cal_state = False

def effaceTous():
    global entry, cal_state, tmp
    entry.delete(0, END)
    tmp.delete(0, END)
    cal_state = False

def calculate():
    global result, x, y, entry, cal_state, textnote, L_Note,tmp
    txt = entry.get()
    indicator_list = ["sin", "cos","tan"]
    try:
        if '^' in txt:
            txt = txt.replace('^', '**')
            result = eval(txt)
        elif any(indicator in txt for indicator in indicator_list):
            txt = tmp.get()
            result = eval(txt)
        else:
            result = eval(txt)
        entry.delete(0, END)
        entry.insert(0, result)
        cal_state = True
        L_Note.configure(text="")
        tmp.delete(0, END)

    except SyntaxError:
        assert L_Note.configure(text = "Syntax Error !!!"), "Syntax Error !!"




fenetre = Tk()

fenetre.title('Calculatrice')
sw = fenetre.winfo_screenwidth()
sh = fenetre.winfo_screenheight()
ww = 400
wh = 570
x = (sw - ww) / 2
y = (sh - wh) / 2
fenetre.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
fenetre.resizable(0,0)

menuBar = Menu(fenetre)
menu = Menu(menuBar)
for item in ['Aide', 'Mode Basique', 'Mode Scientifique']:
    menu.add_command(label = item)
menuBar.add_cascade(label = "Menu", menu = menu)
fenetre['menu'] = menuBar



entry = Entry(fenetre, font=(20), bg=('grey'))
tmp = Entry(fenetre)
entry.grid(row = 0, column = 1, columnspan = 5, ipadx = 110, ipady = 10)
B_Puissance = Button(fenetre, text='^', width = 10, height = 5, command = Puissance).grid(row = 1, column = 1)
B_sin = Button(fenetre, text='sin', width = 10, height = 5, command = Sin).grid(row = 1, column = 2)
B_cos = Button(fenetre, text='cos', width = 10, height = 5, command = Cos).grid(row = 1, column = 3)
B_tan = Button(fenetre, text='tan', width = 10, height = 5, command = Tan).grid(row = 1, column = 4)
B_1 = Button(fenetre, text='1', width = 10, height = 5, command = showText1).grid(row = 2, column = 1)
B_2 = Button(fenetre, text='2', width = 10, height = 5, command = showText2).grid(row = 2, column = 2)
B_3 = Button(fenetre, text='3', width = 10, height = 5, command = showText3).grid(row = 2, column = 3)
B_4 = Button(fenetre, text='4', width = 10, height = 5, command = showText4).grid(row = 3, column = 1)
B_5 = Button(fenetre, text='5', width = 10, height = 5, command = showText5).grid(row = 3, column = 2)
B_6 = Button(fenetre, text='6', width = 10, height = 5, command = showText6).grid(row = 3, column = 3)
B_7 = Button(fenetre, text='7', width = 10, height = 5, command = showText7).grid(row = 4, column = 1)
B_8 = Button(fenetre, text='8', width = 10, height = 5, command = showText8).grid(row = 4, column = 2)
B_9 = Button(fenetre, text='9', width = 10, height = 5, command = showText9).grid(row = 4, column = 3)
B_0 = Button(fenetre, text='0', width = 10, height = 5, command = showText0).grid(row = 5, column = 1)
B_P = Button(fenetre, text='.', width = 10, height = 5, command = showTextP).grid(row = 5, column = 2)
B_E = Button(fenetre, text='=', width = 10, height = 5, command = calculate).grid(row = 5, column = 5)
B_AC = Button(fenetre, text='AC', width = 10, height = 5, command = effaceTous).grid(row = 2, column = 5)
B_PG = Button(fenetre, text='(', width = 10, height = 5, command = showTextPG).grid(row = 5, column = 3)
B_PD = Button(fenetre, text=')', width = 10, height = 5, command = showTextPD).grid(row = 5, column = 4)
B_C = Button(fenetre, text='C', width = 10, height = 5, command = effaceDernierChiffre).grid(row = 3, column = 5)
B_Plus = Button(fenetre, text='+', width = 10, height = 5, command = Addition).grid(row = 2, column = 4)
B_Moins = Button(fenetre, text='-', width = 10, height = 5, command = Soustraction).grid(row = 3, column = 4)
B_Multiple = Button(fenetre, text='*', width = 10, height = 5, command = Multiplication).grid(row = 4, column = 4)
B_Division = Button(fenetre, text='/', width = 10, height = 5, command = Division).grid(row = 4, column = 5)
L_Note = Label(fenetre)
L_Note.grid(row=6, column=1, columnspan=5)

fenetre.mainloop()
