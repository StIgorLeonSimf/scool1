from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get(
            'https://dog.ceo/api/breed/affenpinscher/images/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as er:
        messagebox.showerror('Ошибка', f"Воникла ошибка при "
                                       f"запросе API изображения {er}")
        return None



def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img
        except Exception as er:
            messagebox.showerror('Ошибка', f"Воникла ошибка при "
                                           f"загрузке изображения {er}")
            return None
    progress.stop()


def prog():
    progress['value'] = 0
    progress.start(30)
    window.after(3100, show_image)



window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = ttk.Label()
label.pack(pady=15)

btn = ttk.Button(text='Загрузить изображение', command=prog)
btn.pack()

progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(pady=10)
window.mainloop()
