from tkinter import font
from tkinter.font import Font
import pymysql
from tkinter import *
from datetime import date
from tkinter import messagebox

conn = pymysql.connect(host='localhost',user='root',passwd='',database='student',port=3307)
cur = conn.cursor()

root = Tk()

def change():
    global dateEntry
    ndate = dateEntry.get()
    global thedate
    thedate = ndate

    ls = ndate.split('-')
    temp = False
    if len(ls) == 3:
        if len(ls[0]) == 4:
            if len(ls[1]) > 0 and len(ls[1]) < 3 :
                if len(ls[2]) > 0 and len(ls[2]) < 3 :
                    try:
                        a,b,c = int(ls[0]),int(ls[1]),int(ls[2])
                        temp = True
                    except ValueError:
                        temp = False
    if not temp:
        messagebox.showerror('Error','Wrong Date format !!!\nGive the date in the format \'YYYY-MM-DD\'')
    else:
        redisplay(ndate)

def refresh():
    l = len(table)
    for each in table:
        each.remove()
    global rowcount
    rowcount -= l
    display(thedate)

def presentFunc(usn):
    cur.execute('select count(*) from attendance where (day = \'{}\' and usn = \'{}\')'.format(thedate,usn))
    for each in cur:
        if each[0] == 1:
            cur.execute('update attendance set presence = 1 where (usn = \'{}\' and day = \'{}\')'.format(usn,thedate))
        else:
            cur.execute('insert into attendance values(\'{}\',\'{}\',{})'.format(thedate,usn,1))    
    conn.commit()
    redisplay(thedate)

def absentFunc(usn):
    cur.execute('select count(*) from attendance where (day = \'{}\' and usn = \'{}\')'.format(thedate,usn))
    for each in cur:
        if each[0] == 1:
            cur.execute('update attendance set presence = 0 where (usn = \'{}\' and day = \'{}\')'.format(usn,thedate))
        else:
            cur.execute('insert into attendance values(\'{}\',\'{}\',{})'.format(thedate,usn,0))    
    conn.commit()
    redisplay(thedate)

'''
def registration():
    name = ename.get()
    usn = eusn.get()
    sem = esem.get()
    branch = ebranch.get()
    cur.execute('insert into students values(\'{}\',\'{}\',\'{}\',\'{}\')'.format(usn,name,sem,branch))
    conn.commit()
    if cur.rowcount == 1:
        global reg
        reg.destroy()

def register():
    global reg
    reg = Toplevel()
    lbl = Label(reg,text=' Register New Student ',font=Font(size=30)).grid(row=0,column=0,columnspan=2)
    lname = Label(reg,text='  Name',font=Font(size=16)).grid(row=1,column=0,sticky='w')
    global ename
    ename = Entry(reg,font=Font(size=16))
    ename.grid(row=1,column=1,sticky='nsw')
    lusn = Label(reg,text='  USN',font=Font(size=16)).grid(row=2,column=0,sticky='w')
    global eusn
    eusn = Entry(reg,font=Font(size=16))
    eusn.grid(row=2,column=1,sticky='nsw')
    lsem = Label(reg,text='  Sem',font=Font(size=16)).grid(row=3,column=0,sticky='w')
    global esem
    esem = Entry(reg,font=Font(size=16))
    esem.grid(row=3,column=1,sticky='nsw')
    lbranch = Label(reg,text='  Branch',font=Font(size=16)).grid(row=4,column=0,sticky='w')
    global ebranch
    ebranch = Entry(reg,font=Font(size=16))
    ebranch.grid(row=4,column=1,sticky='nsw')
    spacerline1 = Label(reg,text='').grid(row=5,column=0)
    regbut = Button(reg,text='Register',font=Font(size=16),command=registration).grid(row=6,column=0,sticky='e')
    cancel = Button(reg,text='Cancel',font=Font(size=16),command=reg.destroy).grid(row=6,column=1,sticky='w')
    spacerline = Label(reg,text='').grid(row=7,column=0)
    reg.resizable(False,False)
'''

header = Label(root,text='Student Attendance System',font=Font(size=40))
header.grid(row=0,columnspan=7)

spacer1 = Label(root,text='',font=Font(size=20)).grid(row=1,column=0)

datelbl = Label(root,text='Date : ',font=Font(size=30)).grid(row=2,column=1,sticky='nsew')
dateEntry = Entry(root,font=Font(size=20))
dateEntry.grid(row=2,column=2,columnspan=2,sticky='nsew')
change = Button(root,text='Change',font=Font(size=20),command=change).grid(row=2,column=4,sticky='snew')

