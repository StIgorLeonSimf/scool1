import time
from tkinter import *
from tkinter import messagebox
import pygame as pg

pg.init()
pg.mixer.music.load('music.mp3')

root = Tk()
root.geometry('450x250+400+200')
root.title('Будильник')
root.config(bg='black')

tab = Label(root, text='00:00:00')
tab.config(font='Arial 50', bg='black', fg='lime')
tab.pack(pady=10)
alarm = Entry(root)
alarm.config(font='Arial 20', width=8, justify='center')
alarm.pack()
on_btn = Button(root)
on_btn.config(width=10, text='Включить', font='Arial 10')
on_btn.pack(pady=10)
off_btn = Button(root)
off_btn.config(width=10, text='Выключить', font='Arial 10')
off_btn.pack()

alarm_time = ''


def tick():
    global alarm_time
    time_now = time.strftime('%X')  # '%H:%M:%S'
    if (alarm_time == time_now or alarm_time == time.strftime('%H:%M') or
            alarm_time == time.strftime('%H')):
        alarm_time = ''
        pg.mixer.music.play()

    tab.config(text=time_now)
    tab.after(1000, tick)

def on_alarm(event):
    global alarm_time
    alarm_time = alarm.get().strip()
    # print(event.x, event.y)
    event.widget.after(1,
                       lambda: messagebox.showinfo
                       ("Информация", f'Будильник '
                                      f'установлен на {alarm_time}'))



def off_alarm(event):
    alarm_time = ''
    alarm.delete(0, END)
    pg.mixer.music.stop()
    # messagebox.showinfo('Сообщение', 'Будильник выключен')
    event.widget.after(1,
                       lambda: messagebox.showinfo
                       ('Сообщение', 'Будильник выключен'))

on_btn.bind('<Button-1>', on_alarm)
off_btn.bind('<Button-1>', off_alarm)

tick()
root.mainloop()