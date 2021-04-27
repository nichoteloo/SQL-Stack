from tkinter import *
import tkinter
from tkinter import messagebox
import pymysql

root = tkinter.Tk()

root.geometry("600x450")

L1 = Label(root, text="Enter Id: ", font=('arial', 30), fg='blue')
L1.grid(row=0, column=0, sticky=W)
E1 = Entry(root, bd=5, width=50)
E1.grid(row=0, column=1)

L2 = Label(root, text="Enter Name: ", font=('arial', 30), fg='blue')
L2.grid(row=1, column=0, sticky=W)
E2 = Entry(root, bd=5, width=50)
E2.grid(row=1, column=1)

L3 = Label(root, text="Enter Address: ", font=('arial', 30), fg='blue')
L3.grid(row=2, column=0, sticky=W)
E3 = Entry(root, bd=5, width=50)
E3.grid(row=2, column=1)


def myButtonEvent(selection):
    print("Student Id is : ", E1.get())
    print("Student Name is : ", E2.get())
    print("Student Address is : ", E3.get())

    id = E1.get()
    name = E2.get()
    address = E3.get()

    if selection in ('Insert'):
        conn = pymysql.connect("localhost", "root", "", "user_test")
        cur = conn.cursor()  # get the cursor object
        # cur.execute("select version()") # check if it's run, select specific command
        # data = cur.fetchone()
        # print("MySQL Database Version is ",data)

        query = "create table if not exists student (id char(20) Not Null,\
                    name char(20), address char(20))"

        cur.execute(query)
        conn.commit()
        print("Table student created successfully")

        # try:
        #     cur.execute(query)
        #     conn.commit()
        #     print("Table student created successfully")
        # except Error as e:
        #     print("Error occured at database creation.", e)
        #     conn.rollback()
        #     conn.close()

        insQuery = "insert into student (id, name, address)\
                    values ('%s','%s','%s')" % (id, name, address)

        try:
            cur.execute(insQuery)
            conn.commit()
            print("Student saved to DB table ", id, ",", name, ",", address)
            conn.close()
        except Error as e:
            print("Error occured at database insertion.", e)
            conn.rollback()
            conn.close()

    elif selection in ('Update'):
        try:
            query = "update student set name='%s'" % (
                name)+", address='%s'" % (address)+" where id = '%s'" % (id)
            conn = pymysql.connect("localhost", "root", "", "user_test")
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
            print("student updated successfully..", id)
        except Error as e:
            print("Error occured at database updation.", e)
            conn.rollback()
            conn.close()

    elif selection in ('Delete'):
        try:
            query = "delete from student where id = '%s'" % (id)
            conn = pymysql.connect("localhost", "root", "", "user_test")
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
            print("student deleted successfully..", id)
        except Error as e:
            print("Error occured at database deletion.", e)
            conn.rollback()
            conn.close()

    elif selection in ('Select'):
        try:
            query = "select * from student where id = '%s'" % (id)
            conn = pymysql.connect("localhost", "root", "", "user_test")
            cur = conn.cursor()
            cur.execute(query)

            # return tuple in one row
            rows = cur.fetchall()
            address1 = ''
            name1 = ''
            id1 = ''
            for row in rows:
                id1 = row[0]
                name1 = row[1]
                address1 = row[2]

            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)

            E1.insert(0, id1)
            E2.insert(1, name1)
            E3.insert(2, address1)

            conn.close()
            print("student fetch successfully..", id)
        except Error as e:
            print("Error occured at database selection.", e)
            conn.close()


BInsert = tkinter.Button(text="Insert", fg="black",
                         bg="white", font=('arial', 20, 'bold'), command=lambda: myButtonEvent('Insert'))
BInsert.grid(row=5, column=0)

BUpdate = tkinter.Button(text="Update", fg="black",
                         bg="white", font=('arial', 20, 'bold'), command=lambda: myButtonEvent('Update'))
BUpdate.grid(row=5, column=1)

BDelete = tkinter.Button(text="Delete", fg="black",
                         bg="white", font=('arial', 20, 'bold'), command=lambda: myButtonEvent('Delete'))
BDelete.grid(row=7, column=0)

BSelect = tkinter.Button(text="Select", fg="black",
                         bg="white", font=('arial', 20, 'bold'), command=lambda: myButtonEvent('Select'))
BSelect.grid(row=7, column=1)

root.mainloop()
