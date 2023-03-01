"""*****************************************************************************
                            MODULES USED IN PROJECT
*****************************************************************************"""
 
import pickle
import os
import random
import time
"""*****************************************************************************
                            FUNCTIONS USED IN PROJECT
*****************************************************************************"""
def pass_details():                  # passenger details
        name=str(input("\n\nEnter passenger name:"))
        print("\n\nJOURNEY FROM:")
        fstat=str(input("\n\n SOURCE:"))
        tstat=str(input("\n\n DESTINATION:"))
        doj=input("\n\nENTER DATE OF JOURNEY:")
        gender=str(input("MALE/FEMALE :"))
        tno=input("TRAIN NUMBER:")
        no_tic=input("enter number of tickets:")
        add=input("enter the phone number :")
                                                #generating random pnr number and file names
        a=('pnr'+name)
        
        f=open(a+".dat","w")                             # writing passenger details to different files 
                                         
                                                
                                               
        print (">>>>>>>>>>>>>>TICKET RESERVED <<<<<<<<<<<<<<<<<")
        c=random.randint(10000,99999)
                                        
        print ("your pnr no is",c)
        f.write(name)
        f.write('\n')
        f.write(fstat)
        f.write('\n')
        f.write(tstat)
        f.write('\n')
        f.write(doj)
        f.write('\n')
        f.write(gender)
        f.write('\n')
        f.write(tno)
        f.write('\n')
        f.write(no_tic)
        f.write('\n')
        f.write(add)
        f.write('\n')
        
        f.close()
def cancel():
        zx=str(input("Name of the passenger:"))
        zz=int(input("PNR number:"))
        os.remove('pnr'+zx+'.dat')
def display_passdetails():
        try:
                z=str(input("ENTER YOUR NAME : "))
                X=int(input("ENTER PNR number :"))
                ra=random.randint(1,99)
                f2=open('pnr'+z+'.dat',"r")
                str1=f2.readline()
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TK RAILWAYS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("                           arrival time : 11:55            departure time : 13:11")
                print ("                           seat no:",ra)
                print ("                           class : 2AC")
                print ("Name:",str1)                                                             
                str2=f2.readline()
                print ("Journey from station:",str2)
                str3=f2.readline()
                print ("To Station:",str3)
                str4=f2.readline()
                print ("DATE OF JOURNEY : ",str4)
                str5=f2.readline()
                print ("GENDER :",str5)
                str6=f2.readline()
                print ("TRAIN NUMBER :",str6)
                str7=f2.readline()
                print ("NUMBER OF TICKETS :",str7)
                str8=f2.readline()
                print ("PHONE NUMBER :",str8)
                
                
      
                print ("~~~~~~~~~~~~~~~~~~~~~~~HAPPY JOURNEY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except (FileNotFoundError, IOError):
                print("भावा गंडलास तू......")  
  
"""*****************************************************************************
                         INTRODUCTORY FUNCTION
*****************************************************************************"""
        
 
def intro():
    print ("\n\tRAILWAY RESERVATION SYSTEM")
    print ("\n\n\nMADE BY : TEJAS KENJALE ")
    print ("\nCOLLEGE : BHARATI VIDYAPEETH COLLEGE OF ENGINEERING,KHARGHAR")
 
 
 
"""*****************************************************************************
                        THE MAIN FUNCTION OF PROGRAM
*****************************************************************************"""
intro()
time.sleep(2)
a="TKRAILWAYS"
while a=="TKRAILWAYS":
        time.sleep(2)
        print("_______________________________________________________________________")
        print (         """MAIN MENU
             1. Passenger's DETAILS
             2. Passenger's reserved TICKET
             3. CANCEL Ticket
             4. EXIT
                """)
        ch=int(input("Enter Your Choice(1~4): "))
        if ch==1:
                pass_details()
        elif ch==2:
                display_passdetails()
        elif ch==3:
                cancel()
        elif ch==4:
                break
        else:
                print("Input correcr choice...(1-4)")
input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")
 
"""*****************************************************************************
                END OF PROJECT
*****************************************************************************"""
