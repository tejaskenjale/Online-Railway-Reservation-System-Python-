import tkinter as tk

root = tk.Tk()
deli = 200           # milliseconds of delay per character
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=10)

def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)

shif.msg = 'Welcome To Railway Reservation System '
shif()
labl.place(x=100,y=0)
