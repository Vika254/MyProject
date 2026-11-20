import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("MyProject", "Программа успешно установлена!")

root = tk.Tk()
root.title("MyProject")
root.geometry("400x250")

label = tk.Label(
    root,
    text="Моя первая программа",
    font=("Arial", 16)
)
label.pack(pady=30)

button = tk.Button(
    root,
    text="Нажми меня",
    command=show_message
)
button.pack()

root.mainloop()