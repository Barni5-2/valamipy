import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append('/')
import program.refresh
import program.format

main_file = program.refresh.refresh_file()
main_class = program.format.format_to_class(main_file)

def show_alert(title, desc):
    msg=messagebox.showinfo(title, desc)

def init_gui():
    root = tk.Tk()
    label = tk.Label(root, text="SlágerLista")
    label.pack()

    root.title('SlágerLista')
    root.geometry("400x300+300+120")
    root.resizable(False, False)
    root.attributes("-alpha", 0.95)

    entry = tk.Entry(root)
    entry.pack()

    listbox = tk.Listbox(root)
    for i in range(len(main_class)):
        listbox.insert(tk.END, main_class[i].name)
    listbox.pack()

    button = tk.Button(root, text="Suicide", command = show_alert("test","test"))
    button.pack()

    root.mainloop()