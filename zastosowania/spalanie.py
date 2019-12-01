from tkinter import Tk, Label, Entry, Button

"""
Napisz program obliczający koszt przejazdu na zadanym dystansie

uzytkownik wprowadz w GUI: cena 1l paliwa, spalanie na 100 km, dystans
"""


def licz_spalanie():
    cena = float(cena_entry.get())
    spalanie = float(spalanie_entry.get())
    dystans = int(dystans_entry.get())
    koszt = (dystans / 100) * spalanie * cena
    wynik_label.configure(text=f"Koszt: {koszt:.2f}")

root = Tk()

cena_label = Label(master=root, text="Cena 1L paliwa")
cena_label.grid(row=1, column=1)
cena_entry = Entry(master=root)
cena_entry.grid(row=1, column=2)

spalanie_label = Label(master=root, text="Spalanie na 100 km")
spalanie_label.grid(row=2, column=1)
spalanie_entry = Entry(master=root)
spalanie_entry.grid(row=2, column=2)

dystans_label = Label(master=root, text="Dystans")
dystans_label.grid(row=3, column=1)
dystans_entry = Entry(master=root)
dystans_entry.grid(row=3, column=2)

button = Button(master=root, text="Oblicz", command=licz_spalanie)
button.grid(row=4, column=2)

wynik_label = Label(master=root, text="")
wynik_label.grid(row=5, column=2)

root.mainloop()
