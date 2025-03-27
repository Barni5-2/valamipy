import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x200")
root.title("Slágerlista")
frm = ttk.Frame(root, padding=25)

frm.grid()

ttk.Label(frm, text="Slágerlista").grid(column=1, row=0)
ttk.Button(frm, text="Felvétel", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text="Lista", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="Átrendezés", command=root.destroy).grid(column=1,  row=3)
ttk.Button(frm, text="Kilépés", command=root.destroy).grid(column=1, row=4)

root.mainloop()