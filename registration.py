import tkinter as tk
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os

# import admin registration
# import Admin_form as admin_regis



window = tk.Tk()
w,h = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry("%dx%d"%(w,h))
window.title("REGISTRATION FORM")
window.configure(background="white")

Fullname = tk.StringVar()
address = tk.StringVar()
# username = tk.StringVar()
# Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
var1 = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT, category TEXT)")
db.commit()

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_reg"
               "(Name TEXT, Available_Vacancy_count  TEXT, Email_ID TEXT,Phoneno TEXT,Criateria TEXT)")
db.commit()


def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%', '!', '&', '*'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    # un = username.get()
    # email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()
    category = var1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE Phoneno = ?')
    # c.execute(find_user, [(username.get())])
    c.execute(find_user, [mobile])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$'
    # regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # if (re.search(regex, email)):
    #     a = True
    # else:
    #     a = False
        
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "Please Enter Valid Name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Valid Address")
    # elif (email == "") or (a == False):
    #     ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter Valid Mobile Number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter Valid Age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Mobile Number Already in Use.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter Valid Password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter Gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "Password must contain at least 1 uppercase letter, 1 symbol, 1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password do not match")
    elif (category == False):
        ms.showinfo("Message", "Please Select Category")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            
            if category == 2:
                cursor.execute(
                    'INSERT INTO admin_reg(Name, Phoneno, Address, Gender, password, age) VALUES(?,?,?,?,?,?)',
                    (fname, mobile, addr, gender, pwd, time))
            else:
                cursor.execute(
                    # 'INSERT INTO registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                    # (fname, addr, un, email, mobile, gender, time, pwd))
                    'INSERT INTO registration(Fullname, address, Phoneno, Gender, age , password, category) VALUES(?,?,?,?,?,?,?)',
                    (fname, addr, mobile, gender, time, pwd, category))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            window.destroy()

#####################################################################################################################################################

#from subprocess import call
#call(["python", "lecture_login.py"])


# assign and define variable
# def login():

#####For background Image
# image2 =Image.open('new2.jpg')
# image2 =image2.resize((200,200), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)

# background_label = tk.Label(window, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

frame = Frame(window, width=500, height=200, borderwidth=0, highlightthickness=0)
frame.pack()
frame.place(anchor='center', relx=0.3, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("regis.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

frame = tk.LabelFrame(window, text="", width=600, height=625, bd=5, font=('times', 14, ' bold '),bg="skyblue")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=700, y=110)



lbl = tk.Label(window, text="Registration Form", font=('times', 35,' bold '), height=2, width=50,bg="white",fg="black")
lbl.place(x=75, y=0)



#l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="blue4", fg="red")
#l1.place(x=490, y=40)

# that is for label1 registration

l2 = tk.Label(frame, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue",bd=5)
l2.place(x=30, y=30)
t1 = tk.Entry(frame, textvar=Fullname, width=20, font=('', 15),bd=5)
t1.config(borderwidth = 0)
t1.place(x=230, y=30)
# that is for label 2 (full name)






l3 = tk.Label(frame, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue",bd=5)
l3.place(x=30, y=80)
t2 = tk.Entry(frame, textvar=address, width=20, font=('', 15),bd=5)
t2.config(borderwidth = 0)
t2.place(x=230, y=80)
# that is for label 3(address)


# that is for label 4(blood group)

#l5 = tk.Label(frame, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
#l5.place(x=30, y=130)
#t4 = tk.Entry(frame, textvar=Email, width=20, font=('', 15),bd=5)
#t4.place(x=230, y=130)
# that is for email address

l6 = tk.Label(frame, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
l6.place(x=30, y=130)
t5 = tk.Entry(frame, textvar=Phoneno, width=20, font=('', 15),bd=5)
t5.config(borderwidth = 0)
t5.place(x=230, y=130)
# phone number
l7 = tk.Label(frame, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
l7.place(x=30, y=180)
# gender
tk.Radiobutton(frame, text="Male", padx=5, width=5, bg="skyblue", font=("bold", 15), variable=var, value=1).place(x=230,
                                                                                                                y=180)
tk.Radiobutton(frame, text="Female", padx=20, width=4, bg="skyblue", font=("bold", 15), variable=var, value=2).place(
    x=340, y=180)

l8 = tk.Label(frame, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
l8.place(x=30, y=230)
t6 = tk.Entry(frame, textvar=age, width=20, font=('', 15),bd=5)
t6.config(borderwidth = 0)
t6.place(x=230, y=230)

#l4 = tk.Label(frame, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="lightgreen")
#l4.place(x=30, y=330)
#t3 = tk.Entry(frame, textvar=username, width=20, font=('', 15),bd=5)
#t3.place(x=230, y=330)

l9 = tk.Label(frame, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
l9.place(x=30, y=280)
t9 = tk.Entry(frame, textvar=password, width=20, font=('', 15), show="*",bd=5)
t9.config(borderwidth = 0)
t9.place(x=230, y=280)

l10 = tk.Label(frame, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"), bg="skyblue")
l10.place(x=30, y=330)

t10 = tk.Entry(frame, textvar=password1, width=20, font=('', 15), show="*",bd=5)
t10.config(borderwidth = 0)
t10.place(x=230, y=330)

# login-type
l11 = tk.Label(frame, text="Category :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
l11.place(x=30, y=370)
# login type
tk.Radiobutton(frame, text="Worker", padx=5, width=5, bg="skyblue", font=("bold", 15), variable=var1, value=1).place(x=230,
                                                                                                                y=370)
tk.Radiobutton(frame, text="Contractor", padx=20, width=4, bg="skyblue", font=("bold", 15), variable=var1, value=2).place(
    x=340, y=370)

btn = tk.Button(frame, text="Register", bg="grey",font=("",20),fg="white", width=9, height=1, command=insert,bd=5)
btn.place(x=230, y=460)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)



window.mainloop()