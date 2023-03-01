from tkinter import *
from tkinter import messagebox
import os
import sqlite3
import re
from tkinter import ttk
import time
import smtplib
import getpass
from prettytable import PrettyTable

root=Tk()
root.title("first page")
root.config(background="orange")


img1=PhotoImage(file="E:\python\\bvplogo.gif")
logo=Label(root,bd=0,image=img1)
logo.config(height=150,width=350)
logo.place(x=750,y=850)

frame1=Frame(root,width=1400,height=100,bg="white",bd=5)
frame1.pack(side=TOP)
frame1.config(background='white')
lab1=Label(frame1,text="सोनहिरा रेल प्रवासी आरक्षण  ",fg='blue',bg='orange',font=('times new roman',50,'bold'),bd=20,width=41,justify='center')
lab1.grid(row=0,column=0)

frame2=Frame(root,width=600,height=400,bd=5,bg="orange",relief="raise")
frame2.place(x=7,y=600)

lab3=Label(frame2,text="Login",fg='white',bg='blue',font=('times new roman',20),width=39,relief="raise")
lab3.place(x=0,y=0)

nameL1 = Label(frame2, text='Username :- ',fg='blue',bg='orange',font=('times new roman',15)) 
pwordL1 = Label(frame2, text='Password :- ',fg='blue',bg='orange',font=('times new roman',15)) 
nameL1.place(x=10,y=70)
pwordL1.place(x=10,y=120) 
 
nameE1 = Entry(frame2) 
pwordE1 = Entry(frame2, show='*') 
nameE1.place(x=180,y=70) 
pwordE1.place(x=180,y=120)




