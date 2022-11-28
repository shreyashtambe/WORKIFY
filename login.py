# Imports
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox as ms


# main Class
class main:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        # self.username = tk.StringVar()
        # self.Phoneno = tk.StringVar()
        self.Phoneno = tk.StringVar()
        self.password = tk.StringVar()
        self.var1 = tk.IntVar()
        # self.n_username = tk.StringVar()
        # self.n_Phoneno = tk.StringVar()
        # self.n_password = tk.StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection

        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

            # Find user If there is any take proper action
            db = sqlite3.connect('evaluation.db')
            cursor = db.cursor()
            
            # print(self.var1.get())
            
            if(self.var1.get() == 1):
                # print("========= WORKER ===========")
                find_entry = ('SELECT * FROM registration WHERE Phoneno = ? AND password = ?')
                c.execute(find_entry, [(self.Phoneno.get()), (self.password.get())])
                result = c.fetchall()
                # print(result)
                if result:
                    msg = ""
                    self.logf.pack_forget()
                    # self.head['text'] = self.Phoneno.get() + '\n Loged In'
                    # msg = self.head['text']
                    # self.head['pady'] = 150
                    # print(msg)
                    ms.showinfo("messege", "LogIn sucessfully")
                    # ===========================================
                    # root.destroy()
        
                    from subprocess import call
                    call(['python','job_recom.py'])
                    
                    root.destroy()
        
                    # ================================================
                else:
                    ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')
                
            if(self.var1.get() == 2):
                # print("========= CONTRACTOR =========")
                find_entry = ('SELECT * FROM admin_reg WHERE Phoneno = ? AND password = ?')
                c.execute(find_entry, [(self.Phoneno.get()), (self.password.get())])
                result = c.fetchall()
                # print(result)
                if result:
                    # msg = ""
                    # self.logf.pack_forget()
                    # self.head['text'] = self.Phoneno.get() + '\n Loged In'
                    # msg = self.head['text']
                    # self.head['pady'] = 150
                    # print(msg)
                    ms.showinfo("messege", "LogIn sucessfully")
                    # ===========================================
                    root.destroy()
        
                    from subprocess import call
                    call(['python','Admin_form.py'])
        
                    # ================================================
                else:
                    ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')
            
            # cursor.execute("CREATE TABLE IF NOT EXISTS registration"
            #                "(Fullname TEXT, address TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT, category TEXT)")
            # cursor.execute("CREATE TABLE IF NOT EXISTS admin_reg"
            #                 "(Name TEXT, Phoneno TEXT, Address TEXT, Gender TEXT, password TEXT, age TEXT)")
            # db.commit()
            # find_entry = ('SELECT * FROM admin_reg WHERE Phoneno = ? AND password = ?')
            # find_entry = ('SELECT * FROM admin_reg WHERE Phoneno=1234566666 AND password=Sharan@1')
            
            # c.execute(find_entry, [(self.Phoneno.get()), (self.password.get())])
            # c.execute(find_entry, [("1234566666"), ('Sharan@1')])
            
            # result = c.fetchall()
            # print(result)
            # if result:
            #     msg = ""
            #     # self.logf.pack_forget()
            #     # self.head['text'] = self.username.get() + '\n Loged In'
            #     # msg = self.head['text']
            #     #            self.head['pady'] = 150
            #     print(msg)
            #     ms.showinfo("messege", "LogIn sucessfully")
            #     # ===========================================
            #     root.destroy()
    
            #     from subprocess import call
            #     call(['python','job_recom.py'])
    
            #     # ================================================
            # else:
            #     ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created Successfully !')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def registration(self):
        root.destroy()
        from subprocess import call
        call(["python", "registration.py"])

        # mainloop(root)

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

 # , relwidth=1, relheight=1)

    # Draw Widgets
    def widgets(self):
        
        # ========= ORIGINAL CODE =========
        
        # self.head = tk.Label(self.master, text='Welcome To Login', background="White", font=('Times New Roman', 20),
        #                       pady=20)
        # self.head.pack()

        # # self.head.pack()
        # # self.head = Label(self.master, text='LOGIN',background="gold", font=('Times New Roman', 35), pady=10)
        # # self.head.pack()
        
        self.logf = tk.Frame(self.master, padx=50, pady=70, background="Sky Blue")
        
        # tk.Label(self.logf, text='Username: ', background="Sky Blue", font=("Times New Roman", 20), pady=5,
        #           padx=5).grid(sticky=tk.W)
        # tk.Entry(self.logf, textvariable=self.username, bd=5, background="white", font=('', 15)).grid(row=0, column=1)
        # tk.Label(self.logf, text='Password: ', background="Sky Blue", font=("Times New Roman", 20), pady=5,
        #           padx=5).grid(sticky=tk.W)
        # tk.Entry(self.logf, textvariable=self.password, bd=5, background="white", font=('', 15), show='*').grid(row=1,column=1)
        # tk.Button(self.logf, text=' Login ', command=self.login, bd=2, font=("Times New Roman", 20), background="Red",
        #           foreground="white", padx=2, pady=2)
        
        # self.logf.pack()
        # self.crf = tk.Frame(self.master, padx=200, pady=200)
        
        
        
        # ========= EDITED CODE =========
        
        frame = tk.LabelFrame(root, text="", width=490, height=250, bd=5, font=('times', 14, ' bold '),bg="Sky Blue")
        
        self.password = tk.StringVar()
        self.Phoneno = tk.StringVar()
        self.var1 = tk.IntVar()
        frame.place(x=525, y=280)

        lbl = tk.Label(root, text="Welcome To Login", font=('times', 35,' bold '), height=2, width=50,bg="skyblue",fg="black")
        lbl.place(x=75, y=0)



        #l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="blue4", fg="red")
        #l1.place(x=490, y=40)

        # that is for label1 registration

        
        l4 = tk.Label(frame, text="Mobile Number :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
        l4.place(x=15, y=30)
        t3 = tk.Entry(frame, textvar=self.Phoneno, width=20, font=('', 15),bd=5)
        t3.place(x=200, y=30)

        l9 = tk.Label(frame, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
        l9.place(x=15, y=80)
        t9 = tk.Entry(frame, textvar=self.password, width=20, font=('', 15), show="*",bd=5)
        t9.place(x=200, y=80)
        
        # login-type
        l11 = tk.Label(frame, text="Category :", width=12, font=("Times new roman", 15, "bold"), bg="skyblue")
        l11.place(x=15, y=130)
        # login type
        tk.Radiobutton(frame, text="Worker", padx=5, width=5, bg="skyblue", font=("bold", 15), variable=self.var1, value=1).place(x=200,
                                                                                                                        y=130)
        tk.Radiobutton(frame, text="Contractor", padx=20, width=4, bg="skyblue", font=("bold", 15), variable=self.var1, value=2).place(
            x=325, y=130)
                
        btn = tk.Button(frame, text="Login", bg="grey",font=("",16),fg="white", width=10, height=1, command=self.login,bd=3)
        btn.place(x=170, y=180)
        
        
        

        


root = tk.Tk()

root.configure(background="Sky Blue")
root.geometry("2010x990")
root.title("Login")

#image2 = Image.open('logimg1.jpg')
#image2 = image2.resize((500, 500), Image.ANTIALIAS)

#background_image = ImageTk.PhotoImage(image2)

#background_label = tk.Label(root, image=background_image)

#background_label.image = background_image

#background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("A1.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()


main(root)

root.mainloop()
