import psycopg2
from tkinter import *
import tkinter as tk
from DB import insert_data

def search_id(ID):
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="2458",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''select * from students where id=%s'''
    cur.execute(query,(ID))
    row = cur.fetchone()
    display_result(row)
    conn.commit()
    conn.close()

def search_name(name):
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="????,host="localhost",port="5432")
    cur = conn.cursor()
    query = '''select * from students where name=%s'''
    cur.execute(query,(name,))
    row = cur.fetchone()
    display_result(row)
    conn.commit()
    conn.close()
    

def display_result(row):
    listbox=Listbox(frame,width=23,height=1)
    listbox.grid(row=9,column=1)
    listbox.insert(END,row)

def display_all():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="2458",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''select * from students'''
    cur.execute(query)
    row=cur.fetchall()

    listbox=Listbox(frame,width=23,height=5)
    listbox.grid(row=11,column=1)
    for x in row:
        listbox.insert(END,x)


root = Tk()
    
canvas = Canvas(root,height=480,width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame,text="Add data")
label.grid(row=0,column=1)

label = Label(frame,text="Name: ")
label.grid(row=1,column=0)

entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text="Age: ")
label.grid(row=2,column=0)

entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

label = Label(frame,text="Address: ")
label.grid(row=3,column=0)

entry_address = Entry(frame)
entry_address.grid(row=3,column=1)

button = Button(frame,text="Add",command = lambda:insert_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4,column=1)

label = Label(frame,text="Search Data: ")
label.grid(row=5,column=1)

label = Label(frame,text="Search by ID: ")
label.grid(row=6,column=0)

id_search = Entry(frame)
id_search.grid(row=6,column=1)

button = Button(frame,text="Search",command = lambda:search_id(id_search.get()))
button.grid(row=6,column=2)

label = Label(frame,text="Search by Name: ")
label.grid(row=7,column=0)

name_search = Entry(frame)
name_search.grid(row=7,column=1)

button = Button(frame,text="Search",command = lambda:search_name(name_search.get()))
button.grid(row=7,column=2)

button = Button(frame,text="Display all",command = lambda:display_all())
button.grid(row=10,column=1)



root.mainloop()
