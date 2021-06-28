from tkinter import*
from tkinter import messagebox
root=Tk()

def first_window():
    root=Tk()
    root.title('Frame')
    root.geometry('560x560')
    frm= Frame(root,bg='#ccccff' ,height=600, width=560)

    CheckVar1 = IntVar()

    CheckVar2 = IntVar()

    CheckVar3 = IntVar()

    CheckVar4 = IntVar()

    CheckVar5 = IntVar()

    CheckVar6 = IntVar()

    CheckVar7 = IntVar()

    CheckVar8 = IntVar()

    CheckVar9 = IntVar()

    CheckVar10 = IntVar()


    C1 = Checkbutton(frm,text='Cat',height=2,width=20,variable=CheckVar1, onvalue=1,offvalue=0,font=('Arial', 14))
    C1.pack()
    C1.place(x=10,y=10)
    C2 = Checkbutton(frm,text='Dog',height=2,width=20,variable=CheckVar2, onvalue=1,offvalue=0,font=('Arial', 14))
    C2.pack()
    C2.place(x=10,y=90)
    C3 = Checkbutton(frm, text='Glass',height=2, width=20,variable=CheckVar3, onvalue=1,offvalue=0,font='Arial' )
    C3.pack()
    C3.place(x=10,y=170)
    C4 = Checkbutton(frm, text='Iron Man',height=2, width=20,variable=CheckVar4, onvalue=1,offvalue=0,font=('Arial', 14))
    C4.pack()
    C4.place(x=10,y=250)
    C5 = Checkbutton(frm, text='Elephant',height=2, width=20,variable=CheckVar5, onvalue=1,offvalue=0,font=('Arial', 14))
    C5.pack()
    C5.place(x=10,y=330)
    C6 = Checkbutton(frm, text='Rat',height=2, width=20,variable=CheckVar6, onvalue=1,offvalue=0,font=('Arial', 14))
    C6.pack()
    C6.place(x=220,y=10)
    C7 = Checkbutton(frm, text='Bird',height=2, width=20,variable=CheckVar7, onvalue=1,offvalue=0,font=('Arial', 14))
    C7.pack()
    C7.place(x=220,y=90)
    C8 = Checkbutton(frm, text='Cow',height=2, width=20,variable=CheckVar8, onvalue=1,offvalue=0,font=('Arial', 14))
    C8.pack()
    C8.place(x=220,y=170)
    C9 = Checkbutton(frm, text='Got',height=2, width=20,variable=CheckVar9, onvalue=1,offvalue=0,font=('Arial', 14))
    C9.pack()
    C9.place(x=220,y=250)
    C10 = Checkbutton(frm, text='Earth',height=2, width=20,variable=CheckVar10, onvalue=1,offvalue=0,font=('Arial', 14))
    C10.pack()
    C10.place(x=220,y=330)
    def showMsg():
        a=CheckVar1.get()
        b=CheckVar2.get()
        c=CheckVar3.get()
        d=CheckVar4.get()
        if a and b:
            messagebox.showinfo('2 correct')
        elif a:
            messagebox.showinfo('1 correct')
        elif b:
            messagebox.showinfo('1 correct')
        else:
            messagebox.showinfo('all incorrect')
       
    b= Button(frm, text = 'Submit',height=4,width=30, bd = '10',bg='teal',activebackground='#00ff00',command=showMsg)
    B1= Button(frm, text="End", height=4,width=30, bd = '10',bg='teal',activebackground='#00ff00',command= root.destroy )
    B1.pack()
    B1.place(x=100, y= 480)
    b.pack()
    b.place(x=100, y= 390)
    frm.propagate(0)
    frm.pack()
    label = Label()
    label.pack()
    
####################################################################################

c=Canvas(bg='white', height=600,width=1200)
file1=PhotoImage(file="catg.gif")
file2=PhotoImage(file="Dog.gif")
file3=PhotoImage(file="glass.gif")
file4=PhotoImage(file="ironman.png")
button_1= Button(root, text = 'Next',height=4,width=30, bd = '5',bg='teal',activebackground='#00ff00',command=first_window)

c.create_image(200, 200, anchor=CENTER, image=file1)
c.create_image(700, 150, anchor=CENTER, image=file2)
c.create_image(900, 400, anchor=CENTER, image=file3)
c.create_image(500, 400, anchor=CENTER, image=file4)
c.pack(expand = YES, fill = BOTH)
c.pack()
button_1.place(x=100, y=200)
button_1.pack()
#####################################################################################
root.mainloop()
