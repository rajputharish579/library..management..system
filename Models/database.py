import sqlite3
import datetime


conn = sqlite3.connect('library_management.db')
c = conn.cursor()

def saving_details():
    conn.commit()

def closing_database():
    conn.close()


# Database details
def books_taken(username):
    c.execute('SELECT * FROM books WHERE rented_user = "%s";' %(username))
    list = c.fetchall()
    saving_details()
    return len(list)

def book_details(username):
    c.execute('SELECT * FROM books WHERE rented_user = "%s";' %(username))
    list = c.fetchall()
    saving_details()
    return list

def book_lending():
    c.execute('SELECT * FROM books WHERE rented_user IS NULL;')
    lend_books = c.fetchall()
    saving_details()
    return lend_books

def book_return(book_name):
    c.execute('UPDATE books SET rented_date = NULL WHERE book_name="%s";' %(book_name))
    saving_details()
    c.execute('UPDATE books SET rented_user = NULL WHERE book_name = "%s";' %(book_name))
    saving_details()


## Checking login credentials
def login_check(username ,  password):
    c.execute('SELECT * FROM users WHERE username="%s" AND password="%s"' % (username, password))
    list = c.fetchall()
    if len(list) > 0:
        return True
    elif len(list) == 0:
        return False

## Checking registration data
def registration_check(username , password):
    c.execute('SELECT * FROM users WHERE username="%s" AND password="%s"' % (username, password))
    list = c.fetchall()
    if len(list) > 0:
        saving_details()
        return False
    elif len(list) == 0:
        c.execute('INSERT INTO users (username , password) VALUES ( "%s" , "%s");' %(username , password))
        saving_details()
        return True
    
def book_lending_database(book_name):
    name = book_name.split(',')[0]
    username = book_name.split(',')[1]
    current_date  = datetime.date.today()
    c.execute('UPDATE books SET rented_date = "%s" WHERE book_name = "%s";' %(current_date , name))
    saving_details()
    c.execute('UPDATE books SET rented_user = "%s" WHERE book_name ="%s";' %(username , name))
    saving_details()
    c.execute('SELECT * FROM books WHERE rented_user = "%s";' %(username))
    list = c.fetchall()
    return list

