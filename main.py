from tkinter import *
import tkinter.font as font
root=Tk()
root.geometry('350x300')
root.title('Project Tec')
myfont=font.Font(family='Courier',weight='bold',size=10)
#create a label
mylabel=Label(root,text="Hello World!")

#clicks functions
def click(num):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(num))

def click_clear():
    e.delete(0,END)

def click_add():
    first=e.get()
    global f_num
    global math
    math="add"
    f_num=int(first)
    e.delete(0,END)

def click_sub():
    first=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(first)
    e.delete(0,END)

def click_mul():
    first=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(first)
    e.delete(0,END)

def click_div():
    first=e.get()
    global f_num
    global math
    math="div"
    f_num=int(first)
    e.delete(0,END)

def click_equal():
    second=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num+int(second))
    if math=="sub":
        e.insert(0,f_num-int(second))
    if math=="mul":
        e.insert(0,f_num*int(second))
    if math=="div":
        e.insert(0,f_num/int(second))
#create an entry widget
e=Entry(root,width=50,borderwidth=5,bg='yellow')
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#create calculator buttons

button_1=Button(root,text="1",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(1))
button_2=Button(root,text="2",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(2))
button_3=Button(root,text="3",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(3))

button_4=Button(root,text="4",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(4))
button_5=Button(root,text="5",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(5))
button_6=Button(root,text="6",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(6))

button_7=Button(root,text="7",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(7))
button_8=Button(root,text="8",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(8))
button_9=Button(root,text="9",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(9))

button_0=Button(root,text="0",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click(0))
button_plus=Button(root,text="+",padx=50,pady=5,bg='skyblue',fg='black' ,command=click_add)
button_clear=Button(root,text="C",padx=50,pady=5,bg='skyblue',fg='black' ,command=lambda :click_clear())
button_equal=Button(root,text="=",padx=50,pady=5,bg='skyblue',fg='black' ,command=click_equal)
button_sub=Button(root,text="-",padx=50,pady=5,bg='skyblue',fg='black' ,command=click_sub)
button_mul=Button(root,text="*",padx=50,pady=5,bg='skyblue',fg='black' ,command=click_mul)
button_div=Button(root,text="/",padx=50,pady=5,bg='skyblue',fg='black' ,command=click_div)

#show buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_plus.grid(row=5,column=0)
button_equal.grid(row=5,column=1)

button_mul.grid(row=6,column=0)
button_sub.grid(row=6,column=1)
button_div.grid(row=6,column=2)


root.mainloop()

