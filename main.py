from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

root = Tk()

acc = {'sahan':'0000','shibin':'1111','rachan':'2222'}

def loginFunc():
    global eusername
    username = eusername.get()
    global epass
    password = epass.get()
    try:
        if acc[username] == password:
            global root
            root.destroy()
            import attendance
            attendance.mainloop()
        else:
            messagebox.showwarning('Error !!!','Wrong username or password !!!')

    except KeyError:
        messagebox.showwarning('Error !!!','Wrong username or password !!!')

lglbl = Label(root,text=' Login ',font=Font(size=40)).grid(row=0,column=0,columnspan=4)
loginspacer = Label(root,text='').grid(row=1,column=0)
namelbl = Label(root,text=' Username ',font=Font(size=20)).grid(row=2,column=0,sticky='w')
eusername = Entry(root,font=Font(size=20))
eusername.grid(row=2,column=1,sticky='nsw',columnspan=2)
spacer1 = Label(root,text='   ').grid(row=1,column=3)
passlbl = Label(root,text=' Password ',font=Font(size=20)).grid(row=3,column=0,sticky='w')
epass = Entry(root,font=Font(size=20))
epass.grid(row=3,column=1,sticky='nsw',columnspan=2)
spacer = Label(root,text='').grid(row=4,column=0)
login = Button(root,text='Login',font=Font(size=16),command=loginFunc).grid(row=5,column=1,sticky='nse')
cancel = Button(root,text='Cancel',font=Font(size=16),command=root.destroy).grid(row=5,column=2,sticky='nsw')
spacer = Label(root,text='').grid(row=6,column=0)
root.resizable(False,False)
root.mainloop()
