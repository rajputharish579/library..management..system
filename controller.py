from pubsub import pub
from Views.login_form import Login_form
import Models.database
import Models.calculations
from tkinter import messagebox
from Views.dashboard import Dashboard
    

message_string = "Library - Manager"


def login_data(login_data):
    username  = login_data.split(",")[0]
    password = login_data.split(",")[1]
    result  = Models.database.login_check(username, password)
    if result:
        books_taken = Models.database.books_taken(username)
        book_lending_list = Models.database.book_lending()
        book_taken_list = Models.database.book_details(username)
        whole_book = []
        whole_book = book_taken_list
        book_lending_list  = Models.calculations.book_taken_data(book_lending_list)
        book_taken_list  = Models.calculations.book_taken_data(book_taken_list)
        name.killing_app()
        calling_dashboard(username , books_taken , book_taken_list , book_lending_list , whole_book)
    else:
        messagebox.showerror(message_string , "Wrong username or password")


def registration_data(registration_data):
    username  = registration_data.split(",")[0]
    password = registration_data.split(",")[1]
    result  = Models.database.registration_check(username , password)
    if result:
        messagebox.showinfo(message_string , "Registration Successful")
    else:
        messagebox.showerror(message_string , "User Already Exists - Choose Different Username and Password")


def rent_book(book_name):
    returned_data = Models.database.book_lending_database(book_name)
    db.inserting_data_after_rent_click(returned_data)

def return_book(returned_book):
    Models.database.book_return(returned_book)

def calling_login():    
    global name
    name  = Login_form()
    name.non_dynamic_controls()
    name.placing_controls()
    name.calling_app()


def calling_dashboard(username , bookcount , *book_details):
    global db
    db =Dashboard(username ,bookcount , *book_details)
    db.defining_static_controls()   
    db.defining_dynamic_controls()
    db.placing_controls()



pub.subscribe(login_data , "login_data")
pub.subscribe(registration_data , "registration_data")
pub.subscribe(rent_book , "book_renting")
pub.subscribe(return_book , "returned_book")



if __name__ == '__main__':
    calling_login()