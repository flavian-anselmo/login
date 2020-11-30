from tkinter import*
import sqlite3
from tkinter import messagebox
win = Tk()
win.title("LOGIN_FORM")
win.resizable(False,False)
win.geometry("500x240")
#gets the registration inputs and inserts them in a table
def get_input():
    con = sqlite3.connect("passwd.db")
    c= con.cursor()
    #create a table to store the user name and password
    c.execute('''CREATE TABLE IF NOT EXISTS pass_word_t(
                                    user_name TEXT,
                                    password TEXT
                                    )''' )
    #insret into the table
    c.execute("INSERT INTO pass_word_t VALUES(:user_name,:password)",
              {
                  'user_name':reg_entry.get(),
                  'password':passw_entry.get()
              })
    con.commit()
    con.close()
    reg_entry.delete(0,END)
    passw_entry.delete(0, END)
def log_in():
    con = sqlite3.connect("passwd.db")
    c = con.cursor()
    #read from the table
    #query into the table
    c.execute("SELECT *,rowid FROM pass_word_t ")
    items = c.fetchall()
    for i in items:
        print(i)
        if i[0]==log_entry.get() and i[1]==pass_entry.get():
            login_valid()

    if items[0]!=log_entry.get() and items[1]!=pass_entry.get():
        login_invalid()

    con.commit()
    con.close()
#deleting users from the system
def delete_form():
    global del_entry
    d_win = Toplevel()
    d_win.resizable(False, False)
    d_win.geometry("400x215")
    d_win.title("DELETE_USER")

    del_log_frame = LabelFrame(d_win, text="REGISTER_USER", padx=100, pady=50, bg="lightgreen")
    del_log_frame.pack(padx=10, pady=10)
    del_name = Label(del_log_frame, text="DELETE_ID", bg="lightgreen")
    del_name.grid(row=0, column=0)
    del_but = Button(del_log_frame, text="Delete", fg="red", bg="blue", padx=20, pady=5,
                     relief="flat",command=delete_user)
    del_but.grid(row=3, column=0)

    del_entry = Entry(del_log_frame, width=30)
    del_entry.grid(row=0, column=1)

def delete_user():
    con = sqlite3.connect("passwd.db")
    c = con.cursor()
    c.execute("DELETE FROM pass_word_t WHERE  rowid=" + del_entry.get() )
    con.commit()
    con.close()

def login_valid():
    messagebox.showinfo("Valid","LOGIN SUCCESSFUL")
def login_invalid():
    messagebox.showerror("Error!","ACCESS DENIED!")

#registration function
def reg_win():
    global reg_entry,passw_entry,reg_log_frame
    r_win=Toplevel()
    r_win.resizable(False,False)
    r_win.geometry("400x215")
    r_win.title("USER_REGISTRATION")

    reg_log_frame = LabelFrame(r_win, text="REGISTER_USER", padx=100, pady=50, bg="lightgreen")
    reg_log_frame.pack(padx=10, pady=10)
    reg_name = Label(reg_log_frame, text="USER_NAME", bg="lightgreen")
    reg_name.grid(row=0, column=0)
    reg_password = Label(reg_log_frame, text="PASSWORD", bg="lightgreen")
    reg_password.grid(row=2, column=0)
    reg_but = Button(reg_log_frame, text="Submit", fg="red", bg="blue", padx=20, pady=5,
                     relief="flat",command=get_input)
    reg_but.grid(row=5, column=0)

    reg_entry = Entry(reg_log_frame,width=30)
    reg_entry.grid(row=0,column=1 )
    passw_entry = Entry(reg_log_frame, width=30)
    passw_entry.grid(row=2, column=1)


log_frame=LabelFrame(win,text = "LOGIN_FORM",padx = 100,pady=50,bg="lightgreen")
log_frame.pack(padx = 10,pady=10)
user_name=Label(log_frame,text="USERNAME",bg = "lightgreen")
user_name.grid(row=0,column =0)
password=Label(log_frame,text="PASSWORD",bg="lightgreen")
password.grid(row=2,column=0)
login_but=Button(log_frame,text="Login",bg="blue",relief="flat",padx=20,pady=5,
                 command=log_in)
login_but.grid(row=3,column=0)
reg_but=Button(log_frame,text="click here to register!",fg="red",bg="lightgreen",padx=20,pady=5,
               relief="flat",command=reg_win)
del_but_1 = Button(log_frame,text="Delete",fg = "black",bg="red",padx= 20,pady=5,relief="flat",
                   command=delete_form)
del_but_1 .grid(row=5,column=0)
reg_but.grid(row=4,column=0)
log_entry = Entry(log_frame,width=30)
log_entry.grid(row=0,column=1 )
pass_entry = Entry(log_frame,width=30)
pass_entry.grid(row=2,column=1 )

win.mainloop()



