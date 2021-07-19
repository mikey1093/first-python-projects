from tkinter import *
from math import *
from PIL import ImageTk,Image
import numpy as np
from matplotlib import pylab
from matplotlib import pyplot as plt 


root = Tk()
root.title("Mikeys Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

f_num= None
math= None

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global button_add
    global f_num 
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))
    elif math == "division":
        e.insert(0, f_num / float(second_number))
    
def button_subtract():
    first_number = e.get()
    global f_num
    global math 
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math 
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num 
    global math 
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_sin():
    first_number = e.get()
    e.insert(0, sin(float(first_number)))

def button_cos():
    first_number = e.get()
    e.insert(0, cos(float(first_number)))

def button_tan():
    first_number = e.get()
    e.insert(0, tan(float(first_number)))

def button_sqrt():
    first_number = e.get()
    sq_rt = sqrt(float(first_number))
    e.delete(0, END)
    e.insert(0, (sq_rt))
    
def button_sqrd():
    first_number = e.get()
    sqrd = float(first_number)**2
    e.delete(0, END)
    e.insert(0, sqrd)

def button_neg():
    first_number = e.get()
    neg = float(first_number) * -1
    e.delete(0, END)
    e.insert(0, neg)

def button_dot():
    first_number = e.get()
    dot = first_number + str(".")
    e.delete(0, END)
    e.insert(0, dot)

def button_f():
    first_number = e.get()
    far = (float(first_number)*(9/5))+32
    e.delete(0, END)
    e.insert(0, far)

def button_c():
    first_number = e.get()
    cel = (float(first_number)-32)*(5/9)
    e.delete(0, END)
    e.insert(0, cel)

button_1=Button(root, text="1",bg="white",padx=40,pady=20,command=lambda: button_click(1)).grid(row=3,column=0)
button_2=Button(root, text="2",bg="white",padx=40,pady=20,command=lambda: button_click(2)).grid(row=3,column=1)   
button_3=Button(root, text="3",bg="white",padx=43,pady=20,command=lambda: button_click(3)).grid(row=3,column=2)
button_4=Button(root, text="4",bg="white",padx=40,pady=20,command=lambda: button_click(4)).grid(row=2,column=0)
button_5=Button(root, text="5",bg="white",padx=40,pady=20,command=lambda: button_click(5)).grid(row=2,column=1)
button_6=Button(root, text="6",bg="white",padx=43,pady=20,command=lambda: button_click(6)).grid(row=2,column=2)
button_7=Button(root, text="7",bg="white",padx=40,pady=20,command=lambda: button_click(7)).grid(row=1,column=0)
button_8=Button(root, text="8",bg="white",padx=40,pady=20,command=lambda: button_click(8)).grid(row=1,column=1)
button_9=Button(root, text="9",bg="white",padx=43,pady=20,command=lambda: button_click(9)).grid(row=1,column=2)
button_dot=Button(root, text=".",bg="light gray",padx=52,pady=20,command=button_dot).grid(row=5,column=3)
button_0=Button(root, text="0",bg="white",padx=40,pady=20,command=lambda: button_click(0)).grid(row=4,column=0)
#button_pi=Button(root, text="π",bg="light gray",padx=40,pady=20,command=lambda: button_click(3.14)).grid(row=8,column=0)

button_add=Button(root, text="+",bg="light gray",padx=39,pady=20,command=button_add).grid(row=5,column=0) 
button_equal=Button(root, text="=",bg="light gray",padx=91,pady=20,command=button_equal).grid(row=5,column=1,columnspan=2)
button_clear=Button(root, text="C",bg="firebrick3",padx=40,pady=20,command=button_clear).grid(row=4,column=1)
button_neg=Button(root, text="(-)",bg="white",padx=40,pady=20,command=button_neg).grid(row=4,column=2)

button_subtract=Button(root, text="-",bg="light gray",padx=41,pady=20,command=button_subtract).grid(row=6,column=0)
button_multiply=Button(root, text="*",bg="light gray",padx=41,pady=20,command=button_multiply).grid(row=6,column=1)
button_divide=Button(root, text="/",bg="light gray",padx=44,pady=20,command=button_divide).grid(row=6,column=2)

button_f=Button(root, text="C->F",bg="light gray",padx=40,pady=22,command=button_f).grid(row=3,column=3,rowspan=1)
button_c=Button(root, text="F->C",bg="light gray",padx=40,pady=20,command=button_c).grid(row=4,column=3)





