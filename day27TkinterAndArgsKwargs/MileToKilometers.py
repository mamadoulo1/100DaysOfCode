from tkinter import *

#Button
def button_clicked():
    value = float(input.get())
    km = round(value * 1.609)
    zero.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=20, height=20)

# Label
is_equal_to = Label(text="is equal to")
is_equal_to.config(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Label
miles = Label(text="Miles")
miles.config(text="Miles")
miles.grid(column=2, row=0)

# Label
km = Label(text="Km")
km.config(text="Km")
km.grid(column=2, row=1)

# Label
zero = Label(text="0")
zero.config(text="0")
zero.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)



#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)




window.mainloop()

