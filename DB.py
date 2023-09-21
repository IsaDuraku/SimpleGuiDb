import psycopg2
from tkinter import *


def create():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="????",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute('''Create Table students(ID Serial, Name text,Age text,Address text);''')
    print("created")
    conn.commit()
    conn.close()
    
def insert_data(name,age,address):
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="????",host="localhost",port="5432")
    cur = conn.cursor()
    # name = input("Enter name: ")
    # age = input("Enter age: ")
    # address = input("Enter address: ")

    query = '''Insert Into students (Name,Age,Address) Values(%s,%s,%s);'''
    cur.execute(query,(name,age,address))
    print("Inserted")
    conn.commit()
    conn.close()

 


#create()   
# insert_data() 