def open(): 
    top = Toplevel()
    top.title("Other Calculator")
    e = Entry(top, width=35, borderwidth=5)
    e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear():
        e.delete(0, END)
    
    def button_add():
        first_number = e.get()
        global button_add
        global f_num 
        global math
        math = "addition"
        f_num = float(first_number)
        e.delete(0, END)

    def button_equal():
        second_number = e.get()
        e.delete(0, END)
        if math == "addition":
            e.insert(0, f_num + float(second_number))
        elif math == "subtraction":
            e.insert(0, f_num - float(second_number))
        elif math == "multiplication":
            e.insert(0, f_num * float(second_number))
        elif math == "division":
            e.insert(0, f_num / float(second_number))

    def button_subtract():
        first_number = e.get()
        global f_num
        global math 
        math = "subtraction"
        f_num = float(first_number)
        e.delete(0, END)

    def button_multiply():
        first_number = e.get()
        global f_num 
        global math 
        math = "multiplication"
        f_num = float(first_number)
        e.delete(0, END)

    def button_divide():
        first_number = e.get()
        global f_num 
        global math 
        math = "division"
        f_num = float(first_number)
        e.delete(0, END)

    def button_sin():
        first_number = e.get()
        e.insert(0, sin(float(first_number)))

    def button_cos():
        first_number = e.get()
        e.insert(0, cos(float(first_number)))

    def button_tan():
        first_number = e.get()
        e.insert(0, tan(float(first_number)))

    def button_sqrt():
        first_number = e.get()
        sq_rt = sqrt(float(first_number))
        e.delete(0, END)
        e.insert(0, (sq_rt))

    def button_sqrd():
        first_number = e.get()
        sqrd = float(first_number)**2
        e.delete(0, END)
        e.insert(0, sqrd)

    def button_neg():
        first_number = e.get()
        neg = float(first_number) * -1
        e.delete(0, END)
        e.insert(0, neg)

    def button_dot():
        first_number = e.get()
        dot = first_number + str(".")
        e.delete(0, END)
        e.insert(0, dot)

    button_1=Button(top, text="1",bg="white",padx=40,pady=20,command=lambda: button_click(1)).grid(row=3,column=0)
    button_2=Button(top, text="2",bg="white",padx=40,pady=20,command=lambda: button_click(2)).grid(row=3,column=1)   
    button_3=Button(top, text="3",bg="white",padx=43,pady=20,command=lambda: button_click(3)).grid(row=3,column=2)
    button_4=Button(top, text="4",bg="white",padx=40,pady=20,command=lambda: button_click(4)).grid(row=2,column=0)
    button_5=Button(top, text="5",bg="white",padx=40,pady=20,command=lambda: button_click(5)).grid(row=2,column=1)
    button_6=Button(top, text="6",bg="white",padx=43,pady=20,command=lambda: button_click(6)).grid(row=2,column=2)
    button_7=Button(top, text="7",bg="white",padx=40,pady=20,command=lambda: button_click(7)).grid(row=1,column=0)
    button_8=Button(top, text="8",bg="white",padx=40,pady=20,command=lambda: button_click(8)).grid(row=1,column=1)
    button_9=Button(top, text="9",bg="white",padx=43,pady=20,command=lambda: button_click(9)).grid(row=1,column=2)
    button_dot=Button(top, text=".",bg="light gray",padx=42,pady=20,command=button_dot).grid(row=8,column=1)
    button_0=Button(top, text="0",bg="white",padx=40,pady=20,command=lambda: button_click(0)).grid(row=4,column=0)
    button_pi=Button(top, text="π",bg="light gray",padx=40,pady=20,command=lambda: button_click(3.14)).grid(row=8,column=0)

    button_add=Button(top, text="+",bg="light gray",padx=39,pady=20,command=button_add).grid(row=5,column=0) 
    button_equal=Button(top, text="=",bg="light gray",padx=91,pady=20,command=button_equal).grid(row=5,column=1,columnspan=2)
    button_clear=Button(top, text="C",bg="firebrick3",padx=40,pady=20,command=button_clear).grid(row=4,column=1)
    button_neg=Button(top, text="(-)",bg="white",padx=40,pady=20,command=button_neg).grid(row=4,column=2)

    button_subtract=Button(top, text="-",bg="light gray",padx=41,pady=20,command=button_subtract).grid(row=6,column=0)
    button_multiply=Button(top, text="*",bg="light gray",padx=43,pady=20,command=button_multiply).grid(row=6,column=1)
    button_divide=Button(top, text="/",bg="light gray",padx=44,pady=20,command=button_divide).grid(row=6,column=2)

    button_sqrt=Button(top, text="√",bg="light gray",padx=43,pady=20,command=button_sqrt).grid(row=8,column=2)
    button_sin=Button(top, text="sinx",bg="light gray",padx=33,pady=20,command=button_sin).grid(row=7,column=0)
    button_cos=Button(top, text="cosx",bg="light gray",padx=33,pady=20,command=button_cos).grid(row=7,column=1)
    button_tan=Button(top, text="tanx",bg="light gray",padx=35,pady=20,command=button_tan).grid(row=7,column=2)






root.mainloop()
