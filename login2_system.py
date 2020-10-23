
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
        #========Buttons================
        Change_btn=Button(Frame_Login,text="Change Password?",bg="white",fg="red",font=("times new roman",12),borderwidth=0,command=self.forget_password).place(x=275,y=236)
        login_btn=Button(Frame_Login,text="Login",fg="white",borderwidth=1,bg="green",font=("times new roman", 17),command=self.login,cursor="hand2").place(x=30,y=350,width=100)

        reset_btn = Button(Frame_Login, text="Reset",bd=1, fg="white", bg="green", font=("times new roman", 17),
                           command=self.clear).place(x=160, y=350, width=100)
        exit_btn = Button(Frame_Login, text="Exit", fg="white", borderwidth=1, bg="green", font=("times new roman", 17),
                          command=self.iExit).place(x=290, y=350)
        btn_reg=Button(Frame_Login,text="Register New Account?",bg="white",fg="blue",font=("times new roman",12),borderwidth=0,command=self.register_window).place(x=20,y=236)
        btn_toggle=Checkbutton(Frame_Login,justify=CENTER,text="Hide",bg="white",fg="blue",font=("times new roman",12),borderwidth=0,command=self.show_psd_hide,variable=self.check_var,onvalue=1,offvalue=0).place(x=400, y=195)





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
    def forget_pass(self):
        if self.txt_username_2.get()==""  or self.new_txt_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password='', database="password_database")
                cur = con.cursor()
                cur.execute("select * from user where Username=%s ", self.txt_username_2.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter the valid username", parent=self.root2)
                else:
                    cur.execute("select salt from user where Username=%s ",(self.txt_username_2.get()))
                    data=cur.fetchone()
                    salt_encoded_2=data[0].encode("utf-8")
                    a_2=sha256_algo(self.new_txt_password.get(),salt_encoded_2)
                    cur.execute("update user set Password=%s where Username=%s",(a_2,self.txt_username_2.get()))


                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "your password has been reset,Please login with new password.",
                                        parent=self.root2)


                    self.clear()
            except Exception as es:

                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root2)

    def iExit_2(self):

            self.iExit_2 = messagebox.askyesno("Change Password systems", "Confirm if you want to exit.", parent=self.root2)
            if self.iExit_2 > 0:
                self.root2.destroy()

            else:
                command = self.root2
                return

    def forget_password(self):
        if self.txt_username.get()=="":
            messagebox.showerror("Error","Please enter a username!",parent=self.root)


        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password='',database="password_database")
                cur=con.cursor()
                cur.execute("select * from user where Username=%s ",self.txt_username.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter a valid username",parent=self.root)
                else:

                    con.close()
                    self.root2 = Toplevel(self.root)
                    self.root2.title("Change password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    # =======background image====
                    self.bg_pic2 = ImageTk.Image.open("C:\images_for_project/background3_img.jpg")
                    self.resized_2 = self.bg_pic2.resize((1350, 700), ImageTk.Image.ANTIALIAS)
                    self.new_bgpic2 = ImageTk.PhotoImage(self.resized_2)

                    bg_lbl = Label(self.root2, image=self.new_bgpic2).pack()
                    title = Label(self.root2, text="Signup System")
                    # ======Frame========
                    t_Frame = Frame(self.root2, bg="white")
                    t_Frame.place(x=460, y=100, width=360, height=400)

                    # =====Usename=====
                    desc = Label(t_Frame, text="CHANGE IT NOW",
                                 font=("times new roman", 20, "bold"), bg="white", fg="black").place(x=70, y=40)
                    username2 = Label(t_Frame, text="Username", font=("times new roman", 15, "bold"), bg="white",
                                      fg="red").place(
                        x=20, y=110)
                    self.txt_username_2 = Entry(t_Frame, font=("times new roman", 15), bg="lightgray")
                    self.txt_username_2.place(x=120, y=110, width=170)

                    # =====New Password=====
                    self.check_var_2=IntVar()
                    new_password_1 = Label(t_Frame, text="New ", font=("times new roman", 15, "bold"), bg="white",
                                           fg="blue").place(
                        x=40, y=160)
                    new_password_2 = Label(t_Frame, text="Password ", font=("times new roman", 15, "bold"), bg="white",
                                           fg="blue").place(
                        x=20, y=190)
                    self.new_txt_password = Entry(t_Frame, font=("times new roman", 15), bg="lightgray", show="*")
                    self.new_txt_password.place(x=120, y=160, width=170)
                    #==========================
                    btn_change_password = Button(t_Frame, text="Reset password", bg="green", fg="white",relief=SUNKEN,
                                                 font=("times new roman", 15, "bold"),command=self.forget_pass).place(x=30, y=300)
                    btn_reset=Button(t_Frame, text="Reset", bg="green", fg="white",
                                                 font=("times new roman", 15, "bold"),command=self.clear2,relief=SUNKEN).place(x=180, y=300)
                    btn_toggle_2 = Checkbutton(t_Frame, text="Show", bg="white", fg="blue",
                                             font=("times new roman", 12), borderwidth=0, command=self.show_psd_hide_2,variable=self.check_var_2, onvalue=1, offvalue=0).place(x=295, y=160)
                    btn_exit_2=Button(t_Frame, text="Exit", bg="green", fg="white",
                                                 font=("times new roman", 15, "bold"),command=self.iExit_2,relief=SUNKEN).place(x=247, y=300)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)



    def clear(self):
        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)
    def clear2(self):
        self.txt_username_2.delete(0,END)
        self.new_txt_password.delete(0,END)



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
                        self.clear()
                    else:

                        messagebox.showerror("Error","Invalid password!",parent=self.root)
                        self.clear()



                con.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

if __name__=="__main__":
    main()
