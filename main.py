import os
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image
from pydub import AudioSegment
from moviepy import VideoFileClip

def convert_image(input_file, output_file, output_format):
    try:
        with Image.open(input_file) as img:
            img.save(output_file, format=output_format.upper())
        messagebox.showinfo("Конвертация завершена", f"Изображение успешно конвертировано в {output_format.upper()}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось конвертировать изображение: {e}")

def convert_audio(input_file, output_file, output_format):
    try:
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format=output_format)
        messagebox.showinfo("Конвертация завершена", f"Аудио успешно конвертировано в {output_format}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось конвертировать аудио: {e}")

def convert_video(input_file, output_file, output_format):
    try:
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', threads=4)
        messagebox.showinfo("Конвертация завершена", f"Видео успешно конвертировано в {output_format}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось конвертировать видео: {e}")


def select_file():
    file_path = filedialog.askopenfilename(title="Выберите файл", filetypes=[("All files", "*.*")])
    entry_file.delete(0, END)
    entry_file.insert(0, file_path)

def convert_file():
    input_file = entry_file.get()
    output_format = combo_format.get()
    
    if not input_file or not output_format:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите файл и формат.")
        return
    
    _, ext = os.path.splitext(input_file)
    ext = ext[1:].lower()

    output_file = filedialog.asksaveasfilename(defaultextension=f".{output_format}", 
                                               filetypes=[(output_format.upper(), f"*.{output_format}")])
    
    if not output_file:
        return
    
    if ext in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
        convert_image(input_file, output_file, output_format)
    elif ext in ['mp3', 'wav', 'flac']:
        convert_audio(input_file, output_file, output_format)
    elif ext in ['mp4', 'avi', 'mov']:
        convert_video(input_file, output_file, output_format)
    else:
        messagebox.showerror("Ошибка", "Невозможный формат для конвертации.")

root = Tk()
root.title("Конвертер файлов")
root.geometry("450x250")

# Поле для выбора файла
label_file = Label(root, text="Выберите файл:")
label_file.pack(pady=10)

entry_file = Entry(root, width=40)
entry_file.pack(pady=5)

button_browse = Button(root, text="Обзор", command=select_file)
button_browse.pack(pady=5)

label_format = Label(root, text="Выберите формат:")
label_format.pack(pady=10)

combo_format = ttk.Combobox(root, values=["jpg", "png", "gif", "mp3", "wav", "flac", "mp4", "avi", "mov"])
combo_format.pack(pady=5)

button_convert = Button(root, text="Конвертировать", command=convert_file)
button_convert.pack(pady=20)

root.mainloop()