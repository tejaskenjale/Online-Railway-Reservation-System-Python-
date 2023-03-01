from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import re


root=Tk()
root.title("sample gui application")

top=Frame(root,width=1350,height=100,bd=14,relief="raise")
top.pack(side=TOP)
l11=Label(top,text="Railway Reservation Form ",font=('algerian',50),bd=10,width=41,justify='center')
l11.grid(row=0,column=0)

bottom=Frame(root,width=1910,height=150,bd=14,relief="raise")
bottom.pack(side=BOTTOM)

left=Frame(root,width=1000,height=800,bd=14,relief="raise")
left.pack(side=LEFT)

right=Frame(root,width=1000,height=800,bd=14,relief="raise")
right.pack(side=RIGHT)


l1=Label(text="ENTER PASSENGER NAME : ",fg="black",font=('Verdana',20))
l1.place(x=100,y=200)
e1=Entry(width=30)
e1.place(x=575,y=210)

l2=Label(text="ENTER THE SOURCE : ",fg="black",font=('Verdana',20))
l2.place(x=100,y=300)
c1=ttk.Combobox(root)
c1.place(x=575,y=310)
c1['values']=('Ahmadnagar','Akolner','Belvandi','Bhandewadi Halt','Chitali','Dahegaon','Kanhegaon','Kashti','Kedgaon','Kopargaon','Nipani Vadgaon','Padhegaon','Pargaon Sudrik','Puntamba','Rahuri','Sanvatsar','Shrigonda Road','Vadala Road Bby','Vambori','Vilad','Adarki','Ambale','Jarandeshwar','Karad','Lonand','Malkapur','Masur','Murud','Nandgaon','Rahimatpur','Satara','Shenoli','Shirravde','Wathar','Agran','Dhulgaon','Arag','Bedag','Bolwad','Gulvanchi','Langarpeth','Dhalgaon','Jath Road','Kirloskarvadi','Madhavnagar','Miraj Junction','Nimblak','Ranjani','Belanki','Takari','Vishrambag')
c1.current()

l3=Label(text="ENTER THE DESTINATION : ",fg="black",font=('Verdana',20))
l3.place(x=100,y=400)
c2=ttk.Combobox(root)
c2.place(x=575,y=410)
c2['values']=('Ahmadnagar','Akolner','Belvandi','Bhandewadi Halt','Chitali','Dahegaon','Kanhegaon','Kashti','Kedgaon','Kopargaon','Nipani Vadgaon','Padhegaon','Pargaon Sudrik','Puntamba','Rahuri','Sanvatsar','Shrigonda Road','Vadala Road Bby','Vambori','Vilad','Adarki','Ambale','Jarandeshwar','Karad','Lonand','Malkapur','Masur','Murud','Nandgaon','Rahimatpur','Satara','Shenoli','Shirravde','Wathar','Agran','Dhulgaon','Arag','Bedag','Bolwad','Gulvanchi','Langarpeth','Dhalgaon','Jath Road','Kirloskarvadi','Madhavnagar','Miraj Junction','Nimblak','Ranjani','Belanki','Takari','Vishrambag')
c2.current()

l4=Label(text="ENTER DATE OF JOURNEY : ",fg="black",font=('Verdana',20))
l4.place(x=100,y=500)
c3=ttk.Combobox(root)
c3.place(x=535,y=510)
c3['values']=('1','2','3','4','5','6','7','8','9','10','11','12','113','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
c3.current()
c4=ttk.Combobox(root)
c4.place(x=690,y=510)
c4['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
c4.current()
c5=ttk.Combobox(root)
c5.place(x=840,y=510)
c5['values']=('2018')
c5.current()

l5=Label(text="ENTER E-MAIL ID: ",fg="black",font=('Verdana',20))
l5.place(x=100,y=600)
e5=Entry(width=30)
e5.place(x=575,y=610)

l6=Label(text="SELECT GENDER : ",fg="black",font=('Verdana',20))
l6.place(x=1100,y=200)
v=IntVar()
r1=Radiobutton(text="MALE",fg="green",variable=v,value=1,font=('Verdana',15))
r2=Radiobutton(text="FEMALE",fg="green",variable=v,value=2,font=('Verdana',15))
r3=Radiobutton(text="OTHER",fg="green",variable=v,value=3,font=('Verdana',15))
r1.place(x=1500,y=200)
r2.place(x=1600,y=200)
r3.place(x=1710,y=200)

l7=Label(text="ENTER TRAIN NUMBER : ",fg="black",font=('Verdana',20))
l7.place(x=1100,y=300)
e7=Entry(width=30)
e7.place(x=1500,y=310)

l8=Label(text="NUMBER OF TICKETS : ",fg="black",font=('Verdana',20))
l8.place(x=1100,y=400)
e8=Entry(width=30)
e8.place(x=1500,y=410)

l9=Label(text="ENTER PHONE NUMBER : ",fg="black",font=('Verdana',20))
l9.place(x=1100,y=500)
e9=Entry(width=30)
e9.place(x=1500,y=510)

l10=Label(text="ENTER ADDRESS : ",fg="black",font=('Verdana',20))
l10.place(x=1100,y=600)
e10=Entry(width=30)
e10.place(x=1500,y=610)

def reserved():
    phone=e9.get()
    if e1.get()=="":
        messagebox.showinfo("Title", "Please Enter Passenger Name")
    elif e5.get()=="":
        messagebox.showinfo("Title", "Please Enter E-mail Id")
    elif e7.get()=="":
        messagebox.showinfo("Title", "Please Enter Train Number")
    elif e8.get()=="":
        messagebox.showinfo("Title", "Please Enter Number Of Tickets")
    elif e9.get()=="":
        messagebox.showinfo("Title", "Please Enter Phone Number")
    elif e10.get()=="":
        messagebox.showinfo("Title", "Please Enter Address")
    elif c1.get()=="":
        messagebox.showinfo("Title", "Please Select Source")
    elif c2.get()=="":
        messagebox.showinfo("Title", "Please Select Destination")
    elif c3.get()=="":
        messagebox.showinfo("Title", "Please Select Date")
    elif c4.get()=="":
        messagebox.showinfo("Title", "Please Select Month")
    elif c5.get()=="":
        messagebox.showinfo("Title", "Please Select Year")
    elif re.match(r'[789]\d{9}$',phone):
        print("mobile number valid")                                    #linked another file
        os.system('python mail.py')
    else:  
        messagebox.showinfo("Title","please enter valid phone number")
                                                               
b1=Button(text="RESERVE",bd=10,fg="green",command=reserved,font=('Helvetica',15,'bold'))
b1.place(x=700,y=935)
b1.config( height=2, width=15)

def erase():                                                                    #for erasing text fields
    e1.delete(first=0,last=20)
    e5.delete(first=0,last=20)
    e7.delete(first=0,last=20)
    e8.delete(first=0,last=20)
    e9.delete(first=0,last=20)
    e10.delete(first=0,last=20)
    c1.delete(first=0,last=20)
    c2.delete(first=0,last=20)
    c3.delete(first=0,last=20)
    c4.delete(first=0,last=20)
    c5.delete(first=0,last=20)
    
b2=Button(text="RESET",bd=10,fg="red",command=erase,font=('Helvetica',15,'bold'))
b2.place(x=1100,y=935)
b2.config( height=2, width=15)

    
    








