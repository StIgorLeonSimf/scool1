import math
from tkinter import *


def mult(n1, d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return n, d


def div(n1, d1, n2, d2):
    n = n1 * d2
    d = d1 * n2
    return n, d


def add(n1, d1, n2, d2):
    # nod = math.gcd(d1, d2)
    if d1 != d2:
        ng1 = n1 * d2
        ng2 = n2 * d1
        d = d1 * d2
        n = ng1 + ng2
    return n, d


def sub(n1, d1, n2, d2):
    # nod = math.gcd(d1, d2)
    if d1 != d2:
        ng1 = n1 * d2
        ng2 = n2 * d1
        d = d1 * d2
        n = ng1 - ng2
    return n, d


root = Tk()
root.geometry('300x120+400+250')
frame = Frame(root)
frame.pack(pady=15)

num1 = Entry(frame, font='Arial 10')
num1.config(width=3, justify='center')
num1.grid(row=0, column=0)
l1 = Label(frame, text='-------')
l1.grid(row=1, column=0)
den1 = Entry(frame, font='Arial 10')
den1.config(width=3, justify='center')
den1.grid(row=2, column=0)

oper = Entry(frame, width=3, justify='center')
oper.grid(row=1, column=1)

num2 = Entry(frame, font='Arial 10')
num2.config(width=3, justify='center')
num2.grid(row=0, column=2)
l2 = Label(frame, text='-------')
l2.grid(row=1, column=2)
den2 = Entry(frame, font='Arial 10')
den2.config(width=3, justify='center')
den2.grid(row=2, column=2)
eqv = Button(frame, text='=')
eqv.grid(row=1, column=3, padx=5)

intr = Label(frame, font='Arial 10')
intr.config(width=3, justify='center', bg='lightgray')
intr.grid(row=1, column=4)
numr = Label(frame, font='Arial 10')
numr.config(width=3, justify='center', bg='lightgray')
numr.grid(row=0, column=5)
lr = Label(frame, text='-------')
lr.grid(row=1, column=5)
denr = Label(frame, font='Arial 10', bg='lightgray')
denr.config(width=3, justify='center')
denr.grid(row=2, column=5)


def func(event):
    opn = oper.get().strip()
    nm1 = int(num1.get().strip())
    dn1 = int(den1.get().strip())
    nm2 = int(num2.get().strip())
    dn2 = int(den2.get().strip())
    if opn == '*':
        res = mult(nm1, dn1, nm2, dn2)
    elif opn == '/':
        res = div(nm1, dn1, nm2, dn2)
    elif opn == '+':
        res = add(nm1, dn1, nm2, dn2)
    elif opn == '-':
        res = sub(nm1, dn1, nm2, dn2)

    nod = math.gcd(res[0], res[1])
    if nod > 1:
        n = int(res[0] / nod)
        d = int(res[1] / nod)
    else:
        n, d = res[0], res[1]
    if n == d:
        intr['text'] = 1
        numr.config(text='')
        denr.config(text='')
        return
    if n > d:

        it = n // d
        n %= d
        intr['text'] = it
    numr.config(text=n)
    denr.config(text=d)


eqv.bind('<Button-1>', func)
root.mainloop()
