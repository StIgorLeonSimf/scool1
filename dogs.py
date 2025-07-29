from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = Label()
label.pack(pady=15)

btn = Button(text='Загрузить изображение', command=show_image)
btn.pack()

window.mainloop()
