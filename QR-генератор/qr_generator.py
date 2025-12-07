#Создание окон, даем короткое название tk
import tkinter as tk 
#Импортируем диологовое окно, окно проводника и всплывающие сообщения
from tkinter import simpledialog, filedialog, messagebox
#Создание кодов
import qrcode

#Создаем окно в переменной window 
window = tk.Tk()

#Задаем переменной window заголовок и размер
window.title("Быстрый QR")
window.geometry("300x200")

#Создание функции quick_qr
def quick_qr():
    #Из модуля simpledialog вызываем функцию askstring 
    text = simpledialog.askstring("Текст", "Что закодировать?:")
    if not text: return
    
    #Из модуля simpledialog вызываем функцию askstring для названия файла
    name = simpledialog.askstring("Имя", "Имя файла (без расширения):")
    if not name: name = "qr"
    
    #Из модуля filedialog вызываем функцию askdirectory для выбоа папки сохранения
    folder = filedialog.askdirectory(title="Куда сохранить?")
    if not folder: return
    
    #Создаем и сохраняем код, с пощью f делаем строку форматированной
    #А также вставляем путь и имя файла с рсширением, с помощью ранее введенных переменных 
    qrcode.make(text).save(f"{folder}/{name}.png")

    #Из модуля messagebox вызываем функцию showinfo для показа инф. сообщения
    messagebox.showinfo("Готово!", "QR-код создан!")

#Создаем кнопку, привязываем ее к окну windiw и задаем команду с названием функции
tk.Button(window, text="Создать QR", command=quick_qr,
          #С помощью pack размещяем эту кнопку в окне
          #С помощью expand=True растягиваем кнопку на все окно
          font=("Arial", 16), bg="#7544BE", fg="white").pack(expand=True)

# Запускаем главный цикл - окно появится и будет ждать действий
window.mainloop()
