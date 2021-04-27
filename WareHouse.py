# import modules
from tkinter import *
import tkinter.messagebox
import pymysql


# class for Frond End UI (User-Interface
class Product:
    def __init__(self, root):
        self.root = root
        self.root.title("Warehouse Inventory Management System")
        self.root.geometry("1325x690")
        self.root.config(bg="black")


        # set variable for entry section 
        pId = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany = StringVar()
        pContact = StringVar()


        ''' Create the Frame '''
        MainFrame = Frame(self.root, bg="blue")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=1, padx=50,
                          pady=10, bg='white', relief=GROOVE)
        HeadFrame.pack(side=TOP)

        self.ITitle = Label(HeadFrame, font=('arial', 40, 'bold'), fg="black",
                            text=' Warehouse Inventory Management ', bg="white")
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame, bd=2, width=1300, height=60,
                               padx=50, pady=20, bg='white', relief=GROOVE)
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame, bd=2, width=1290, height=400,
                          padx=30, pady=20, bg='white', relief=GROOVE)
        BodyFrame.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame, bd=2, width=600, height=380,
                                   padx=50, pady=10, bg='yellow', relief=GROOVE, font=('arial', 15, 'bold'),
                                   text='Product Item Details : ')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame, bd=2, width=300, height=380,
                                    padx=50, pady=10, bg='yellow', relief=GROOVE, font=('arial', 15, 'bold'),
                                    text='Show Product Information : ')
        RightBodyFrame.pack(side=RIGHT)



        ''' Add the Widgets to LeftBodyFrame '''


if __name__ == '__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()
