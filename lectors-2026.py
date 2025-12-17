
import tkinter as tk
from tkinter import ttk
import time



llistacontrols = ["gracia", "sants", "can cuias", "papiol", "olesa"]

marc = tk.Tk()
marc.title('Barcelona-Montserrat')
marc.geometry('800x480')
marc.columnconfigure(0, weight=1)
marc.rowconfigure(0, weight=1)
marc.rowconfigure(1, weight=9)



entrades = tk.Frame(marc)
entrades.config()
entrades.grid(row=0, column=0, sticky="nsew")
entrades.columnconfigure (0, weight=6)
entrades.columnconfigure (1, weight=2)
entrades.columnconfigure (2, weight=1)
entrades.columnconfigure (3, weight=1)
entrades.rowconfigure (0, weight=1)

hora=tk.Label(entrades)
hora.config(font=("Arial", 30))
hora.grid(row=0, column=1, sticky="nsew")

control=ttk.Combobox(entrades, values=llistacontrols, state="readonly")
control.config(text="coll d'olesa", font=("Arial", 30))
control.grid(row=0, column=0, sticky="NSEW")

gps = tk.Label(entrades)
gps.config(bg='red', text="gps", font=("Arial", 15))
gps.grid(row=0, column=2, sticky="nsew")
xarxa=tk.Label(entrades)
xarxa.config(bg='yellow', text="xar", font=("Arial", 15))
xarxa.grid(row=0, column=3, sticky="nsew")

sortides=tk.Frame(marc)
sortides.config()
sortides.columnconfigure(0, weight=6)
sortides.columnconfigure(1, weight=4)
sortides.rowconfigure(0, weight=1)
sortides.grid(row=1, column=0, sticky="nsew")

sort1=tk.Frame(sortides)
sort1.config()
sort1.columnconfigure(0, weight=1)
sort1.columnconfigure(1, weight=3)
sort1.rowconfigure(0, weight=1)
sort1.grid(row=0, column=0, sticky="nsew")

etdorsal = tk.Label(sort1)
etdorsal.config(text="dorsal:", font=("Arial", 15))
etdorsal.grid(row=0, column=0, sticky="n")

dorsal=tk.Label(sort1)
dorsal.config(bg='blue', text="dorsal", font=("Arial", 50))
dorsal.grid(row=0, column=1, sticky="n")

sort2=tk.Frame(sortides)
sort2.config()

sort2.grid(row=0, column=1, sticky="nsew")

for x in  llistacontrols:
    nomdorsal = tk.Label(sort2)
    nomdorsal.config(bg='green', text=x, font=("Arial", 20))
    nomdorsal.grid(row=llistacontrols.index(x), column=1, sticky="nsew")

    numdorsal = tk.Label(sort2)
    numdorsal.config(bg='yellow', text="123", font=("Arial", 20))
    numdorsal.grid(row=llistacontrols.index(x), column=2, sticky="nsEW")


def tick():
    temps=time.strftime("%H:%M:%S")
    hora.config(text=temps)
    hora.after(500, tick)

tick()


marc.mainloop()
