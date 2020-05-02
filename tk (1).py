from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

GPIO21 = 21
GPIO20 = 20
GPIO16 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)
GPIO.setup(GPIO16, GPIO.OUT)

master = Tk()
master.title("GPIO Control")
master.geometry("300x100")

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   
def GPIO21select():
    GPIO.output(GPIO21, True)
    GPIO.output(GPIO20, False)
    GPIO.output(GPIO16, False)
    
def GPIO20select():
    GPIO.output(GPIO21, False)
    GPIO.output(GPIO20, True)
    GPIO.output(GPIO16, False)

def GPIO16select():
    GPIO.output(GPIO21, False)
    GPIO.output(GPIO20, False)
    GPIO.output(GPIO16, True)
    
def exit():
    GPIO.output(GPIO21, False)
    GPIO.output(GPIO20, False)
    GPIO.output(GPIO16, False)
    master.destroy()


GPIO.output(GPIO21, False)
GPIO.output(GPIO20, False)
GPIO.output(GPIO16, False)

var = IntVar()
R1 = Radiobutton(master, text="Red", variable=var, value=1,
                  command=GPIO21select)
R1.pack( anchor = W )

R2 = Radiobutton(master, text="Blue", variable=var, value=2,
                  command=GPIO20select)
R2.pack( anchor = W )

R3 = Radiobutton(master, text="Yellow", variable=var, value=3,
                  command=GPIO16select)
R3.pack( anchor = W)

b = Button(master, text="Exit", command=exit)
b.pack()

label = Label(master)
label.pack()
master.mainloop()