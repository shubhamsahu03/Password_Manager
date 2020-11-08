
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox

import pymysql
from sha256 import *
from hashlib import *





def main():
    root=Tk()
    app=Login_system(root)
    root.mainloop()
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1350x700+0+0")
        self.root.focus_force()
        self.root.grab_set()

        #======BG IMAGE=======
        self.bg_pic = ImageTk.Image.open("C:\images_for_project/background3_img.jpg")
        self.resized = self.bg_pic.resize((1350, 700), ImageTk.Image.ANTIALIAS)
        self.new_bgpic = ImageTk.PhotoImage(self.resized)

        bg_lbl = Label(self.root, image=self.new_bgpic).pack()
        title = Label(self.root, text="Signup System")
        #=======Login Frame======
        Frame_Login=Frame(self.root,bg="white")
        Frame_Login.place(x=280, y=100, width=600, height=400)
        tilte = Label(Frame_Login, text="LOGIN HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(
            x=190, y=30)
        desc=Label(Frame_Login,text="Password Database Login System",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=135,y=100)
        #======profile pic======
        self.web_user = ImageTk.PhotoImage(
        ImageTk.Image.open("C:\images_for_project/web_user.jpg").resize((100, 100), ImageTk.Image.ANTIALIAS))

        dp = Label(Frame_Login, image=self.web_user, bg="white").place(x=475, y=20)
        #=====username====
        username = Label(Frame_Login, text="Username", font=("times new roman", 19, "bold"), bg="white", fg="dark blue").place(
            x=20, y=145)
        self.txt_username=Entry(Frame_Login,font=("times new roman",17),bg="lightgray")
        self.txt_username.place(x=140,y=145,width=250)

        #=====password=====
        self.check_var=IntVar()
        password = Label(Frame_Login, text="Password", font=("times new roman", 19, "bold"), bg="white",
                         fg="dark blue").place(
            x=20, y=195)
        self.txt_password = Entry(Frame_Login, font=("times new roman", 17), bg="lightgray")
        self.txt_password.place(x=140, y=195, width=250)
        self.tab_order()
        #========Buttons================
        Change_btn=Button(Frame_Login,text="Change Password?",bg="white",fg="red",font=("times new roman",12),borderwidth=0,command=self.forget_password).place(x=275,y=236)
        login_btn=Button(Frame_Login,text="Login",fg="white",borderwidth=1,bg="green",font=("times new roman", 17),command=self.login,cursor="hand2").place(x=30,y=350,width=100)

        reset_btn = Button(Frame_Login, text="Reset",bd=1, fg="white", bg="green", font=("times new roman", 17),
                           command=self.clear).place(x=160, y=350, width=100)
        exit_btn = Button(Frame_Login, text="Exit", fg="white", borderwidth=1, bg="green", font=("times new roman", 17),
                          command=self.iExit).place(x=290, y=350)
        btn_reg=Button(Frame_Login,text="Register New Account?",bg="white",fg="blue",font=("times new roman",12),borderwidth=0,command=self.register_window).place(x=20,y=236)
        btn_toggle=Checkbutton(Frame_Login,justify=CENTER,text="Hide",bg="white",fg="blue",font=("times new roman",12),borderwidth=0,command=self.show_psd_hide,variable=self.check_var,onvalue=1,offvalue=0).place(x=400, y=195)




    def tab_order(self):
        self.txt_username.focus()
        widget=[self.txt_username,self.txt_password]
        for i in widget:
            i.lift()
    def show_psd_hide(self):
        if (self.check_var.get()):

            self.txt_password.config(show="*")
        else:

            self.txt_password.config(show="")


    def show_psd_hide_2(self):
        if (self.check_var_2.get()):

            self.new_txt_password.config(show="")
        else:

            self.new_txt_password.config(show="*")


    def iExit_2(self):

            self.iExit_2 = messagebox.askyesno("Change Password systems", "Confirm if you want to exit.", parent=self.root2)
            if self.iExit_2 > 0:
                self.root2.destroy()

            else:
                command = self.root2
                return




    def clear(self):
        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)


    def iExit(self):
        self.iExit=messagebox.askyesno("Login systems","Confirm if you want to exit.",parent=self.root)
        if self.iExit>0:
            self.root.destroy()

        else:
            command=self.root
            return
    def register_window(self):
        self.root.destroy()

    def login(self):
        if self.txt_password.get()=="" or  self.txt_username.get()=="" :
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password='',database="password_database")
                cur=con.cursor()
                cur.execute("select * from user where Username=%s",(self.txt_username.get()))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error","Invalid Username",parent=self.root)
                else:
                    cur_2 = con.cursor()
                    cur_2.execute("select Password,salt from user where Username=%s ",(self.txt_username.get()))
                    data=cur_2.fetchone()
                    s=data[1]
                    salt_encoded=s.encode("utf-8")

                    a=sha256_algo(self.txt_password.get(),salt_encoded)
                    if a==data[0]:
                        messagebox.showinfo("congrats","Successfully logged in!",parent=self.root)
                        self.iv_and_salt=take_iv_salt(self.txt_username.get())
                        self.clear()





                    else:

                        messagebox.showerror("Error","Invalid password!",parent=self.root)
                        self.clear()



                con.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

if __name__=="__main__":
    main()
