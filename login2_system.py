
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox

import pymysql
from sha256 import *
from hashlib import *
import binascii




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
        self.bg_pic = ImageTk.Image.open("pictures_1/background3_img.jpg")
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
        ImageTk.Image.open("pictures_1/web_user.jpg").resize((100, 100), ImageTk.Image.ANTIALIAS))

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
                        self.iv_and_salt=take_iv_id_salt(self.txt_username.get())
                        self.clear()
                        self.security_key=security_key(self.txt_password.get(),self.iv_and_salt[1].encode("latin1"))

                        self.password_manager_window()





                    else:

                        messagebox.showerror("Error","Invalid password!",parent=self.root)
                        self.clear()



                con.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
    def password_manager_window(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Password manager Window")
        self.root2.geometry("400x400+450+150")
        self.root2.focus_force()
        self.root2.grab_set()



        #========background============
        self.root2.configure(bg="gray7")
        #=======Title==========
        title=Label(self.root2,text="Password Manager",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="white",fg="black")
        title.pack(side=TOP,fill=X)
        # =====All varibles=====
        self.Title_var = StringVar()
        self.Username_var = StringVar()
        self.URL_var = StringVar()
        self.Password_var = StringVar()
        self.Notes_var = StringVar()
        self.U_ID_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        #=====Manager_Frame======
        Manager_Frame=Frame(self.root2,bd=4,relief=RIDGE,bg="white")
        Manager_Frame.place(x=20,y=100,width=450,height=560)
        #====Detail_Frame
        Detail_Frame = Frame(self.root2, bd=4, relief=RIDGE, bg="white")
        Detail_Frame.place(x=500, y=100, width=765, height=70)

        #====content of manager frame===

        m_title=Label(Manager_Frame,text="Manage Passwords",bg="white",fg="black",font=("times new roman",20,"bold")).place(x=100,y=10)
        lbl_title=Label(Manager_Frame,text="Title",bg="white",fg="black",font=("times new roman",20,"bold")).place(x=10,y=80)
        self.txt_title=Entry(Manager_Frame,textvariable=self.Title_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE).place(x=140,y=80)
        lbl_username = Label(Manager_Frame, text="Username", bg="white", fg="black", font=("times new roman", 20, "bold")).place(x=10,y=130)
        self.txt_username_entry=Entry(Manager_Frame,textvariable=self.Username_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE).place(x=140, y=130)
        lbl_URL=Label(Manager_Frame, text="URL", bg="white", fg="black", font=("times new roman", 20, "bold")).place(x=10, y=180)
        self.txt_URL=Entry(Manager_Frame,textvariable=self.URL_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE).place(x=140,y=180)
        lbl_password=Label(Manager_Frame, text="Password", bg="white", fg="black", font=("times new roman", 20, "bold")).place(x=10,y=230)
        self.txt_password_entry=Entry(Manager_Frame,textvariable=self.Password_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE).place(x=140,y=230)
        lbl_notes=Label(Manager_Frame, text="Notes", bg="white", fg="black", font=("times new roman", 20, "bold")).place(x=10,y=280)
        self.txt_notes = Entry(Manager_Frame,textvariable=self.Notes_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE).place(x=140,y=280,height=100)
        self.txt_U_ID=Entry(Manager_Frame,textvariable=self.U_ID_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE,state="readonly",highlightbackground="red",highlightthickness=2).place(x=10,y=390,width=120)


        Addbtn=Button(Manager_Frame,text="Add",fg="white",borderwidth=1,bg="green",font=("times new roman",17,"bold"),relief=GROOVE,command=self.add_data).place(x=10,y=500,width=100)
        Updatetn=Button(Manager_Frame,text="Update",fg="white",borderwidth=1,bg="green",font=("times new roman",17,"bold"),relief=GROOVE,command=self.update_data).place(x=110,y=500,width=100)
        Deletebtn=Button(Manager_Frame,text="Delete",fg="white",borderwidth=1,bg="green",font=("times new roman",17,"bold"),relief=GROOVE,command=self.delete_data).place(x=210,y=500,width=100)
        Clearbtn=Button(Manager_Frame,text="Clear",fg="white",borderwidth=1,bg="green",font=("times new roman",17,"bold"),relief=GROOVE,command=self.Clear).place(x=310,y=500,width=100)

    #=====content of detail frame=====
        lbl_search=lbl_password=Label(Detail_Frame, text="Search By:", bg="white", fg="black", font=("times new roman", 20, "bold")).place(x=10,y=10)
        combo_search=ttk.Combobox(Detail_Frame,font=("times new roman",13,"bold"),state="readonly",textvariable=self.search_by)
        combo_search["values"]=("","Title","Username","URL")
        combo_search.place(x=145,y=15)


        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=1,font=("times new roman",17,"bold"),bd=5,relief=GROOVE).place(x=360,y=15,width=170,height=40)
        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,bg="gold3",font=("times new roman",10,"bold"),command=self.search_option).place(x=545,y=15)
        show_allbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, bg="OrangeRed3",
                           font=("times new roman", 10, "bold"),command=self.fetch_data).place(x=640, y=15)
    #=======Table Frame====
        Table_Frame = Frame(self.root2, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=500, y=190, width=765, height=470)




        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.Password_Table=ttk.Treeview(Table_Frame,columns=("Title","Username","URL","Password","Notes","U_ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Password_Table.xview)
        scroll_y.config(command=self.Password_Table.yview)
        self.Password_Table.heading("Title",text="Title")
        self.Password_Table.heading("Username", text="Username")
        self.Password_Table.heading("URL", text="URL")
        self.Password_Table.heading("Password", text="Password")
        self.Password_Table.heading("Notes", text="Notes")
        self.Password_Table.heading("U_ID", text="U_ID")

        self.Password_Table["show"]="headings"
        self.Password_Table.column("Title",width=200)
        self.Password_Table.column("Username", width=200)
        self.Password_Table.column("URL", width=200)
        self.Password_Table.column("Password", width=200)
        self.Password_Table.column("Notes", width=200)
        self.Password_Table.column("U_ID",width=200)
        self.Password_Table.pack(fill=BOTH,expand=1)
        self.Password_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    #======Add entries=======
    def add_data(self):
        if self.Title_var.get()=="" or self.Username_var.get()=="" or self.URL_var.get()=="" or self.Password_var.get()=="" or self.Notes_var.get()=="":
            messagebox.showerror("Error","All entries are required to fulfill!" ,parent=self.root2)
        else:

            db=pymysql.connect("localhost","root",'',"password_database")
            cur=db.cursor()
            cur.execute("insert into user_{} (Title,Username,URL,Password,Notes,U_ID) values(%s,%s,%s,%s,%s,%s)".format(str(self.iv_and_salt[2])),(self.Title_var.get(),self.Username_var.get(),
                     self.URL_var.get(),
                     encrypt(self.Password_var.get(),
                             self.security_key,int(self.iv_and_salt[0])),
                     self.Notes_var.get(),random_ID_generator()))
            db.commit()
            self.fetch_data()
            self.Clear()
            db.close()
    #======fetch data====
    def fetch_data(self):
        db = pymysql.connect("localhost", "root", '', "password_database")
        cur = db.cursor()
        cur.execute("select * from user_{}".format(str(self.iv_and_salt[2])))
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Password_Table.delete(*self.Password_Table.get_children())
            for row in rows:
                self.Password_Table.insert("",END,values=(row[0],row[1],row[2],decrypt(binascii.unhexlify(row[3]),self.security_key,int(self.iv_and_salt[0])),row[4],row[5]))
            db.commit()
        db.close()
    #======Clear_entries=====
    def Clear(self):
        self.Title_var.set("")
        self.Username_var.set("")
        self.URL_var.set("")
        self.Password_var.set("")
        self.Notes_var.set("")
        self.U_ID_var.set("")
        self.search_txt.set("")
        self.search_by.set("")
    def get_cursor(self,ev):
        cursor_row=self.Password_Table.focus()
        content=self.Password_Table.item(cursor_row)
        row=content["values"]
        self.Title_var.set(row[0])
        self.Username_var.set(row[1])
        self.URL_var.set(row[2])
        self.Password_var.set(row[3])
        self.Notes_var.set(row[4])
        self.U_ID_var.set(row[5])
    #=======update data from table=======

    def update_data(self):
        db = pymysql.connect("localhost", "root", '', "password_database")
        cur = db.cursor()
        cur.execute("update user_{} set Title=%s,Username=%s,URL=%s,Password=%s,Notes=%s where U_ID=%s".format(str(self.iv_and_salt[2])),
                    (self.Title_var.get(),self.Username_var.get(),self.URL_var.get(),encrypt(self.Password_var.get(),
                             self.security_key,int(self.iv_and_salt[0])),self.Notes_var.get(),self.U_ID_var.get()))

        db.commit()
        self.fetch_data()
        self.Clear()
        db.close()
    #======delete entry from table======
    def delete_data(self):
        db = pymysql.connect("localhost", "root", '', "password_database")
        cur = db.cursor()
        cur.execute("delete from user_{} where U_ID=%s".format(str(self.iv_and_salt[2])),(self.U_ID_var.get()))
        db.commit()
        db.close()
        self.fetch_data()
        self.Clear()

    def search_option(self):
        db = pymysql.connect("localhost", "root", '', "password_database")
        cur = db.cursor()
        table_name="select * from user_"+str(self.iv_and_salt[2])
        cur.execute(table_name+" where " + str(self.search_by.get()) +" Like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Password_Table.delete(*self.Password_Table.get_children())
            for row in rows:
                self.Password_Table.insert("", END, values=(row[0], row[1], row[2],
                                                            decrypt(binascii.unhexlify(row[3]), self.security_key,
                                                                    int(self.iv_and_salt[0])), row[4], row[5]))
            db.commit()
        else:
            messagebox.showerror("Error","Incorrect Information!",parent=self.root2)
        db.close()
        self.Clear()






if __name__=="__main__":
    main()
