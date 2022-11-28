# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:52:22 2021

@author: srcdo
"""

import os
from gtts import gTTS
from translate import Translator
from PIL import Image , ImageTk   
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import * 
# import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image 
from tkinter import messagebox as ms
##############################################+=============================================================

root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Google Map Route")


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('lang.png')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

c=StringVar()
c1=StringVar()
data=StringVar()


lbl = tk.Label(root, text="Map Display", font=('times', 40,' bold '), height=1, width=30,bg="lightblue2",fg="indian red")
lbl.place(x=230, y=10)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=680, height=300, bd=5, font=('times', 15, ' bold '),bg="lightblue1")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=30, y=180)

frame_alpr1 = tk.LabelFrame(root, text=" --Display Map-- ", width=300, height=300, bd=5, font=('times', 15, ' bold '),bg="indian red")
frame_alpr1.grid(row=0, column=0, sticky='nw')
frame_alpr1.place(x=730, y=180)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def translate(): 
    import gmplot
    Lang1=c.get()
    print(Lang1)
    
    if Lang1 == 'Kasarwadi-Dapodi-Bopodi-Khadki-Sancheti-Shivaji_Nagar':
        ms.showinfo( "Route", "Found Route is \nKasarwadi-Dapodi-Bopodi-Khadki-Sancheti-Shivaji_Nagar")
        print("route1 Found")
        lat1 = [18.606088 , 18.585293 ]
        lang1 = [73.822791, 73.833217]
        lat2 = [18.585293 , 18.571487]
        lang2 = [73.833217, 73.837311]
        lat3 = [18.571487,18.554131]
        lang3 = [73.837311,73.848334]
        lat4 = [18.554131, 18.530749]
        lang4 = [73.848334, 73.854635]
        lat5 = [18.53082,18.53082]
        lang5 = [73.847464,73.847464]
        gmapOne = gmplot.GoogleMapPlotter(18.516726, 73.856255, 15 )
        gmapOne.scatter(lat1,lang1,'green', size=50, marker=True , symbol='Source')
        # gmapOne.plot(lat1,lang1,'green',edge_width=5.5)
        gmapOne.scatter(lat2,lang2,'green', size=50, marker=True , symbol='Intermediate 1')
        # gmapOne.plot(lat2,lang2,'green',edge_width=5.5)
        gmapOne.scatter(lat3,lang3,'green', size=50, marker=True , symbol='Intermediate 2')
        # gmapOne.plot(lat3,lang3,'green',edge_width=5.5)
        gmapOne.scatter(lat4,lang4,'green', size=50, marker=True , symbol='Intermediate 3')
        # gmapOne.plot(lat4,lang4,'green',edge_width=5.5)
        gmapOne.scatter(lat5,lang5,'green', size=50, marker=True , symbol='Intermediate 4')
        # gmapOne.plot(lat5,lang5,'green',edge_width=5.5)
        gmapOne.draw("map.html")
        import webbrowser
  
        webbrowser.open_new_tab('map.html')
      
        
    elif Lang1 == 'Kasarwadi-Dapodi-Pragati_Nagar-University_Road-Khaire_Vasti-Shivaji_Nagar':
        ms.showinfo( "Route", "Found Route is \nKasarwadi-Dapodi-Pragati_Nagar-University_Road-Khaire_Vasti-Shivaji_Nagar")
        print("route2 Found")
        lat1 = [18.606088 , 18.585293 ]
        lang1 = [73.822791, 73.833217]
        lat2 = [18.585293 , 18.565459]
        lang2 = [73.833217, 73.831163]
        lat3 = [18.565459,18.555553]
        lang3 = [73.831163,73.818436]
        lat4 = [18.555553, 18.535204]
        lang4 = [73.818436, 73.838236]
        lat5 = [18.535204,18.53082]
        lang5 = [73.838236,73.847464]
        gmapOne = gmplot.GoogleMapPlotter(18.516726, 73.856255, 15 )
        gmapOne.scatter(lat1,lang1,'pink', size=50, marker=True , symbol='Source')
        gmapOne.plot(lat1,lang1,'pink',edge_width=5.5)
        gmapOne.scatter(lat2,lang2,'green', size=50, marker=True , symbol='Intermediate 1')
        gmapOne.plot(lat2,lang2,'green',edge_width=5.5)
        gmapOne.scatter(lat3,lang3,'red', size=50, marker=True , symbol='Intermediate 2')
        gmapOne.plot(lat3,lang3,'red',edge_width=5.5)
        gmapOne.scatter(lat4,lang4,'red', size=50, marker=True , symbol='Intermediate 3')
        gmapOne.plot(lat4,lang4,'red',edge_width=5.5)
        gmapOne.scatter(lat5,lang5,'green', size=50, marker=True , symbol='Intermediate 4')
        gmapOne.plot(lat5,lang5,'green',edge_width=5.5)
        gmapOne.draw("map.html")
        import webbrowser

        webbrowser.open_new_tab('map.html')
        
    elif Lang1 == 'Shivaji Nagar-Khaire_Vasti-University_Road-Pragati_Nagar-Dapodi-Kasarwadi':
        ms.showinfo( "Route", "Found Route is \nShivaji Nagar-Khaire_Vasti-University_Road-Pragati_Nagar-Dapodi-Kasarwadi")
        print("route3 Found")
        lat1 = [18.53082 , 18.535204 ]
        lang1 = [73.847464, 73.838236]
        lat2 = [18.535204 , 18.555553]	
        lang2 = [73.838236, 73.818436]
        lat3 = [18.555553,18.565459]
        lang3 = [73.818436,73.831163]
        lat4 = [18.565459, 18.585293]
        lang4 = [73.831163, 73.833217]
        lat5 = [18.585293,18.606088]
        lang5 = [73.833217,73.822791]
        gmapOne = gmplot.GoogleMapPlotter(18.516726, 73.856255, 15 )
        gmapOne.scatter(lat1,lang1,'green', size=50, marker=True , symbol='Source')
        gmapOne.plot(lat1,lang1,'green',edge_width=5.5)
        gmapOne.scatter(lat2,lang2,'red', size=50, marker=True , symbol='Intermediate 1')
        gmapOne.plot(lat2,lang2,'red',edge_width=5.5)
        gmapOne.scatter(lat3,lang3,'red', size=50, marker=True , symbol='Intermediate 2')
        gmapOne.plot(lat3,lang3,'red',edge_width=5.5)
        gmapOne.scatter(lat4,lang4,'red', size=50, marker=True , symbol='Intermediate 3')
        gmapOne.plot(lat4,lang4,'red',edge_width=5.5)
        gmapOne.scatter(lat5,lang5,'green', size=50, marker=True , symbol='Intermediate 4')
        gmapOne.plot(lat5,lang5,'green',edge_width=5.5)
        gmapOne.draw("map.html")
        import webbrowser
  
        webbrowser.open_new_tab('map.html')
    else:
        print("No route Found")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


label_1 = Label(frame_alpr, text="Route On Google Map",width=20,font=("bold", 10))
label_1.place(x=20,y=80)

list1 = ['Kasarwadi-Dapodi-Bopodi-Khadki-Sancheti-Shivaji_Nagar'
         ,'Kasarwadi-Dapodi-Pragati_Nagar-University_Road-Khaire_Vasti-Shivaji_Nagar'
         ,'Shivaji Nagar-Khaire_Vasti-University_Road-Pragati_Nagar-Dapodi-Kasarwadi'];

droplist=OptionMenu(frame_alpr,c, *list1)
droplist.config(width=100)
c.set('Select route') 
droplist.place(x=200,y=80)

Button(frame_alpr, text='Find Route',width=20,bg='brown',fg='white',command=translate).place(x=20,y=130)



root.mainloop()
