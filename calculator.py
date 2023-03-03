from tkinter import*
cal=Tk()
cal.geometry("440x500+400+80")
cal.minsize(width=300,height=550)
cal.maxsize(width=400,height=600)
cal.title("Calculator")


eq=""
var=StringVar()
def btn(no):
    global eq
    eq=eq+str(no)
    var.set(eq)
def clear1():
    global eq
    eq=""
    e1.delete(0,END)
    var.set(eq)
def show():
    global eq
    s=var.get()
    s=eval(s)
    eq=str(s)
    var.set(eq)



e1=Entry(cal,font=2,textvariable=var,width=31,bg="aqua",fg="red")
e1.place(x=25,y=25)
button1 = Button(cal, text=' 1 ',command=lambda:btn(1) ,height=1, width=7)
button1.place(x=25,y=70)
button2 = Button(cal, text=' 2 ',command=lambda:btn(2) ,height=1, width=7)
button2.place(x=100,y=70)
button3 = Button(cal, text=' 3 ',command=lambda:btn(3) ,height=1, width=7)
button3.place(x=175,y=70)
button4 = Button(cal, text=' * ',command=lambda:btn("*") ,height=1, width=7)
button4.place(x=250,y=70)

button5 = Button(cal, text=' 4 ',command=lambda:btn(4) ,height=1, width=7)
button5.place(x=25,y=120)
button6= Button(cal, text=' 5 ',command=lambda:btn(5) ,height=1, width=7)
button6.place(x=100,y=120)
button7 = Button(cal, text=' 6 ',command=lambda:btn(6) ,height=1, width=7)
button7.place(x=175,y=120)
button8 = Button(cal, text=' / ',command=lambda:btn('/') ,height=1, width=7)
button8.place(x=250,y=120)

button9 = Button(cal, text=' 7 ',command=lambda:btn(7) ,height=1, width=7)
button9.place(x=25,y=170)
button10= Button(cal, text=' 8 ',command=lambda:btn(8) ,height=1, width=7)
button10.place(x=100,y=170)
button11 = Button(cal, text=' 9 ',command=lambda:btn(9) ,height=1, width=7)
button11.place(x=175,y=170)
button12 = Button(cal, text=' + ',command=lambda:btn('+') ,height=1, width=7)
button12.place(x=250,y=170)

button13 = Button(cal, text=' C ',command=lambda:clear1() ,height=1, width=7)
button13.place(x=25,y=220)
button14= Button(cal, text=' 0 ',command=lambda:btn(0) ,height=1, width=7)
button14.place(x=100,y=220)
button15 = Button(cal, text=' = ',command=lambda:show() ,height=1, width=7)
button15.place(x=175,y=220)
button16 = Button(cal, text=' - ',command=lambda:btn('-') ,height=1, width=7)
button16.place(x=250,y=220)

cal.mainloop()