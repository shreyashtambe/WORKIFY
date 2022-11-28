# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:39:39 2022

@author: Lenovo
"""
from pandas import *
# importing pandas package
import numpy as np
import pandas as pd
import csv
from pandas import *
import pandas as pd
import csv
import gmplot

from tkinter import messagebox as ms
import shutil, os
import pandas as pandasForSortingCSV 
from pathlib import Path
import shutil
from subprocess import call
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Job Recommandation System")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

n=tk.StringVar()
n1=tk.StringVar()
img=ImageTk.PhotoImage(Image.open("img1.jpg"))

img2=ImageTk.PhotoImage(Image.open("im.jpg"))

img3=ImageTk.PhotoImage(Image.open("img3.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()

lbl = tk.Label(root, text="Job Recommendation System", font=('times', 35,' bold '), height=2, width=58,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)

def Model_Training():
    data = pd.read_csv("City_location.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    

    data['City'] = le.fit_transform(data['City'])
    data['Latitude'] = le.fit_transform(data['Latitude'])
    data['Longitude'] = le.fit_transform(data['Longitude'])
   
       

    """Feature Selection => Manual"""
    x = data.drop(['Status'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Status']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=1234)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.tree import DecisionTreeClassifier
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)


    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as job_recomm.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"job_recomm.joblib")
    print("Model saved as job_recomm.joblib")

# # reading CSV file
def call_file():
    from joblib import dump , load
    a1=load("job_recomm.joblib")
    e1=n.get()
    print(e1)
    data = pd.read_csv(r'city_location.csv')
    interestingRow1 = data[data["Status"] == e1]
    print (interestingRow1)

    print("---------------------------------------------------------------------")
    interestingRow1.to_csv('city_location.csv', sep=',', encoding='utf-8', index=False)
    import pandas as pandasForSortingCSV 
    # assign dataset
    csvData = pandasForSortingCSV.read_csv("rating.csv")
    df = csvData.drop(['job_html', 'Category'], axis = 1)
    print("--------------------------------------------------------")
    print(df)
    df.to_csv('job_final.csv', sep=',', encoding='utf-8', index=False)
    ms.showinfo("Message", "Job Profile Uploaded Successfully")
def rec():
    csvData = pandasForSortingCSV.read_csv("city_location.csv")
    # defining source and destination
    # paths
    src = 'City','Status'
    trg = 'Latitude','Longitude'
    PATH = 'E:/21CG106-job Recommandation'
    def searchFile(fileName):
        for root, dirs, files in os.walk(PATH):
            print('Looking in:',root)
            print(fileName)
            for Files in files:
                try:
                    found = Files.find(fileName)
                    # print(found)
                    if found != -1:
                        print()
                        print(fileName, 'Found\n')
                        shutil.copy2(os.path.join(src,fileName), trg)
                        break
                except:
                    exit()
    files=os.listdir(src)
    

    for f in csvData['ID']:
        print(f)
        f=str(f)
        searchFile(f+'.pdf')
    ms.showinfo("Message", "Recommended job Are Stored In Recommendation Folder")
def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

#button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
 #                   text="Model Training", command=Model_Training, width=15, height=2)
#button3.place(x=5, y=200)

frame_display2 = tk.LabelFrame(root, text=" --Input Text-- ", width=700, height=400, bd=5, font=('times', 14, ' bold '),bg="pink")
frame_display2.grid(row=0, column=0, sticky='nw')
frame_display2.place(x=450, y=250)


l1=tk.Label(frame_display2,text="Select Location",font=('times', 20, ' bold '),width=15)
l1.place(x=80,y=40)

monthchoosen = ttk.Combobox(frame_display2, width = 27,textvariable = n)
monthchoosen['values'] = ('Kasarwadi', 
                          'University_Road',
                          'Khadki',
                          'Sancheti ',
                          'Pragati_Nagar',
                          'Khaire_Vasti',
                          'Bopodi',
                          'Hinjewadi',
                          'Bhumkar_Chowk',
                          'Sayaji_Hotel',
                          'Wakad',
                          'Madhuban_Hotel',
                          'wagholi',
                          'Saswad')
monthchoosen.place(x=420,y=50)  

l2=tk.Label(frame_display2,text="Select criteria",font=('times', 20, ' bold '),width=15)
l2.place(x=80,y=150)

monthchoosen1 = ttk.Combobox(frame_display2, width = 27,textvariable = n1)
monthchoosen1['values'] = ('Plumber', 
                          'Chef',
                          'Electrician',
                         
                         )
monthchoosen1.place(x=420,y=150)  

def reg():
    # -*- coding: utf-8 -*-

    # Open the csv file
    a=n.get()
    b=n1.get()
    data = pd.read_csv(r'city_location.csv')
    interestingRow = data[data["City"] == a]
    print (interestingRow)
    interestingRow = interestingRow[data["Status"] == b]
    print (interestingRow)
    df = interestingRow.drop(['ID', 'City', 'Status'], axis = 1)
    print("--------------------------------------------------------")
    print("Finding Location of Job:")
    print("--------------------------------------------------------")
    print(df)
    df.to_csv('lat_long.csv', sep=',', encoding='utf-8', index=False)
    # reading CSV file
    data = read_csv("lat_long.csv")
     
    # converting column data to list
    Latitude_list = data['Latitude'].tolist()
    Longitude_list = data['Longitude'].tolist()
    pay_list = data['Pay'].tolist()
    gmapOne = gmplot.GoogleMapPlotter(18.606088, 73.822791, 15 )
    gmapOne.scatter(Latitude_list,Longitude_list,'green', size=50, marker=True , symbol='o', label = pay_list)
    gmapOne.draw("map13.html")
    import webbrowser
  
    webbrowser.open_new_tab('map13.html')
    

# button4 = tk.Button(frame_display2, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Upload Value", command=call_file, width=18, height=2)
# button4.place(x=100, y=250)

# Tempus Sans ITC
button4 = tk.Button(frame_display2, foreground="white", background="#560319", font=("Times New Roman", 16, "bold"),
                    text="Submit", command=reg, width=22, height=2)
button4.place(x=400, y=250)

exit = tk.Button(frame_display2, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=230, y=450)

root.mainloop()