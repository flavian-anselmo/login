from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
win = Tk()
win.title("user log_in")
win.geometry("420x400")
win.resizable(False,False)
win.iconbitmap(r'C:\Users\hp\Desktop\photos\login.ico')
#save_the_password
def reg_pwd():
    global u
    global p,log_in,reg
    file = open("user.txt","a")
    u = file.write(user_name2.get() +"\n")
    p = file.write(password2.get()+ "\n")
    file.close()
    user_name2.delete(0,END)
    password2.delete(0,END)
    submission()
    win2.destroy()

def submission():
    messagebox.showinfo("msg_box","login info saved ")



def check_pwd():
    global u
    global p
    file = open("user.txt", "r")
    data = file.readlines()

    u = data[0].strip()
    p = data[1].strip()
    u = data[2].strip()
    p = data[3].strip()
    if user_name.get() == u and password.get()==p:
        messagebox.showinfo("msg_box", 'login successfull!')

    elif user_name.get() != u:
        messagebox.showinfo("msg_box", 'invalid username!')
    elif password.get()!= p:
        messagebox.showinfo("msg_box", 'invalid passcode!')






    file.close()


#registration of passwords
def register():
    global win2,log_in,reg, user_name2 , password2
    win2 = Toplevel()
    win2.title("registration")
    win2.geometry("420x215")
    win2.iconbitmap(r'C:\Users\hp\Desktop\photos\login.ico')

    #frame
    log2 = LabelFrame(win2, text="", padx=80, pady=70, bg="light green")
    log2.grid(padx=3, pady=15)
    #labels
    user2 = Label(log2, text="Username", bg="light green")
    user2.grid(row=5, column=0)
    pwd2 = Label(log2, text="Password", bg="light green")
    pwd2.grid(row=6, column=0)
    #entry
    user_name2 = Entry(log2, width=30)
    user_name2.grid(row=5, column=2, padx=3, pady=3)
    password2 = Entry(log2, width=30,show = "*")
    password2.grid(row=6, column=2, padx=3, pady=3)

    #buttons
    submit = Button(log2, text="Submit",command =reg_pwd, padx=5, pady=5, relief=FLAT)
    submit.grid(row=8, column=2, padx=2, pady=2)


#labels
log = LabelFrame(win,text = "",padx= 80 ,pady=70,bg = "light green")
log.grid(padx=3,pady =15 )
user = Label(log,text = "Username",bg = "light green")
user.grid(row = 5 ,column = 0 )
pwd = Label(log,text = "Password",bg = "light green")
pwd.grid(row = 6 ,column = 0 )

#entry_widgets
user_name = Entry(log,width =30)
user_name.grid(row = 5,column = 2,padx = 3,pady = 3)
password = Entry(log,width =30,show = "*")
password.grid(row = 6,column = 2,padx = 3,pady = 3)
#button
log_in = Button(log,text ="login",command = check_pwd,padx = 5,pady = 5,relief = FLAT)
log_in.grid(row = 8,column = 2,padx = 2,pady = 2)
reg = Button(log,text ="register",padx = 7,pady = 5,relief = FLAT,command = register)
reg.grid(row = 9,column = 2,padx = 2,pady = 2)


#picture
img = ImageTk.PhotoImage(Image.open(r"C:\users\hp\Desktop\photos\login.ico"))
l = Label(log,image = img)
l.grid(row = 0, column =2,pady = 0,padx = 0)

win.mainloop()