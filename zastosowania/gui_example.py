import tkinter
def sumuj():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        w = a + b
        wynik.configure(text=f"wynik: {w}")
    except ValueError:
        print("Niepoprawne użycie. Wartości powinny być liczbami")
        wynik.configure(text=f"Niepoprawne użycie. Wartości powinny być liczbami")

root = tkinter.Tk()
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=3)
a_label = tkinter.Label(master=root, text="Liczba a")
a_label.grid(row=1, column=1)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=1, column=2)

b_label = tkinter.Label(master=root, text="liczba b")
b_label.grid(row=2, column=1)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=2, column=2)

add_button = tkinter.Button(master=root, text="Sumuj", command=sumuj)
add_button.grid(row=3, column=1)
wynik = tkinter.Label(master=root, text="-")
wynik.grid(row=4, column=1)

root.mainloop()

print("To się wykona dopiero po zakończeniu ")
