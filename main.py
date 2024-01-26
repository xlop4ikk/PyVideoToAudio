import tkinter as tk
import pytube as pt
from pytube import YouTube
import os

#-----------------------------------------------------------
# Создание формы
#-----------------------------------------------------------

root = tk.Tk()
root.title("PyVideoToAudio")
root.geometry("300x100")
root.resizable(False, False)
root.configure(bg="white")

label_1 = tk.Label(root, text="Ссылка на видео:", bg="white", fg="black", font="Consolas")
text_box_1 = tk.Entry(root, width=30)

#-----------------------------------------------------------
# Функция конвертации видео в аудио 
#-----------------------------------------------------------

def convertation():
    your_url = text_box_1.get()
    url = pt.YouTube(your_url)
    video = url.streams.filter(only_audio=True).first()
    downloaded_file = video.download()
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    print("Done")

#-----------------------------------------------------------
# Реализация программы
#-----------------------------------------------------------

button_1 = tk.Button(root, text="Конвертировать!", command=convertation)
label_1.pack()
text_box_1.pack()
button_1.pack(ipadx=20, ipady=8, pady=5, side= "top")

root.mainloop()