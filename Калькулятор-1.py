from tkinter import *
from tkinter import messagebox as mb


def summ():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен

    slag1 = int(s1)
    slag2 = int(s2)
    summa = slag1 + slag2
    m1['text'] = f"{s1} + {s2} = {str(summa)}"

    answer = mb.askretrycancel(title="Вопрос", message="Сложить еще два числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

window = Tk()
window.title("Калькулятор")
m = Label(height=3, text="Введи два числа и нажми на кнопку для вычисления суммы")
m.pack()
e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
b = Button(text="Сложить два числа", command=summ)
b.pack()
m1 = Label(height=3)
m1.pack()
window.mainloop()
