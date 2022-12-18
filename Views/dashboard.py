from tkinter import *
import pubsub as pub
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry
import tkintertable as tktable
from tkintertable import Tables
import datetime
from datetime  import datetime
from tkinter import messagebox
from pubsub import pub
from dateutil import parser


class Dashboard():
  
    def __init__(self , username , bookcount , *book_details) -> None:
        self.dashboard = Tk()
        self.dashboard.title("Library - Manager")
        self.dashboard.geometry('950x600')
        # self.dashboard.geometry('500x500')
        self.username = username
        self.bookcount = bookcount
        self.raw_details = []
        self.taken_books = []
        self.books_to_take = []
        self.whole_book = []
        self.book_details  = book_details
        self.total_check_amount = 0
        self.fine_amount = 0
        

    def populating_book_list(self):
        self.taken_books = self.book_details[0]
        self.to_take_books = self.book_details[1]
        self.whole_book = self.book_details[2]
        self.taken_book_count = len(self.taken_books)
        self.book_to_take_count  = len(self.to_take_books)
        self.whole_book_count = len(self.whole_book)

    def defining_static_controls(self):
       
        self.upper_layout  = Frame(self.dashboard )
        self.main_layout = Frame(self.dashboard)
        self.bottom_layout = Frame(self.dashboard)

        self.amount_label  = Label(self.upper_layout , text="Amount Incured || 0 ")
        self.username_label = Label(self.upper_layout , text="Welcome || " + self.username) 
        self.books_label = Label(self.upper_layout , text="Books Taken || " + str(self.bookcount))

    
    def inserting_data_after_rent_click(self, returned_data):
        try:
            self.books['menu'].delete(self.var_choose.get())
            self.var_choose.set("Available Books")
            self.bookcount +=1
            self.books_label.config(text="Books Taken || " + str(self.bookcount))
            self.total_check_amount = 0
            self.fine_amount = 0
            for item in self.table.get_children():
                self.table.delete(item)
            for lines in returned_data:
                self.returned_data = lines
                
                current_date = datetime.today().date()
                date2 = self.returned_data[3]
                date2 = parser.parse(date2).date()
                self.date_diff = self.check_amount(current_date , date2)
                self.total_check_amount  += self.date_diff
                self.amount_label.config(text="Amount Incured || " + str(self.total_check_amount))
                self.table.insert('' , 'end' , text="1" , values=(self.returned_data[0] , self.returned_data[1] , self.returned_data[2], self.returned_data[3],self.date_diff))
        except :
            print("Error hai")


    def check_amount(self, date1, date2):
        delta =  (date1 - date2).days
        if delta == 0 :
            return 12
        elif  0 < delta < 10:
            return delta * 12
        else:
            return (delta*12) + 30

        

    # Function to add the book details when the Form is loaded.
    def inserting_data_into_table(self):
        #self.table.insert('' , 'end' , text="1" ,values = ("Book Name" , "Book Publication" , "Book Author" , "Rented date"))
        if self.whole_book_count > 0 :
            self.total_check_amount = 0
            self.fine_amount = 0
            for books in self.whole_book:
                current_date = datetime.today().date()
                date2 = books[3]
                date2 = parser.parse(date2).date()
                self.date_diff = self.check_amount(current_date , date2)
                self.total_check_amount  += self.date_diff
                self.amount_label.config(text="Amount Incured || " + str(self.total_check_amount))
                self.table.insert('' ,'end' , text="1" , values=(books[0] , books[1] , books[2] , books[3] , self.date_diff))
        


    
    """Here working functions defined to be called by the buttons"""
    def renting_book(self):
        data  = self.var_choose.get()
        data = data + "," + self.username
        pub.sendMessage('book_renting' , book_name  = data)

    
    def returning_book(self):
        selected_item = self.table.selection()[0]
        returned_book_name  = self.table.item(selected_item)['values'][0]
        current_value = self.table .item(selected_item)['values'][4]
        self.total_check_amount-= current_value
        self.amount_label.config(text="Amount Incured || " + str(self.total_check_amount))
        # Define the function to add the deleted book into the to take books
        pub.sendMessage("returned_book" , returned_book =  returned_book_name)
        self.bookcount -=1
        self.books_label.config(text="Books Taken || " + str(self.bookcount))
        self.table.delete(self.table.delete(selected_item))
        
   
    
    def defining_dynamic_controls(self):
        self.populating_book_list()
        self.var_choose = StringVar()
        self.var_return = StringVar()
        self.var_choose.set("Available Books")
        self.var_return.set("Choose to Return")

        if self.book_to_take_count > 0:
            self.books = OptionMenu(self.main_layout , self.var_choose, *self.to_take_books)
            self.rentbook = Button(self.main_layout ,text="Rent Selected Book" ,command=self.renting_book)
        if self.taken_book_count > 0:
            self.delete_book = Button(self.main_layout , text="Return Selected Book" , command=self.returning_book)

        self.table  = ttk.Treeview(self.bottom_layout,  columns=("1" , "2" , "3" ,"4" , "5") , show='headings' , height=5)
        self.table.column("# 1" , anchor=CENTER)
        self.table.heading("# 1", text="Book Name")
        self.table.column("# 2", anchor=CENTER)
        self.table.heading("# 2", text="Book Publication")
        self.table.column("# 3", anchor=CENTER)
        self.table.heading("# 3", text="Book Author")
        self.table.column("# 4", anchor=CENTER)
        self.table.heading("# 4", text="Rented Date")
        self.table.column("# 5" , anchor=CENTER)
        self.table.heading("# 5", text="Rent Charged (Rupees)")

    def placing_controls(self):
        # Placement for the static controls
        self.upper_layout.pack(fill=BOTH , pady=12)
        self.main_layout.pack(fill=BOTH , pady=12)
        self.books_label.pack(side=LEFT , padx=15)
        self.amount_label.pack(side=LEFT, padx=15)
        self.username_label.pack(side=RIGHT , padx=10)

        # Placement for the dynamic controls
        if self.book_to_take_count > 0:
            self.books.pack(side=LEFT , padx=5)
            # self.datepicker.pack(side=LEFT , padx=5)
            self.rentbook.pack(side=LEFT , padx=5)

        if self.taken_book_count > 0:
            self.delete_book.pack(side=RIGHT , padx=5)
            # self.rented_books.pack(side=RIGHT , padx=5)

        self.bottom_layout.pack(fill=BOTH, expand=True , side=TOP)
        self.table.pack(side=TOP, fill="both", expand=True)
        # Calling the inserting fuction
        self.inserting_data_into_table()
        self.dashboard.mainloop()
        