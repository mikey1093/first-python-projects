import mouse 
from pynput.mouse import Button, Controller
from time import *
from tkinter import *
import threading 
import pyautogui



root = Tk()
root.title('Move Mouse')
root.geometry('200x50')

x = 1

def update_var():
    global x
    x = 0


def refresh():
    root.update()
    root.after(1000,refresh)

def start_move():
    refresh()
    threading.Thread(target=move).start()

def move():
    while var.get() == 1:
        pyautogui.move(0,1)
        sleep(3)
        pyautogui.move(0, -1)
        sleep(3)
        var.get()
        if var.get() == 0:
            break


var = IntVar()

c = Checkbutton(root, text='Move Mouse', variable=var, command=start_move)
c.pack()
myLabel = Label(root, text=var.get()).pack


root.mainloop()


# Original loop with mouse

#while var.get() == 1:
    #    mouse.move(500, 300, absolute="False")
    #    sleep(3)
    #    mouse.move(300, 500, absolute='False')
    #    sleep(2)
    #    var.get()
    #    if var.get() == 0:
    #        break
