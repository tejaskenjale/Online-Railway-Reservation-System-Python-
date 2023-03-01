import smtplib
import getpass
from tkinter import messagebox

sender="tejaskenjale17@gmail.com"
password="tejas@98"
recipient="tejaskenjale@rediffmail.com"
msg="YOUR ONLINE RESERVATION DONE SUCCESSFULLY "

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,recipient,msg)
messagebox.showinfo("Title", """Your Reservation Done Successfully
     Please Check Your E-mail""")           
server.quit()

