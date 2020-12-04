########################################################
############# Code written by mikey1093 ################
####################  12/3/2020  #######################
## Mouse mover to prevent your PC from falling asleep ##
########################################################

import mouse 
from pynput.mouse import Button, Controller
from time import *
from tkinter import *
import threading 
import pyautogui


root = Tk()
root.title("CrackMouse")
root.geometry("300x50")

def refresh():
    root.update()
    root.after(1000,refresh)

def start_move():
    pyautogui.FAILSAFE = False
    refresh()
    t = threading.Thread(target=move).start()
    t.setDaemon(True)
    t.start()

def move():
    while var.get() == 1:
        pyautogui.move(0, 5)
        sleep(2)
        pyautogui.press("shift")
        pyautogui.move(0, -5)
        sleep(2)
        var.get()
        if var.get() == 0:
            break

var = IntVar()

c = Checkbutton(root, text="Move Mouse", variable=var, command=start_move)
c.pack()
myLabel = Label(root, text=var.get()).pack

root.mainloop()



