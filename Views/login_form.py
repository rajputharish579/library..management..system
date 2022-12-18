# Importing relevant modules for the operation
from tkinter import *
from tkinter import ttk
from pubsub import pub
# End Importing



class Login_form():

    ## Calling in int and defining the parameters
    def __init__(self) -> None:
        # Non self controls
        self.loginscreen = Tk()
        self.loginscreen.title("Login - Library Manager")
        self.loginscreen.geometry('250x200')
        self.loginscreen.resizable(0,0)
    
    ## Defining the functions to call when the buttons are clicked Login and Register
    def login_click(self):
        self.username  = self.username_textbox.get()
        self.password = self.password_textbox.get()
        self.username_textbox.delete(0 , END)
        self.password_textbox.delete(0,END)
        pub.sendMessage('login_data' , login_data = self.username + "," + self.password)

    def registration_click(self):
        self.username  = self.username_textbox.get()
        self.password = self.password_textbox.get()
        self.username_textbox.delete(0 , END)   
        self.password_textbox.delete(0,END)
        pub.sendMessage('registration_data' , registration_data = self.username + "," + self.password)


    ## Defining the non dynamic controls They will be the same in the app and it won't cahnge dynamically
    def non_dynamic_controls(self):
        self.username_label  = Label(self.loginscreen , text="Enter Username")
        self.username_textbox = Entry(self.loginscreen , width=40)
        self.password_label = Label(self.loginscreen , text="Enter Password")
        self.password_textbox = Entry(self.loginscreen, width=40 , show="*")
        self.remember_me = Checkbutton(self.loginscreen , text="Remember Me")
        self.loginBtn = Button(self.loginscreen  ,text="Login" , width=18,command=self.login_click)
        self.registerbtn = Button(self.loginscreen , text="Register New User", width=33  , command=self.registration_click)
        self.librarianbtn = Button(self.loginscreen ,text="Librarian-Login" , width=16)
        self.admintbn = Button(self.loginscreen, text="Admin-Login" , width=16)
    
    # Placing the controls in the app have used the place function here
    def placing_controls(self):
        self.username_label.place(x=2 , y=5)
        self.username_textbox.place(x=3 , y =30)
        self.password_label.place(x=2 , y = 55)
        self.password_textbox.place(x=3 , y = 80)
        self.remember_me.place(x=2 , y=105)
        self.loginBtn.place(x=110 , y= 105)
        self.registerbtn.place(x=5 , y=135)
        self.librarianbtn.place(x = 2 , y=165)
        self.admintbn.place(x=126 , y=165)


    def calling_app(self):
        self.loginscreen.mainloop()

    def killing_app(self):
        self.loginscreen.destroy()






# if __name__ == '__main__':
#     global name
#     name = Login_form()
#     name.non_dynamic_controls()
#     name.placing_controls()
#     name.calling_app()
