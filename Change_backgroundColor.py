import tkinter as tk
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')
def callme():
    if(chkvalue.get()==1):
        win.configure(background='Red')
    elif(chkvalue.get()==2):
        win.configure(background='Green')              
    else:
        win.configure(background='Blue')    
# chkvalue = tk.BooleanVar()
chkvalue = tk.IntVar()
l4 = tk.Radiobutton(win,text="Red", var=chkvalue, command=callme, value=1)
l4.place(x=100,y=100)
l5 = tk.Radiobutton(win,text="green", var=chkvalue, command=callme, value=2)
l5.place(x=100,y=200)
l6 = tk.Radiobutton(win,text="Blue", var=chkvalue, command=callme,value=3)
l6.place(x=100,y=300)
win.mainloop()