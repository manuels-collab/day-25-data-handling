from tkinter import *

def calc_km():
    km = first_entry.get()
    answer = float(km) * 1.60934
    result.config(text=f'{answer}')

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
#Label

result = 0

first_entry = Entry()
first_entry.grid(row=0, column=1)

first_label = Label(text="Miles")
first_label.grid(row=0, column=2)

second_label = Label(text="is equal to")
second_label.grid(row=1, column=0)

result = Label(text=f"{result}")
result.grid(row=1, column=1)

third_label = Label(text="Km")
third_label.grid(row=1,  column=2)

#Button
my_button = Button(text="Calculate", command=calc_km)
my_button.grid(row=2, column=1)





window.mainloop()