from tkinter import *
import tkinter.scrolledtext as tkst
import sqlite3
window = Tk()
conn = sqlite3.connect('contacts.db')
curs = conn.cursor()
conn.execute("CREATE TABLE IF NOT EXISTS CONTACT(NAME VARCHAR(100),NUMBER varchar(10));")
print("Table created")
conn.close()
def load_contact():
    cont.delete('1.0', END)
    cont.insert(END,"NAME\t|\tNUMBER")
    con = sqlite3.connect('contacts.db')
    cus = con.cursor()
    cus.execute("select * from contact")
    data=cus.fetchall()
    for i in data:
        st=str(i[1]+"\t\t"+i[0])
        cont.insert(END,"\n"+st)
def do_insert():
    conn = sqlite3.connect('contacts.db')
    curs = conn.cursor()
    print("insert")
    sql = "insert into contact (name,number) values ('%s','%s');"%(number.get(),name.get())
    curs.execute(sql)
    conn.commit()
    txt_result.config(text="Successfully inserted the data", fg="red")
    conn.close()
    load_contact()
def do_update():
    con = sqlite3.connect('contacts.db')
    cur = con.cursor()
    print("update")
    sql1 = "update contact set name = '%s' where number = '%s';"%(name1.get(),number1.get())
    cur.execute("update contact set name = '%s' where number = '%s';"%(name1.get(),number1.get()))
    con.commit()
    txt_result.config(text="Successfully updated the data", fg="brown")
    con.close()
    load_contact()

def do_fetch():    
    conne = sqlite3.connect('contacts.db')
    cur = conne.cursor()    
    sql = "select * from contact where name = '%s'"%(number1.get())
    cur.execute(sql)
    name = cur.fetchone()
    print(name)
    nameVar.set(name[1])
    print("fetch")
    txt_result.config(text="Successfully fetched the data", fg="blue")
    conne.commit()
    conne.close()

def do_delete():
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    cur.execute("DELETE FROM contact WHERE number = ?", (number1.get(),))
    con.commit()
    con.close()   
    txt_result.config(text="Successfully deleted the data", fg="green")
    load_contact()


fnt = ('Times',22,'bold italic underline')
l = Label(window, text="Contacts Manager", fg="red",font=fnt)
l.grid(row=0, column=1)

l = Label(window, text="  ")
l.grid(row=1, column=1)

l = Label(window, text="Phone Number:")
l.grid(row=2, column=0)    
number = Entry(window)
number.grid(row=2, column=1)    


l = Label(window, text="Name:")
l.grid(row=3, column=0)   
name = Entry(window)
name.grid(row=3, column=1)

window.title('Conatcts Manager')
submitbtn = Button(window, text="Add contact", command=do_insert)
submitbtn.grid(row=7, column=1)

l = Label(window, text="Enter number to search:")
l.grid(row=9, column=0)    
number1 = Entry(window)
number1.grid(row=9, column=1)

submitbtn = Button(window, text="Search", command=do_fetch)
submitbtn.grid(row=10, column=1)

nameVar = StringVar()
l = Label(window, text="Name:")
l.grid(row=12, column=0)   
name1 = Entry(window,textvariable=nameVar)
name1.grid(row=12, column=1)


submitbtn = Button(window, text="Update Data", command=do_update)
submitbtn.grid(row=13, column=1)

submitbtn = Button(window, text="Delete", command=do_delete)
submitbtn.grid(row=13, column=2)

txt = Label(window,text="Message: ")
txt.grid(row=14, column=0)
txt_result = Label(window,text=" ")
txt_result.grid(row=14, column=1)

cont=tkst.ScrolledText(width=30,height=5)
cont.grid(row=15, column=0)

load_contact()
window.mainloop()
