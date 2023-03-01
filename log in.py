from tkinter import *
import os
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('userpassw.db')
conn.execute('''CREATE TABLE LoginDatabase
         (USERNAME           TEXT    NOT NULL,
         PASSWORD       TEXT);''')
cursor = conn.cursor()
roots = Tk() 
roots.title('Signup') 
intruction = Label(roots, text='Please Enter new Credidentials\n') 
intruction.grid(row=0, column=0, sticky=E) 
 
nameL = Label(roots, text='New Username: ') 
pwordL = Label(roots, text='New Password: ') 
nameL.place(x=50,y=150)
pwordL.place(x=50,y=200) 
 
nameE = Entry(roots) 
pwordE = Entry(roots, show='*') 
nameE.place(x=150,y=150) 
pwordE.place(x=150,y=200)
 

    


def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
 
    intruction = Label(rootA, text='Please Login\n') 
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Username: ')
    pwordL = Label(rootA, text='Password: ') 
    nameL.place(x=50,y=150)
    pwordL.place(x=50,y=200)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.place(x=150,y=150)
    pwordEL.place(x=150,y=200)

    loginB = Button(rootA, text='Login', command=validate) 
    loginB.place(x=100,y=300)

 


def signup():
    us=nameE.get()
    pas=pwordE.get()
    cursor.execute("INSERT INTO LoginDatabase (USERNAME,PASSWORD) \
      VALUES (?,?)",(us,pas));
    roots.destroy() 
    Login()



signupbutton = Button(roots, text='Sign In', command=signup) 
signupbutton.place(x=90,y=300)
already = Button(roots, text='Already User', command=Login) 
already.place(x=150,y=300)






    
    
 
 
