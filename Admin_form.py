import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
from tkinter import ttk


window = tk.Tk()
w,h = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry("%dx%d+0+0"%(w,h))
window.title("ADMIN FORM")
window.configure(background="skyblue")

Name = tk.StringVar()
Available_Vacancy_count  = tk.IntVar()
Location = tk.StringVar()
Phoneno = tk.IntVar()
Criateria = tk.StringVar()


value = random.randint(1, 1000)
# print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS jobs"
               "(Name TEXT, Available_Vacancy_count TEXT, Phoneno TEXT, Location TEXT Criateria TEXT)")
db.commit()



def insert():
    Name1 = Name.get()
    Available_Vacancy_count1 =  Available_Vacancy_count.get()
    Location1 = Location.get()
    Phoneno1 = Phoneno.get()
    Criateria1 = Criateria.get()
   

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    
    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    # regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # if (re.search(regex, Email_ID1)):
    #     a = True
    # else:
    #     a = False
    # validation
    if (Name1.isdigit() or (Name1 == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (Available_Vacancy_count1 == ""):
        ms.showinfo("Message", "Please Enter Available_Vacancy")
    # elif (Email_ID1 == "") or (a == False):
    #     ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(Phoneno1)))<10 or len(str((Phoneno1)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif (Criateria1 == ""):
        ms.showinfo("Message", "Please Enter Criteria")
  

    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO jobs(Name, Available_Vacancy_count, Phoneno, Location, Criateria ) VALUES(?,?,?,?,?)',
                (Name1, Available_Vacancy_count1,Phoneno1, Location1, Criateria1))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'All Data Submit Successfully !')
            # window.destroy()
            window.destroy()

#####################################################################################################################################################

#from subprocess import call
#call(["python", "lecture_login.py"])


# assign and define variable
# def login():

#####For background Image
image2 =Image.open('new2.jpg')
image2 =image2.resize((2010,990), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=-20, y=0) #, relwidth=1, relheight=1)

frame = tk.LabelFrame(window, text="", width=600, height=570, bd=5, font=('times', 14, ' bold '),bg="antiquewhite2")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=10, y=120) # x = 470

lbl = tk.Label(window, text="Create Job", font=('times', 35,' bold '), height=2, width=55,bg="skyblue",fg="red")
lbl.place(x=0, y=0)



#l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="blue4", fg="red")
#l1.place(x=490, y=40)

# that is for label1 registration

l2 = tk.Label(frame, text="Name :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2",bd=5)
l2.place(x=30, y=30)
t1 = tk.Entry(frame, textvar=Name, width=20, font=('', 15),bd=5)
t1.place(x=230, y=30)
# that is for label 2 (full name)






l3 = tk.Label(frame, text="Available Vacancy :", width=13, font=("Times new roman", 15, "bold"), bg="antiquewhite2",bd=5)
l3.place(x=30, y=80)
t2 = tk.Entry(frame, textvar=Available_Vacancy_count, width=20, font=('', 15),bd=5)
t2.place(x=230, y=80)
# that is for label 3(address)


# that is for label 4(blood group)

# that is for email address

l6 = tk.Label(frame, text="Phone Number:", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l6.place(x=30, y=130)
t5 = tk.Entry(frame, textvar=Phoneno, width=20, font=('', 15),bd=5)
t5.place(x=230, y=130)


l5 = tk.Label(frame, text="Location :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l5.place(x=30, y=180)
t4 = tk.Entry(frame, textvar=Location, width=20, font=('', 15),bd=5)
t4.place(x=230, y=180)

l8 = tk.Label(frame, text="Criteria", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
l8.place(x=30, y=230)
monthchoosen = ttk.Combobox(frame, width = 27,textvariable = Criateria)
monthchoosen['values'] = ('Plumber', 
                          'Chef',
                          'Electriction')
monthchoosen.place(x=230,y=230)



btn = tk.Button(frame, text="Submit", bg="red",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=230, y=380)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()