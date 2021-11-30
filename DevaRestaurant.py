from tkinter import *
import random

root=Tk()
root.geometry("1445x846+0+0")
root.title("Deva Restaurant")
Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,bg="white",height=500,width=800,relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root,bg="white",height=500,width=400,relief=SUNKEN)
f2.pack(side=RIGHT)

lblinfo = Label(Tops,font=('aria',30,'bold'),text='Deva Restaurant',fg='steel blue',bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

text_Input=StringVar()
operator=" "

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator=""

def Ref():
    x=random.randint(12980,50876)
    randomRef = str(x)
    random.set(randomRef)

    cof=float(Fries.get())
    colfries=float(Largefries.get())
    com=float(momos.get())
    coh=float(hamburger.get())
    cod=float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colf*50
    costofmomos = com*30
    costofhamburger= coh*40
    costofdrinks = cod*40

    costofmeal = "Rs.",str('%.2f'%(costoffries + costoflargefries + costofmomos + costofhamburger+ costofdrinks))
    PayTax = ((costoffries + costoflargefries + costofmomos + costofhamburger+ costofdrinks)*0.33)
    Totalcost = (costoffries + costoflargefries + costofmomos + costofhamburger+ costofdrinks)
    Ser_Charge = ((costoffries + costoflargefries + costofmomos + costofhamburger+ costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Ser_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)

def qexit():
    root.destroy

def reset():
    random.set("")
    Fries.set("")
    Largefries.set("")
    momos.set("")
    hamburger.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    

btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="powder blue", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=8,bg="powder blue",command=lambda:btnclick(8) )
btn8.grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=9,bg="powder blue",command=lambda:btnclick(9) )
btn9.grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text="+",bg="powder blue",command=lambda:btnclick("+") )
Addition.grid(row=2,column=3)
btn4=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=4,bg="powder blue",command=lambda:btnclick(4) )
btn4.grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=5,bg="powder blue",command=lambda:btnclick(5) )
btn5.grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=6,bg="powder blue",command=lambda:btnclick(6) )
btn6.grid(row=3,column=2)
Substraction=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text="-",bg="powder blue",command=lambda:btnclick("-") )
Substraction.grid(row=3,column=3)
btn3=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=3,bg="powder blue",command=lambda:btnclick(3) )
btn3.grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=2,bg="powder blue",command=lambda:btnclick(2) )
btn2.grid(row=4,column=1)
btn1=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=1,bg="powder blue",command=lambda:btnclick(1) )
btn1.grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text="*",bg="powder blue",command=lambda:btnclick("*") )
Multiply.grid(row=4,column=3)
btn0=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=0,bg="powder blue",command=lambda:btnclick(0) )
btn0.grid(row=5,column=0)
btnc=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text="c",bg="powder blue",command=clrdisplay)
btnc.grid(row=5,column=1)
Decimal=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text=".",bg="powder blue",command=lambda:btnclick(1) )
Decimal.grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text="/",bg="powder blue",command=lambda:btnclick("/") )
Division.grid(row=5,column=3)
btnequal=Button(f2,padx=40,pady=16,bd=4,fg="black",font=('ariel', 20, 'bold'),text="=",bg="powder blue",command=lambda:btnclick("=") )
btnequal.grid(row=6,columnspan=4)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="-By Bhaskar Joshi",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)

lblreferance=Label(f1,font=('aria',16,'bold'),text="Order No.",fg="steel blue",bd=30,anchor="w" )
lblreferance.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=random , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=28,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable="Fries" , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)
lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=23,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable="Largefries" , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)
lblmomos = Label(f1, font=( 'aria' ,16, 'bold' ),text="momos Meal",fg="steel blue",bd=16,anchor='w')
lblmomos.grid(row=3,column=0)
txtmomos = Entry(f1,font=('ariel' ,16,'bold'), textvariable="momos", bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtmomos.grid(row=3,column=1)
lblham = Label(f1, font=( 'aria' ,16, 'bold' ),text="hamburger",fg="steel blue",bd=23,anchor='w')
lblham.grid(row=4,column=0)
txtham = Entry(f1,font=('ariel' ,16,'bold'), textvariable="hamburger", bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtham.grid(row=4,column=1)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable="Drinks" , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)
lblCost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="steel blue",bd=10,anchor='w')
lblCost.grid(row=1,column=2)
txtCost = Entry(f1,font=('ariel' ,16,'bold'), textvariable="Cost" , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCost.grid(row=1,column=3)
lblService_charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service_charge",fg="steel blue",bd=10,anchor='w')
lblService_charge.grid(row=2,column=2)
txtService_charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable="Service_charge" , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_charge.grid(row=2,column=3)
lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable="Tax" , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)
lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=4,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable="Total" , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=4,column=3)



Fries = StringVar()
Largefries = StringVar()
momos = StringVar()
ham = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()




root.mainloop()