#register = Button(root,text='Register',font=Font(size=20),command=register).grid(row=3,column=2,sticky='nsew')
#refresh = Button(root,text='Refresh',font=Font(size=20),command=lambda:redisplay(thedate)).grid(row=3,column=2,columnspan=2,sticky='')

spacer1 = Label(root,text='',font=Font(size=20)).grid(row=4,column=0)

lblusn = Label(root,text='USN',font=Font(size=20)).grid(row=5,column=0)
lblname = Label(root,text='Name',font=Font(size=20)).grid(row=5,column=1)
lblsem = Label(root,text='Semester',font=Font(size=20)).grid(row=5,column=2)
lblbranch = Label(root,text='Branch',font=Font(size=20)).grid(row=5,column=3)
lblattendance = Label(root,text='Attendance',font=Font(size=20)).grid(row=5,column=4)

rowcount = 6

class tableRow:
    def __init__(self,root,ls):
        self.ls = ls
        self.usn = Entry(root)
        self.usn.insert(END,ls[0])
        self.usn.grid(row=rowcount,column=0,sticky='nsew')
        self.name = Entry(root)
        self.name.insert(END,ls[1])
        self.name.grid(row=rowcount,column=1,sticky='nsew')
        self.sem = Entry(root)
        self.sem.insert(END,ls[2])
        self.sem.grid(row=rowcount,column=2,sticky='nsew')
        self.branch = Entry(root)
        self.branch.insert(END,ls[3])
        self.branch.grid(row=rowcount,column=3,sticky='nsew')
        self.attendance = Entry(root)
        self.attendance.insert(END,ls[4])
        self.attendance.grid(row=rowcount,column=4,sticky='nsew')
        self.present = Button(root,text='Present',command=lambda:presentFunc(self.usn.get())).grid(row=rowcount,column=5,sticky='nsew')
        self.absent = Button(root,text='Absent',command=lambda:absentFunc(self.usn.get())).grid(row=rowcount,column=6,sticky='nsew')
        self.row = rowcount
    
    def update(self,root,ls):
        self.ls = ls
        self.usn = Entry(root)
        self.usn.insert(END,ls[0])
        self.usn.grid(row=rowcount,column=0,sticky='nsew')
        self.name = Entry(root)
        self.name.insert(END,ls[1])
        self.name.grid(row=rowcount,column=1,sticky='nsew')
        self.sem = Entry(root)
        self.sem.insert(END,ls[2])
        self.sem.grid(row=rowcount,column=2,sticky='nsew')
        self.branch = Entry(root)
        self.branch.insert(END,ls[3])
        self.branch.grid(row=rowcount,column=3,sticky='nsew')
        self.attendance = Entry(root)
        self.attendance.insert(END,ls[4])
        self.attendance.grid(row=rowcount,column=4,sticky='nsew')
        self.row = rowcount

    def remove(self):
        self.usn.grid_remove()
        self.name.grid_remove()
        self.sem.grid_remove()
        self.attendance.grid_remove()
        self.branch.grid_remove()
        #self.present.destroy()
        #self.absent.destroy()

    def setPresence(self,x):
        self.attendance.delete(0, 'end')
        self.attendance.insert(END,str(x))

today = str(date.today())

students = []

def initStudents():
    cur.execute('select * from students')
    for each in cur:
        tls = []
        for i in each:
            tls.append(str(i))
        tls.append('Not Marked')
        students.append(tls)

table = []

def display(date):
    global rowcount
    for each in students:
        cur.execute('select presence from attendance where(day = \'{}\' and usn = \'{}\')'.format(date,each[0]))
        if cur.rowcount == 1:
            b = False
            for r in cur:
                b = bool(r[0])
            if b:
                each[4] = 'Present'
            else:
                each[4] = 'Absent'
        table.append(tableRow(root,each))
        rowcount += 1

def redisplay(date):
    for i in range(len(students)):
        cur.execute('select presence from attendance where day = \'{}\' and usn = \'{}\''.format(date,students[i][0]))
        if cur.rowcount == 1:
            for x in cur:
                if x[0] == 1:
                    students[i][-1] = 'Present'
                else:
                    students[i][-1] = 'Absent'
        else:
            students[i][-1] = 'Not Marked'
        table[i].setPresence(students[i][-1])

thedate = today
initStudents()
display(thedate)

root.title('Attendance Register')
root.resizable(False,False)
root.mainloop()