def login():
    us=nameE1.get()
    pa=pwordE1.get()
    conn=sqlite3.connect('logindetails.db')
    c= conn.cursor()
    find="select * from login where user='%s' and password='%s';"%(us,pa)
    c.execute(find)
    result=c.fetchall()
    if result:
        messagebox.showinfo("Title","Your login done successfully")
        root1=Tk()
        root1.title("आरक्षण अर्ज ")
        root1.config(background="orange")

        top2=Frame(root1,width=1350,height=100,bd=14,bg="orange",relief="raise")
        top2.pack(side=TOP)
        l11=Label(top2,text="Railway Reservation Form ",fg='blue',bg='orange',font=('algerian',50),bd=10,width=41,justify='center')
        l11.grid(row=0,column=0)

        bottom=Frame(root1,bg="orange",width=1910,height=150,bd=14,relief="raise")
        bottom.pack(side=BOTTOM)

        left=Frame(root1,bg="orange",width=1000,height=800,bd=14,relief="raise")
        left.pack(side=LEFT)

        right=Frame(root1,bg="orange",width=1000,height=800,bd=14,relief="raise")
        right.pack(side=RIGHT)


        l1=Label(root1,text="ENTER PASSENGER NAME : ",fg='blue',bg='orange',font=('Verdana',20))
        l1.place(x=100,y=200)
        e1=Entry(root1,width=30)
        e1.place(x=575,y=210)

        l2=Label(root1,text="ENTER THE SOURCE : ",fg='blue',bg='orange',font=('Verdana',20))
        l2.place(x=100,y=300)
        c1=ttk.Combobox(root1)
        c1.place(x=575,y=310)
        c1['values']=('Ahmadnagar','Akolner','Belvandi','Bhandewadi Halt','Chitali','Dahegaon','Kanhegaon','Kashti','Kedgaon','Kopargaon','Nipani Vadgaon','Padhegaon','Pargaon Sudrik','Puntamba','Rahuri','Sanvatsar','Shrigonda Road','Vadala Road Bby','Vambori','Vilad','Adarki','Ambale','Jarandeshwar','Karad','Lonand','Malkapur','Masur','Murud','Nandgaon','Rahimatpur','Satara','Shenoli','Shirravde','Wathar','Agran','Dhulgaon','Arag','Bedag','Bolwad','Gulvanchi','Langarpeth','Dhalgaon','Jath Road','Kirloskarvadi','Madhavnagar','Miraj Junction','Nimblak','Ranjani','Belanki','Takari','Vishrambag')
        c1.current()

        l3=Label(root1,text="ENTER THE DESTINATION : ",fg='blue',bg='orange',font=('Verdana',20))
        l3.place(x=100,y=400)
        c2=ttk.Combobox(root1)
        c2.place(x=575,y=410)
        c2['values']=('Ahmadnagar','Akolner','Belvandi','Bhandewadi Halt','Chitali','Dahegaon','Kanhegaon','Kashti','Kedgaon','Kopargaon','Nipani Vadgaon','Padhegaon','Pargaon Sudrik','Puntamba','Rahuri','Sanvatsar','Shrigonda Road','Vadala Road Bby','Vambori','Vilad','Adarki','Ambale','Jarandeshwar','Karad','Lonand','Malkapur','Masur','Murud','Nandgaon','Rahimatpur','Satara','Shenoli','Shirravde','Wathar','Agran','Dhulgaon','Arag','Bedag','Bolwad','Gulvanchi','Langarpeth','Dhalgaon','Jath Road','Kirloskarvadi','Madhavnagar','Miraj Junction','Nimblak','Ranjani','Belanki','Takari','Vishrambag')
        c2.current()

        l4=Label(root1,text="ENTER DATE OF JOURNEY : ",fg='blue',bg='orange',font=('Verdana',20))
        l4.place(x=100,y=500)
        c3=ttk.Combobox(root1)
        c3.place(x=535,y=510)
        c3['values']=('1','2','3','4','5','6','7','8','9','10','11','12','113','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        c3.current()
        c4=ttk.Combobox(root1)
        c4.place(x=690,y=510)
        c4['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
        c4.current()
        c5=ttk.Combobox(root1)
        c5.place(x=840,y=510)
        c5['values']=('2018')
        c5.current()

        l5=Label(root1,text="ENTER E-MAIL ID: ",fg='blue',bg='orange',font=('Verdana',20))
        l5.place(x=100,y=600)
        e5=Entry(root1,width=30)
        e5.place(x=575,y=610)

        l6=Label(root1,text="SELECT GENDER : ",fg='blue',bg='orange',font=('Verdana',20))
        l6.place(x=1100,y=200)
        v=IntVar()
        r1=Radiobutton(root1,text="MALE",fg="green",bg="orange",variable=v,value="male",font=('Verdana',15))
        r2=Radiobutton(root1,text="FEMALE",fg="green",bg="orange",variable=v,value="female",font=('Verdana',15))
        r3=Radiobutton(root1,text="OTHER",fg="green",bg="orange",variable=v,value="other",font=('Verdana',15))
        r1.place(x=1500,y=200)
        r2.place(x=1600,y=200)
        r3.place(x=1710,y=200)

        l7=Label(root1,text="ENTER TRAIN NUMBER : ",fg='blue',bg='orange',font=('Verdana',20))
        l7.place(x=1100,y=300)
        e7=Entry(root1,width=30)
        e7.place(x=1500,y=310)

        l8=Label(root1,text="NUMBER OF TICKETS : ",fg='blue',bg='orange',font=('Verdana',20))
        l8.place(x=1100,y=400)
        e8=Entry(root1,width=30)
        e8.place(x=1500,y=410)

        l9=Label(root1,text="ENTER PHONE NUMBER : ",fg='blue',bg='orange',font=('Verdana',20))
        l9.place(x=1100,y=500)
        e9=Entry(root1,width=30)
        e9.place(x=1500,y=510)

        l10=Label(root1,text="ENTER ADDRESS : ",fg='blue',bg='orange',font=('Verdana',20))
        l10.place(x=1100,y=600)
        e10=Entry(root1,width=30)
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
            else:  
                messagebox.showinfo("Title","please enter valid phone number")
            conn=sqlite3.connect('logindetails.db')
            c= conn.cursor()
            save="update login set name='%s',source='%s',destination='%s',date='%s',month='%s',year='%s',email='%s',gender='%s',train_no='%s',ticket_no='%s',phone='%s',address='%s' where user='%s';"%(e1.get(),c1.get(),c2.get(),c3.get(),c4.get(),c5.get(),e5.get(),v.get(),e7.get(),e8.get(),e9.get(),e10.get(),nameE1.get())
            c.execute(save)
            conn.commit()
            conn.close()
            
            sender="tejaskenjale17@gmail.com"
            password="tejas@98"
            rec=str(e5.get())
            recipient=rec
            msg="YOUR ONLINE RESERVATION DONE SUCCESSFULLY "

            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(sender,password)
            server.sendmail(sender,recipient,msg)
            messagebox.showinfo("Title", """Your Reservation Done Successfully
                     Please Check Your E-mail""")
            server.quit()
            
        b1=Button(root1,text="RESERVE",bd=10,fg="green",bg="orange",command=reserved,font=('Helvetica',15,'bold'))
        b1.place(x=700,y=930)
        b1.config(height=2, width=15)

        can=Label(left,text="For Cancellation Of Reservation Click Here  ",fg='red',bg='orange',font=('Verdana',20))
        can.place(x=15,y=600)

        def cancel():
            can=Tk()
            can.title("आरक्षण रद्द अर्ज ")
            can.config(background="orange")

            x = PrettyTable()
            x.field_names = ["name", "source", "destination","date", "month", "year","email", "gender", "train no","no. of tickets", "phone", "address"]
            show=Label(can,text="name\tsource\t\tdestination\tdate\tmonth\tyear\temail\tgender\ttrain no\tno. of tickets\tphone\taddress",fg='red',bg='orange',font=('Verdana',15))
            show.place(x=15,y=300)

            x.add_row([e1.get(),c1.get(),c2.get(),c3.get(),c4.get(),c5.get(),e5.get(),v.get(),e7.get(),e8.get(),e9.get(),e10.get()])
            
            print(x)
            details=str(e1.get()+"\t"+c1.get()+"\t"+c2.get()+"\t"+str(c3.get())+"\t"+c4.get()+"\t"+str(c5.get())+"\t"+e5.get()+"\t"+str(v.get())+"\t"+str(e7.get())+"\t"+str(e8.get())+"\t"+str(e9.get())+"\t"+e10.get())
            show1=Label(can,text=details,fg='red',bg='orange',font=('Verdana',15))
            show1.place(x=15,y=550)

            def cancel1():
                conn=sqlite3.connect('logindetails.db')
                c= conn.cursor()
                c.execute("delete from login where user='%s'"%(nameE1.get()))
                messagebox.showinfo("Title","cancellation of reservation successful")
                conn.commit()
                conn.close()

                
            ca1=Button(can,text="CANCEL",bd=10,fg="red",bg="orange",command=cancel1,font=('Helvetica',15,'bold'))   
            ca1.place(x=100,y=600)
            ca1.config(height=2, width=15)
                
            
        

        ca=Button(left,text="CANCEL",bd=10,fg="red",bg="orange",command=cancel,font=('Helvetica',15,'bold'))   
        ca.place(x=650,y=585)
        ca.config(height=2, width=15)

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
    
        b2=Button(root1,text="RESET",bd=10,fg="red",bg="orange",command=erase,font=('Helvetica',15,'bold'))
        b2.place(x=1100,y=930)
        b2.config( height=2, width=15)
        
    else:
        messagebox.showinfo("Title","invalid username or password")
    

        

    
    
    

login = Button(frame2, text='Log In',command=login,font=('Helvetica',15,'bold')) 
photo1=PhotoImage(file="E:\python\loginbutton.png")
login.config(image=photo1,width="150",height="40")
login.place(x=150,y=200)



frame3=Frame(root,width=600,height=400,bd=5,bg="orange",relief="raise")
frame3.place(x=1350,y=600)

lab2=Label(frame3,text="Sign Up ",fg='white',bg='blue',font=('times new roman',20),width=39,relief="raise")
lab2.place(x=0,y=0)

nameL = Label(frame3, text='New Username :- ',fg='blue',bg='orange',font=('times new roman',15)) 
pwordL = Label(frame3, text='New Password :- ',fg='blue',bg='orange',font=('times new roman',15)) 
nameL.place(x=10,y=70)
pwordL.place(x=10,y=120) 
 
nameE = Entry(frame3) 
pwordE = Entry(frame3, show='*') 
nameE.place(x=180,y=70) 
pwordE.place(x=180,y=120)


def save():
    conn=sqlite3.connect('logindetails.db')
    c= conn.cursor()
    sql = "insert into login(user,password)values('%s','%s');"%(nameE.get(),pwordE.get())
    c.execute(sql)
    print("success")
    conn.commit()
    messagebox.showinfo("Title","Your data has been saved successfully")
    conn.close()


signupbutton = Button(frame3, text='Sign In',command=save,font=('Helvetica',15,'bold')) 
photo=PhotoImage(file="E:\python\save_button.png")
signupbutton.config(image=photo,width="150",height="40")
signupbutton.place(x=150,y=200)

img2=PhotoImage(file="E:\python\\banner.gif")
label4=Label(root,bd=1,bg="white",image=img2,relief="raise")
label4.config(width=1000,height=450)
label4.place(x=500,y=150)


text = Text(root, width=20, height=1, bg='orange')
text.place(x=750,y=750)
text.config(fg="blue",font=('courier', 24, 'bold'))
s1 = "सोनहिरा रेल प्रवासी आरक्षण मध्ये आपले सहर्ष स्वागत आहे "
s2 = ' ' * 10
s = s2 + s1 + s2
for k in range(len(s)):
    # use string slicing to do the trick
    ticker_text = s[k:k+50]
    text.insert("1.1", ticker_text)
    root.update()
    # delay by 0.15 seconds
    time.sleep(0.15)




