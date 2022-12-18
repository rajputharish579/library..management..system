from tkinter import *
from tkinter import ttk




class Admin():

    def __init__(self , username , *book_details) -> None:
        self.admin = Tk()
        self.username = username
        self.book_details  = book_details


    def defining_controls(self):
        self.upper_frame  = Frame(self.admin)
        self.table  = ttk.Treeview(self.upper_frame,  columns=("1" , "2" , "3" ,"4" , "5") , show='headings' , height=5)
        self.table.column("# 1" , anchor=CENTER)
        self.table.heading("# 1", text="Book Name")
        self.table.column("# 2", anchor=CENTER)
        self.table.heading("# 2", text="Book Publication")
        self.table.column("# 3", anchor=CENTER)
        self.table.heading("# 3", text="Book Author")
        self.table.column("# 4", anchor=CENTER)
        self.table.heading("# 4", text="Rented Date")
        self.table.column("# 5" , anchor=CENTER)
        self.table.heading("# 5", text="Username")

    def placing_controls(self):
        pass

